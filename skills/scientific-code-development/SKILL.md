---
name: scientific-code-development
description: Develop, debug, review, or extend scientific and numerical software in Python, C++, or other languages. Use for numerical correctness, established API reuse, HPC efficiency, data/memory handling, state/restart behavior, and meaningful validation. Compare plausible implementations when the best choice is uncertain. Does not impose a research-experiment workflow on every small code edit.
---

# Scientific code development

Produce maintainable scientific code with explicit numerical semantics and
evidence for the behavior and resource claims that matter. Use ordinary source,
file, build and execution tools in Codex or OpenCode; no particular dependency
or second agent is required. Scale the work to the task's numerical risk/cost.

## Establish the contract and reuse existing work

Read project instructions, interfaces, conventions, dependencies, build and
test commands. Identify the actual import/binary path, supported versions and
execution backend. Specify inputs/outputs, units, shapes/association, index
conventions, precision and a small observable correctness criterion.

Search the project and installed dependencies for suitable functionality before
implementing a replacement. Inspect the relevant API's contract and callers;
prefer maintained optimized library/project operations that fit the semantics.
Do not replicate an unfamiliar API, create a parallel interface, or add a new
dependency without a concrete benefit. Explain a custom implementation or a
departure from the established API. Stop searching once the required semantics
are established; resolve remaining issues through focused builds/tests.

For framework-specific work, apply its conventions (for example the
OpenFOAM.com development skill when available). Do not mix another fork's APIs
or override a project's numerical conventions with generic defaults.

## Choose a correct, efficient implementation

Read [numerical correctness](references/numerical-correctness.md) when selecting
or changing algorithms. Establish numerical stability, tolerances, conditioning,
normalization, convergence and relevant invariants before optimizing.

Among candidates meeting required correctness, stability and interface behavior,
favor efficiency for the expected workload. Assess work complexity, peak memory,
allocations/copies, locality, device transfers, communication, synchronization
and I/O. Read [data and performance](references/data-and-performance.md) when
these tradeoffs matter. Prefer suitable optimized operations, buffer reuse and
distributed/batched/streaming methods over unnecessary materialization. Do not
assume vectorization, a GPU, more threads/ranks, or fewer source lines is faster.

If the best suitable option is uncertain, list the plausible candidates and
decision criteria. Rule out incorrect or capacity-infeasible choices first.
Run a bounded representative comparison when useful and within authorization;
otherwise propose exact inputs, metrics, tolerances and resource limits needed
to resolve the choice. Apply `numerical-experiments` if available for substantial
benchmarks; small comparisons need only correctness checks, fair inputs/settings,
completion-aware timing, repeats and raw evidence. Do not require an unrelated
model comparison or a production-scale job to settle a local implementation.

Report observed sizes/settings and variation. Distinguish predicted complexity
from measured performance, and state workload-dependent crossovers/ties rather
than inventing a universal winner. Keep the simpler established solution when
further comparison would not change a meaningful decision.

## Implement and handle lifecycle

Preserve interfaces and intentional compatibility; document new defaults and
failure behavior. Use the project's naming, file headers, documentation and
licensing conventions without inventing authorship. Read
[interfaces and documentation](references/interfaces-and-documentation.md) when
state, persistent output, restart or repeated invocation are affected.

Make ownership, copies/views, dtype/device conversions and object lifetimes
intentional. Define which state persists, which can be rebuilt, and when caches
are invalidated. Account for interruption, partial output and retries where
applicable; do not add recovery machinery to a stateless small function.

## Validate and deliver

Read [testing and validation](references/testing-and-validation.md). Use analytic
results, manufactured solutions, suitable invariants or a trusted independent
implementation; avoid making the changed implementation its own sole oracle.
Exercise relevant shape/precision/invalid-input and scaling-dependent paths.
For stateful work, test restart/repeated calls; for resource-impact changes,
assess peak memory and repeated-use growth as well as elapsed time.

Run appropriate existing tests and actual changed entry points. Preserve user
inputs and keep generated data/build artifacts isolated. Report the change,
reused facilities, actual numerical/resource checks, reproduction commands,
versions/settings, and remaining limitations. A successful build, a plausible
plot, or a toy benchmark does not prove scientific validity or HPC scalability.
