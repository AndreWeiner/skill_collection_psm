# Execution and host integration

## Discovery and provider boundaries

Check the installed host's command help before relying on options. Inspect only
provider/model identifiers and nonsecret metadata from configuration. Never
dump full configuration, authentication files, or environment variables.

OpenCode: `opencode models` lists catalog entries; `opencode models PROVIDER`
filters the configured ScaDS identifier. Use metadata or provider documentation
to shortlist suitable models. Exact provider/model strings must come from the
live setup. Confirm account access through the requested runs, not extra paid
probe calls. Do not refresh configuration or change defaults unnecessarily.

Codex: use model IDs exposed by the current host, its documented inventory, or
the user's explicit selection. Read current official OpenAI documentation if
capabilities or endpoint compatibility need verification. The catalog of API
models and the models available to Codex subscriptions can differ. Confirm the
selected execution tool actually supports each candidate. Check the effective
provider is OpenAI; do not assume every Codex configuration uses OpenAI.

ChatGPT: use an available tool that explicitly supports independent OpenAI
model calls. Ordinary conversation access does not establish this capability.
If none exists, perform comparison of supplied artifacts. Do not claim this
folder has installed a ChatGPT plugin or enabled model switching.

## Running tasks

For each candidate create a private output directory and a workspace containing
the same task inputs. A workspace copy is often enough; use isolated Git
worktrees when appropriate, remembering they do not include uncommitted inputs
automatically. Avoid copying secrets, credentials, unrelated large data, or
the controller's comparison instructions into candidate workspaces. Preserve
task-relevant instructions equally for all candidates. Explicitly tell each
candidate to perform only the original task, not launch comparisons.

Use structured subprocess arguments rather than shell-interpolating prompts.
Store a shared UTF-8 prompt file and per-run stdout/stderr files. Examples below
describe options, not universal commands; check local help and permissions.

- OpenCode: `opencode run --model PROVIDER/MODEL --format json --dir WORKSPACE`
  with the shared task prompt and input attachments. Use a fresh run, without
  `--continue` or `--session`. Keep permissions restricted to task requirements;
  do not use blanket auto-approval to overcome blocked execution.
- Codex: `codex exec --model MODEL --json --cd WORKSPACE --sandbox workspace-write`
  with the shared prompt through stdin and, when supported,
  `--output-last-message OUTPUT`. Use `--skip-git-repo-check` only for a deliberately
  non-repository workspace. Do not bypass approval or sandbox controls.
- Native host tools: use only supported model overrides and actual independent
  sessions. A user-authorized comparison permits candidate executions, but
  does not authorize messaging unrelated chats or changing account settings.

Bound run time with the available process timeout facility, terminate any owned
child processes on timeout, and retain partial artifacts as such. Prefer
sequential execution initially. Record actual effective settings and any
provider errors; unsupported models remain unavailable, without silent fallback.

## Visual routes

For sketches or conceptual figures, code-generated SVG or a diagram format is
a useful shared route for text models. For scientific plots use supplied data
and a common plotting environment. Tell candidates where to save source and
rendered output. If no data is supplied, clearly label any requested illustrative
data; do not present invented values as measurements.

Render generated code only within the task's authorized sandbox. Candidate HTML
is an output file, not trusted controller code. Prefer raster previews of active
content; the bundled gallery never embeds candidate HTML as executable content.
PDFs and SVGs can retain original links while using PNG previews produced by
available rendering tools. Record rendering failures separately from generation
failures. If candidates receive different rendering interventions, disclose them.

Direct image generation requires a confirmed image-generation endpoint/tool for
the exact requested model. Do not send a text-model ID to an image endpoint or
silently use one shared image model and label images as different text models.
If comparing text models that call the same image generator, label it as a
comparison of orchestration/prompting and record both models.

## Registration

Maintain one folder. OpenCode discovers `.opencode/skills/model-compare` and
Codex discovers `.agents/skills/model-compare`; directory symlinks can share this
collection's source folder. Global registration affects other projects and is
separate from project registration. Restart or refresh the host to discover a
new skill. For ChatGPT packaging, verify the target environment's current skill
or plugin import mechanism rather than assuming local filesystem discovery.

Sources checked during creation (2026-10-09):
- https://opencode.ai/docs/skills/
- https://opencode.ai/docs/cli/
- https://developers.openai.com/codex/skills/
