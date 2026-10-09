# Host integration

Use a single maintained skill folder when sharing a workflow between agents.
Do not copy the same definition into several locations unless there is a clear
update strategy. A local directory symlink can expose the maintained folder to
a host's discovery path on systems that support it.

## OpenCode

The locally checked OpenCode 1.18.35 discovers project skills under
`.opencode/skills/<name>/SKILL.md` and global skills under
`~/.config/opencode/skills/<name>/SKILL.md`. It also recognizes compatible
`.agents/skills` and `.claude/skills` locations.

Use `opencode debug skill` to check the discovered inventory. This command may
initialize plugins and write logs; use `opencode --pure debug skill` when an
inventory should skip external plugins. Check the target version before relying
on configuration fields: other versions can use different schemas.

Project registration applies only in that project. Global registration affects
other projects too, so choose it only when that scope matches the request.
Restart an existing OpenCode session after adding or changing skill definitions.

Official documentation: https://opencode.ai/docs/skills/

## Codex

Project skills can be stored under `.agents/skills/<name>/SKILL.md`. Personal
skills can be stored under `$CODEX_HOME/skills/<name>/SKILL.md`, using
`~/.codex/skills` when `CODEX_HOME` is unset.

Codex-specific `agents/openai.yaml` is optional for a portable definition;
omit it unless Codex UI metadata or an invocation policy is needed. When adding
it, use the host's current schema and validation tooling rather than assuming
another installed skill is available.
Codex already includes a skill named `skill-creator`. Keep this collection's
version registered in OpenCode; if registering it in Codex, choose a distinct
name unless explicitly asked to override an existing definition.
Check the available-skills list in a fresh session to verify registration.

## Claude Code

Project skills can be stored under `.claude/skills/<name>/SKILL.md`; personal
skills can be stored under `~/.claude/skills/<name>/SKILL.md`.
Confirm current host documentation before adding Claude-specific fields or
assuming a particular invocation mechanism.
