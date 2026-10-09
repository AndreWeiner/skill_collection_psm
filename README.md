# Scientific agent skills and tools

A collection of reusable scientific workflows for OpenCode and ChatGPT/Codex,
with a practical OpenCode setup for TU Dresden's TUD:AI (ScaDS.AI) service.
This is a personal collection, not an official TU Dresden distribution.

## Start here

1. [Set up OpenCode at TU Dresden](docs/opencode-tu-dresden.md).
2. [Install and invoke skills](docs/installation.md).
3. [Choose a skill](docs/catalog.md).
4. [Install OpenCode plugins, commands and agents](docs/opencode-extensions.md).
5. [Set up voice input](docs/voice-input.md).

Agents should read [AGENTS.md](AGENTS.md) and the selected skill's `SKILL.md`.
Skills describe workflows; plugins add executable host behavior; commands and
agents provide OpenCode entry points. Installing one does not install the others.

## Contents

- `skills/`: eight maintained skills, with their references, scripts and assets.
- `opencode/`: credential-free provider example, model-sync plugin, voice command,
  and report-reviewer agent.
- `tools/voice/`: Linux dictation helpers.
- `scripts/`: selective skill registration.
- `tests/`: existing offline checks for helpers and scientific plot styling.
- `docs/`: setup, compatibility, usage and maintenance guidance.

Local validation runs and generated artifacts remain on disk but are excluded
from Git, along with credentials, dependencies and personal host configuration.

## Validation and contributions

Run `python3 -m unittest discover -s tests -v`. The plotting checks require
Matplotlib and Pillow; the LaTeX export check skips when its tools are absent.
Remote service access, microphones and desktop shortcuts require separate checks.

For a new skill, add `skills/<name>/SKILL.md` with matching `name` and a concise
`description`, then list its dependencies, compatibility and example in the
catalog. Keep host-specific integration in `opencode/` or `tools/` and update the
relevant setup guide. Do not commit keys, recordings or private experiment data.
No redistribution license has been selected yet; contact the author for terms.
