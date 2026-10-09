# HPC efficiency and implementation comparisons

Choose the efficient suitable implementation, not merely the shortest code.
First inspect optimized OpenFOAM.com APIs and their actual semantics. Estimate
work and memory as functions of cells/faces, fields/components, snapshots,
iterations and ranks as relevant to the change.

Review temporary fields, repeated allocation, avoidable conversions/copies,
recomputed geometry/addressing, and data locality. Reuse valid buffers or cached
geometry when it helps, with explicit lifetime and invalidation rules. Track
per-rank peak memory as well as aggregate memory; growing state over time can
matter more than the cost of one invocation.

Prefer distributed reductions to gathering full data. Consider communication
volume, collective count, synchronization, load imbalance, and empty partitions.
Adding ranks may increase memory replication or communication cost even when
serial arithmetic is linear. Consider output frequency, metadata/file counts,
collated/uncollated behavior, and filesystem pressure when I/O changes.

## Resolve uncertain alternatives

State candidate implementations, equivalent numerical semantics, acceptable
error/tolerance, and the quantity deciding the choice (for example end-to-end
time under a memory limit). Rule out unsuitable candidates by correctness,
complexity, API support, or capacity before timing them.

For remaining plausible alternatives, use the same inputs, precision, compiler
optimization, rank/thread settings, and included phases. Check numerical
agreement before timing. Use a bounded pilot, warm-up/repeats where appropriate,
and raw samples. Measure actual completion and peak-memory differences; include
loading, transfers, communication and writing when claiming end-to-end speed.
Apply `numerical-experiments` if available for substantial comparisons; these
requirements are sufficient to proceed without that skill on a small case.

Use representative mesh sizes and partitions or explain why they are unavailable.
Report observed workload/range, variation, and limits. If time differences are
inside noise or different sizes favor different approaches, state the tradeoff
instead of inventing a universal winner. Prefer the simpler established option
when it meets requirements and further measurement would not change the choice.

Implementation comparison is distinct from comparing agent/model outputs. Use
model-comparison tooling only when comparing models is itself useful/requested.
Do not launch production jobs or broaden hardware/allocation scope merely to
settle a local coding choice; propose an exact bounded test if scope is missing.
