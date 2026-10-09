# OpenCode extensions

The files below were collected from the author's local OpenCode setup on
2026-10-09. Install each component selectively. For OpenCode 1.18.35, the
source installation used singular `plugin/` and `agent/` directories; current
[plugin documentation](https://opencode.ai/docs/plugins/) uses `plugins/`.
Check your host version rather than registering the same file twice.

## ScaDS model-sync plugin

Copy `opencode/plugins/scads-model-sync.ts` into
`~/.config/opencode/plugins/` (create the directory first). It is loaded at
startup on hosts using documented plugin discovery. The type import is from
`@opencode-ai/plugin`; the source setup had version 1.18.35.

The plugin queries `/models` with `SCADSAI_API_KEY`, filters entries with
`mode == "chat"`, and adds missing models to `provider.scads.models` in the
global JSON config. It checks at startup when the previous successful check
was at least 24 hours ago; failures have a one-hour retry cooldown. It does not
run a background timer, remove unavailable models, or change the default model.
It logs removed catalog entries as warnings.

Back up the target configuration first. This plugin rewrites plain JSON when
adding models; JSONC comments are unsupported. Its asynchronous update may
require a restart before new models appear in the current session.

Optional environment overrides: `SCADS_MODEL_SYNC_CONFIG`,
`SCADS_MODEL_SYNC_STATE`, `SCADS_MODEL_SYNC_LOG`. Defaults are under
`~/.config/opencode`. Set these explicitly for a project config or custom
configuration directory. State and logs are local files excluded from Git.
Remove the installed plugin file to disable future checks.

## Voice slash command

Copy `opencode/commands/voice.md` into `~/.config/opencode/commands/`.
Install the helper and dependencies following [voice-input.md](voice-input.md).
Use `/voice` for five seconds or `/voice 10` for ten seconds. Its transcription
enters the agent prompt, so inspect whether your host submits it immediately
before using dictation for actions with side effects.

## Report-reviewer agent

Copy `opencode/agents/report-reviewer.md` into
`~/.config/opencode/agents/` (or the source version's `agent/` directory).
Register `report-consistency` and, if needed, `image-review` separately.
Restart and ask OpenCode to delegate the finished report to `report-reviewer`,
passing the document path and its data sources. It reports findings and denies
file edits; inspect shell/tool permissions separately if strict read-only
execution is required. It is a prompt agent, not a sandbox boundary.

For the agent format, see [official agents documentation](https://opencode.ai/docs/agents/).
The repository's `AGENTS.md` supplies task routing, without installing personal
global rules or requiring delegation for every small edit.
