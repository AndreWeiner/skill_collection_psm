import type { Plugin } from "@opencode-ai/plugin"
import fs from "node:fs/promises"
import os from "node:os"
import path from "node:path"

const BASE_URL = "https://llm.scads.ai/v1"
const DAY_MS = 24 * 60 * 60 * 1000
const RETRY_MS = 60 * 60 * 1000

const stateFile =
  process.env.SCADS_MODEL_SYNC_STATE ??
  path.join(os.homedir(), ".config/opencode/.scads-model-sync.json")
const configFile =
  process.env.SCADS_MODEL_SYNC_CONFIG ??
  path.join(os.homedir(), ".config/opencode/opencode.json")
const logFile =
  process.env.SCADS_MODEL_SYNC_LOG ??
  path.join(os.homedir(), ".config/opencode/.scads-model-sync.log")

const emit = (msg: string, err = false) => {
  if (err) console.error(`[scads-model-sync] ${msg}`)
  else console.log(`[scads-model-sync] ${msg}`)
  void fs
    .appendFile(logFile, `${new Date().toISOString()} ${msg}\n`)
    .catch(() => {})
}

interface RemoteModel {
  id: string
  mode?: string
  max_input_tokens?: number
  max_output_tokens?: number
}

interface ModelEntry {
  name: string
  limit?: { context: number; output: number }
}

type Models = Record<string, ModelEntry>

interface ConfigShape {
  provider?: { scads?: { models?: Models } }
}

const readJson = async <T>(file: string): Promise<T> =>
  JSON.parse(await fs.readFile(file, "utf8"))

const toEntry = (m: RemoteModel): ModelEntry => {
  const entry: ModelEntry = {
    name: m.id
      .split("/")
      .pop()!
      .replace(/[-_]/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase()),
  }
  if (
    typeof m.max_input_tokens === "number" &&
    typeof m.max_output_tokens === "number"
  ) {
    entry.limit = { context: m.max_input_tokens, output: m.max_output_tokens }
  }
  return entry
}

async function sync(): Promise<RemoteModel[]> {
  const state = await readJson<Record<string, unknown>>(stateFile).catch(
    () => ({}) as Record<string, unknown>,
  )
  const now = Date.now()
  if (now - Number(state.lastCheck ?? 0) < DAY_MS) {
    emit(
      `skipped, last check was ${state.checkedAt ? new Date(String(state.checkedAt)).toISOString() : "recent"} (< 24h ago)`,
    )
    return []
  }
  if (state.lastError && now - Number(state.lastAttempt ?? 0) < RETRY_MS) {
    emit(`skipped, last error "${state.lastError}" < 1h ago`)
    return []
  }

  try {
    if (!process.env.SCADSAI_API_KEY) throw new Error("SCADSAI_API_KEY not set")

    const res = await fetch(`${BASE_URL}/models`, {
      headers: { Authorization: `Bearer ${process.env.SCADSAI_API_KEY}` },
      signal: AbortSignal.timeout(15000),
    })
    if (!res.ok) throw new Error(`models API returned HTTP ${res.status}`)
    const remote: RemoteModel[] = (await res.json()).data.filter(
      (m: RemoteModel) => m.mode === "chat",
    )

    const cfg = await readJson<ConfigShape>(configFile)
    const models = cfg?.provider?.scads?.models
    if (!models) throw new Error(`no provider.scads.models in ${configFile}`)

    const added = remote.filter((m) => !models[m.id])
    const gone = Object.keys(models).filter(
      (id) => !remote.some((m) => m.id === id),
    )

    for (const m of added) models[m.id] = toEntry(m)
    if (added.length) {
      await fs.writeFile(configFile, JSON.stringify(cfg, null, 2) + "\n")
    }
    emit(
      `checked ScaDS API: ${remote.length} chat model(s) found, ${added.length} added${added.length ? `: ${added.map((m) => m.id).join(", ")}` : " (config is up to date)"}`,
    )
    if (gone.length) {
      emit(`warning, no longer offered: ${gone.join(", ")}`)
    }

    await fs.writeFile(
      stateFile,
      JSON.stringify(
        {
          checkedAt: new Date(now).toISOString(),
          lastCheck: now,
          lastAttempt: now,
          added: added.map((m) => m.id),
          gone,
        },
        null,
        2,
      ) + "\n",
    )
    return added
  } catch (e) {
    await fs
      .writeFile(
        stateFile,
        JSON.stringify(
          {
            ...state,
            lastAttempt: now,
            lastError: e instanceof Error ? e.message : String(e),
          },
          null,
          2,
        ) + "\n",
      )
      .catch(() => {})
    throw e
  }
}

const plugin: Plugin = async () => {
  const pending = sync().catch((e: Error) => {
    emit(`error: ${e.message}`, true)
    return [] as RemoteModel[]
  })
  return {
    config: (cfg) => {
      void pending.then((added) => {
        const models = (cfg as ConfigShape)?.provider?.scads?.models
        if (models && added.length) {
          for (const m of added) if (!models[m.id]) models[m.id] = toEntry(m)
        }
      })
    },
  }
}

export default plugin
