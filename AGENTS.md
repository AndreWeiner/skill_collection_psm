# Instructions for agents using or maintaining this collection

Read `docs/catalog.md` to choose a relevant skill. Load the complete
`skills/<name>/SKILL.md` before using it, and read supporting references only
when the task needs them. In OpenCode use the native `skill` tool when registered;
in ChatGPT/Codex use the discovered skill mechanism. A skill name is not an
executable tool. If discovery is unavailable, read the file directly and state
that you are following its instructions manually.

Preserve the user's selected host, provider, task scope and permissions.
Registration does not authorize API calls, uploading files, installing software,
recording audio or changing global settings. Check the selected helper's real
dependencies and report unavailable capabilities plainly.

When maintaining this repository, follow [CONTRIBUTING.md](CONTRIBUTING.md).
Use a focused feature branch and the contributor's fork for pull requests to
upstream `main`; check remotes and preserve unrelated local changes.

When maintaining this repository:
- Keep `skills/` as the source of truth; preserve complete helper/reference trees.
- Do not copy personal configuration or secrets into distributable examples.
- Keep plugin, command and agent installation distinct from skill installation.
- Check relevant tests, document links and actual host discovery after changes.
- Review completed documentation for consistency using `report-consistency`.
- Do not claim that local filesystem registration installs a ChatGPT plugin.
- Exclude `validation/` output from publication unless explicitly curated.
