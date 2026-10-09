---
name: numerical-experiments
description: Design, implement, run, or audit numerical experiments, performance benchmarks, and parameter sweeps, including small generated-code harnesses. Use to validate correctness, measurements, execution paths, reproducibility, and resource use before costly runs. Does not require a full experiment workflow for ordinary unit tests or simple calculations.
---

# Numerical experiments

Produce trustworthy evidence within the requested resource scope. Use a staged
workflow: define the experiment, validate a small instance, run a representative
pilot, then expand only when the relevant checks pass. A successful process exit
or plausible-looking graph does not establish that the experiment is correct.
This workflow uses ordinary file and execution tools in Codex or OpenCode.

Keep the procedure proportional to the experiment's cost and risk. For a small
local check, inline assertions and a concise result record can be sufficient;
do not build an orchestration framework or load every reference by default.
Read only the guidance relevant to the actual measurement path. Inspect the
experiment's logs and code, not the agent's own conversation/event logs unless
they are needed to diagnose a tooling failure.

## Define the experiment before spending resources

Identify the question, compared methods, controlled variables, outputs and units,
and a falsifiable acceptance criterion. Specify what computation is measured,
what is excluded, the reference result, tolerances, repeat/warm-up policy, and
the intended hardware/software path. For a parameter sweep, distinguish tuning
from final evaluation and avoid selecting parameters on the final test data.

Inspect existing implementations, tests, and harnesses before generating code.
Use the project's domain conventions, build process, and suitable existing APIs.
Trace the actual executed entry point and imported module/binary, not just the
file you edited. Keep generated code, fixtures, logs, and outputs isolated.

Establish a proportional compute/time/memory/storage budget and stopping rule.
Use the user's limits and already authorized scope; do not add a confirmation
step when a requested run fits them. If large-run cost or scope is unresolved,
prepare and run the smallest useful checks before clarifying it. Do not silently
increase ranks, GPUs, dataset size, repetitions, or cluster-job duration.

## Smoke test: correctness and the real execution path

Run the smallest instance that exercises the intended algorithm, backend,
loading, and output path. Check against an analytic/manufactured result, a trusted
independent implementation, or appropriate mathematical invariants. Do not use
the same implementation or its saved output as its own sole oracle.

Verify values, shapes, units, dimensions, finite outputs, and failure behavior
where relevant. Add a nontrivial fixture that distinguishes the intended method
from a plausible wrong one (for example unequal weights for a weighted mean).
Check device placement, dtype, thread/rank counts, and actual input sizes.
A metadata label such as "GPU" is not evidence that computation ran there.
For larger scales, also test the behavior introduced by scaling (partitioning,
batching, storage, or shape-dependent code); a toy CPU test cannot validate it.

## Pilot: validate measurements before measuring at scale

Read [measurement checks](references/measurement-checks.md) for timing,
asynchronous execution, statistics, memory, and I/O. Audit timer boundaries,
work completion, metric definitions and units. Run a bounded pilot using the
same measurement path as the full experiment. Independently cross-check at
least one measured quantity: an outer wall-clock measurement, operation count,
known workload, or another suitable independent instrument.

Verify that result files are fresh, complete, parseable, and associated with the
correct run, parameters, and executed code. Validate parsing and aggregation on
known raw records, including failed/missing trials. Keep raw samples and failure
records; exclude invalid runs explicitly rather than silently dropping them.

Read [reproducibility and recovery](references/reproducibility-and-recovery.md)
for provenance, comparisons, and selective reruns. Estimate full-run cost from
the pilot with allowance for nonlinear scaling, initialization, and storage.
Check memory/disk capacity rather than inferring it from elapsed time alone.

## Gate the substantial run

Record the smoke/pilot evidence, measured configuration, relevant code/input
fingerprints, expected outputs, resource estimate, and the decision to proceed
or stop. Correctness, measurement, execution path, artifact integrity, and
resource checks must pass; failed or unverified required checks block expansion.
Optional unavailable checks narrow the claim rather than being called passed.

For substantial runs, read [the gate record](references/gate-record.md) and run
`scripts/check_gate.py` on the saved record. Where you control the expensive
harness, invoke that check before dispatch. Do not automatically launch a full
run from the smoke/pilot path. The helper checks records and fingerprints;
it cannot independently prove that recorded scientific claims are true.

If a failed check or budget estimate already rules out expansion, record the
reason and stop; do not build a full-run wrapper or elaborate gate package for
a run that will not be launched.

For a costly run using a new or substantially changed harness, perform a separate
preflight review of the executed code and raw evidence before expansion. Use an
independent reviewer when available and authorized; otherwise do a second pass
from the raw artifacts and identify it as self-review. Give a reviewer the metric
definitions, code, inputs and records, not only the author's summary. Keep that
review bounded and within the same resource scope.

Proceed within the existing authorization after the gates pass. Preserve partial
results, use bounded batches/checkpoints when useful, and stop on invalid outputs,
unexpected backend/configuration changes, or a breached budget. Revalidate the
affected gate after a meaningful change. Do not keep retrying an unexplained
failure or repeat the entire sweep just because one stage failed.

## Analyse and deliver

Recompute summaries from raw records and verify units, groupings, sample counts,
ratios, and plot labels. Distinguish measured findings from extrapolation and
statistical uncertainty. A timing difference inside observed noise does not
establish a speedup; a single small case does not establish convergence or
general scientific validity.

Before rerunning, classify the error's effect. A corrected parser, unit label,
summary, or plot can often reuse valid raw measurements; an incorrect workload,
timer boundary, backend, or input requires rerunning the affected measurements.
Explain the scope and retain the old records with their invalidation reason.

Deliver the reproduction command/configuration, raw-result and provenance paths,
checks actually performed, results with uncertainty appropriate to the data,
resource usage, and remaining limitations. Never claim a pilot validates an
unexercised large-scale path, or an agent review guarantees every future run.
