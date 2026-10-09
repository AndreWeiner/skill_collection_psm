# Skill catalog

All eight skills have portable `SKILL.md` entry points. OpenCode and local
ChatGPT/Codex can follow them after registration; actual execution depends on
the tools available in the selected host. None of these skills installs its
dependencies.

| Skill | Purpose | Dependencies / limits | Example request |
| --- | --- | --- | --- |
| [scientific-code-development](../skills/scientific-code-development/SKILL.md) | Scientific software changes; numerical semantics, APIs and data handling | Python/C++ project dependencies | Use this skill to review the numerical correctness of my solver. |
| [openfoam-com-development](../skills/openfoam-com-development/SKILL.md) | OpenFOAM.com C++ development and build/API work | Target OpenFOAM.com release and compiler | Use this skill to extend this function object for my OpenFOAM.com release. |
| [numerical-experiments](../skills/numerical-experiments/SKILL.md) | Experiments, benchmarks, parameter sweeps and evidence gates | Python 3 for gate helper; experiment dependencies | Use this skill to design and run a bounded performance benchmark. |
| [scientific-visualization](../skills/scientific-visualization/SKILL.md) | Scientific plots and spatial fields; verified exports | Matplotlib; LaTeX tools for default style; explicit fallback possible | Use this skill to prepare this plot for a paper. |
| [model-compare](../skills/model-compare/SKILL.md) | Independent model runs and a comparison gallery | Supported independent runners/model access; Python 3 gallery helper | Use this skill to compare the same task on two available models. |
| [image-review](../skills/image-review/SKILL.md) | Direct image inspection or optional ScaDS vision review | Python 3 and SCADSAI_API_KEY for ScaDS helper | Use this skill to check the axes and units in these supplied figures. |
| [report-consistency](../skills/report-consistency/SKILL.md) | Completed document audits of numbers, claims and references | Document/source access; format-specific tools where relevant | Use this skill to audit this finished report against its source data. |
| [skill-creator](../skills/skill-creator/SKILL.md) | Create and improve portable reusable workflows | Host discovery knowledge; overlaps bundled Codex name | Use this skill in OpenCode to turn this workflow into a reusable skill. |

`model-compare` can compare supplied outputs when independent model runners are
unavailable. `image-review` prefers direct inspection; its ScaDS path sends
images to an external service and needs authorization for that task.
`scientific-visualization` controls presentation, while `numerical-experiments`
checks experimental evidence. Use both when both parts of the task need work.

The helper programs have their own `--help`. Read the chosen skill before
running them, especially the experiment gate schema and gallery manifest format.
For installation, see [installation.md](installation.md).
