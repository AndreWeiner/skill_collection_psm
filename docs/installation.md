# Install and invoke skills

## OpenCode

Keep this checkout at a persistent path. Register selected skills globally:

```bash
python3 scripts/install_skills.py --host opencode scientific-code-development scientific-visualization
```

The helper creates directory symlinks under `~/.config/opencode/skills` and
refuses to overwrite existing entries. Run with `--dry-run` to inspect actions.
Updates to this checkout become visible through those links. Moving/deleting
the checkout breaks them; remove an installed link with `unlink PATH`.
For a project instead, pass `--destination /path/to/project/.opencode/skills`.
Use `opencode --pure debug skill` on versions supporting `--pure`, or check
`opencode debug --help` for the inventory command. Restart if changes are absent.

Ask, for example: “Use the scientific-visualization skill to improve this plot.”
OpenCode loads matching instructions through its native skill tool.
See [official discovery rules](https://opencode.ai/docs/skills/).

## ChatGPT desktop / Codex

For portable project registration:

```bash
python3 scripts/install_skills.py --host codex --destination /path/to/project/.agents/skills numerical-experiments model-compare
```

The current documented personal discovery path is `~/.agents/skills`, used by
this helper by default for `--host codex`. Older/local Codex setups may use
`~/.codex/skills`; use `--destination` only after checking your host.
Avoid duplicate registrations. This collection's `skill-creator` shares a name
with a bundled Codex skill; the helper refuses that name for Codex.

In a fresh session verify the available skill list. In Codex mention
`$numerical-experiments`; in ChatGPT select an available skill with `@`.
Automatic matching depends on each skill's description.
See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

Standalone desktop skills and distributable ChatGPT plugins are separate.
These folders are reusable skill sources, not a published ChatGPT plugin.
For web/mobile or distribution through the plugin directory, package the desired
skills using the [official plugin format](https://developers.openai.com/plugins/build/plugins)
and test the package in the target client. OpenCode TypeScript plugins cannot
be imported as ChatGPT plugins. No local registration command here performs a
ChatGPT plugin upload or enables remote tools/model switching.

## Manual registration

On systems without symlink support, copy the complete selected skill directory
(including references, scripts and assets) into the host's discovery directory.
Update that copy whenever the source changes. Install only what you need; skills
do not automatically install Python, OpenFOAM, plotting tools or API access.
