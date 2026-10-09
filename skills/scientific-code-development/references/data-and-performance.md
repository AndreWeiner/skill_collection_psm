# Data, memory, HPC efficiency and comparisons

Estimate work and memory in terms of the dimensions that can grow: elements,
components, snapshots, iterations and workers. Include intermediate arrays,
factorizations, buffers, copies, cached state and per-worker replication in
peak-memory estimates. An O(N) final result can hide an O(N squared) temporary.

Inspect ownership, array views/strides, contiguous materialization, dtype
conversion, device transfer and actual loading. Prefer optimized suitable
operations; use batching/streaming when full materialization exceeds capacity.
Vectorization can trade interpreter overhead for excessive temporary storage.
Reuse buffers/caches when valid, with bounded lifetime and invalidation rules.

For parallel work, consider communication volume, synchronization, load balance,
per-rank memory, thread oversubscription and output contention. Prefer reductions
or distributed operations to gathering full data for scalar results. Preserve
correct collective participation and account for empty/local partitions.
Async operations must complete before their time/results are interpreted.

## Comparing implementations

Name the candidates, intended workload and decision criterion before measuring.
Check equivalent semantics and numerical error first; reject unsuitable capacity
or complexity without running an enormous case. Benchmark only uncertain choices
that can affect a meaningful requirement. Small differences within noise do not
justify invasive complexity.

Use identical inputs and comparable precision, compiler/backend, thread/rank
settings, warm-up and included phases. Use a monotonic elapsed clock or suitable
backend instrumentation, wait for completion, keep raw repeated samples, and
record the size/settings. Include allocation, loading, transfers, communication
and output when the claimed metric includes them; otherwise label exclusions.

Compare peak memory/capacity as well as time when they constrain the workload.
Do not declare a tiny resident-array benchmark representative of disk-backed,
distributed or accelerator paths. If representative data/hardware/budget are
missing, propose a bounded comparison and give a provisional, reasoned choice.
Keep existing authorized limits; do not silently broaden allocations or install
new dependencies. Separate theoretical expectation, measured result and unknowns.
