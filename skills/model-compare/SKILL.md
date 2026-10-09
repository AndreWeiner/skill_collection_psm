---
name: model-compare
description: Run the same task with suitable models and present their text, sketches, figures, plots, or other artifacts side by side. Use ScaDS models in OpenCode and OpenAI models in Codex or ChatGPT; also compare supplied outputs when execution is unavailable. Evaluation and ranking are optional.
---

# Model compare

Create a comparison the user can inspect. Default to a labeled gallery and
neutral descriptions of visible differences, without scores or a winner.
Evaluate correctness or recommend a model only when requested.

## Choose the execution route

- In OpenCode, use the configured ScaDS provider. Discover its exact identifier
  and available models; do not guess model IDs or expose credentials.
- In Codex or ChatGPT, use OpenAI models. Prefer the host's available model-selectable
  execution tools or authenticated Codex CLI. Use the OpenAI API only when that
  route and its credentials are available and authorized. Do not silently route
  these hosts through ScaDS or a custom third-party provider.
- A skill cannot itself change the current chat model or make inaccessible
  models available. If independent model execution is unavailable, compare
  supplied outputs and identify their provenance as user supplied. Explain
  the missing execution capability; never simulate another model's result.

Read [references/execution.md](references/execution.md) for backend selection,
isolation, and visual generation. Read it before starting independent runs.

## Set up a fair comparison

Capture the task once: prompt, input files/data, required output, shared
instructions, and any requested constraints. Preserve those inputs verbatim
for all candidates. Use the user's model list when given. Otherwise shortlist
up to three suitable models from the selected backend and disclose the selection.
Catalog presence is not proof of account access. Do not invent capability,
price, context-window, or accessibility claims.

For visual tasks distinguish image understanding, direct image generation, and
code/specification generation. A text model can create plotting code or SVG;
vision support alone does not mean it can generate images. Use a common route
when possible; label comparisons across different routes explicitly.

Use fresh sessions and separate workspaces from the same input state. Do not
let candidates see each other's outputs. Include relevant uncommitted inputs
for repository tasks. Keep input data, installed rendering tools, skills,
permissions, and budgets comparable. Record unavoidable differences, model
IDs, reasoning settings, backend version, and run timestamps.

Default to one run per model, sequentially, with a bounded timeout (ten minutes
per run unless the task needs another limit). Respect user usage/cost limits;
if no spending telemetry is available, say so rather than claiming a cost cap.
Do not automatically retry failed paid runs or substitute another provider.
Treat a single run as an example of that model's output, not a general ranking.

## Collect and show results

Keep original outputs, source code, raw run logs, and any render errors. Record
each run as completed, failed, timed_out, or unavailable. Process completion
alone is insufficient: confirm that requested artifacts exist and can be opened.
Do not hide missing outputs or silently repair one model's solution. If a repair
is requested, preserve the original and label the additional intervention.

Render plots and diagrams with the same environment. Preserve aspect ratios,
use equally sized preview areas, and retain original resolution. Use matching
page selections for multipage documents; provide all pages through original
files. Never alter numerical data or plot axes merely to make previews match.

Present each model's artifacts side by side with exact model ID, generation
route, run status, and links to originals. In a narrow chat layout, use a labeled
sequence plus a gallery file. Describe observed layout/content differences only
after inspecting the outputs. Keep factual checking separate from preference.
Time and token usage may be shown if measured; unknown cost stays unknown.

The Python-standard-library helper builds a local HTML gallery without model
calls or executing candidate output:

```bash
python3 "$SKILL_DIR/scripts/build_gallery.py" /absolute/path/to/comparison.json
```

Resolve `SKILL_DIR` from this skill's actual location. The manifest format and
preview rules are in [references/gallery.md](references/gallery.md). Open the
gallery with the host's artifact/file preview when available and include a link
in the final response. The gallery describes supplied records; it does not
verify that model calls occurred.

## Optional evaluation

Only when requested, define criteria before reviewing outputs. Prefer shared
tests, numerical checks, and direct artifact inspection. Clearly label subjective
judgment and uncertainty. A model-based reviewer should see anonymized outputs
and the same rubric; do not treat its opinion as ground truth. Do not apply a
winning patch, publish artifacts, or switch the user's default model as a side
effect of comparison.
