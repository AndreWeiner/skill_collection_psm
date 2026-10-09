# Measurement checks

## Timing boundaries and completion

State whether the metric is end-to-end latency, steady-state throughput, or a
specific kernel/phase. Include real input loading, transfers, allocation,
materialization, communication, output/basis storage, or finalization when the
claimed metric includes them. Separate compilation/JIT, initialization, tuning,
and warm-up when excluded, and record their cost separately when relevant.

Use a suitable elapsed-time monotonic clock, for example Python's
`time.perf_counter_ns()`, with explicit conversion to reported units. CPU process
time is a different metric and can omit waiting or work in child processes.
For very short operations, measure a justified batch and account for the number
of operations and timer overhead; do not report artificial precision.

For asynchronous GPU work, use backend events or synchronization appropriate to
the stated metric. Ensure preceding work is complete before starting and all
measured work is complete before stopping. Host dispatch time is not device
execution time. Similarly, wait for subprocesses/futures and verify worker exits.
For distributed latency, define rank synchronization and the summary (often
the slowest participating rank), rather than comparing incomparable rank-local
intervals. Inspect actual device placement and fallback paths.

Primary references (consult the installed backend/version when applying them):
- [Python clocks](https://docs.python.org/3/library/time.html#time.perf_counter)
- [PyTorch benchmark utilities](https://docs.pytorch.org/docs/stable/benchmark_utils.html)
- [PyTorch CUDA execution](https://docs.pytorch.org/docs/stable/notes/cuda.html#asynchronous-execution)

## Repeats and comparisons

Printed decimal places or rounded raw samples do not establish the clock's
resolution. Check the instrument/source, or mark resolution unknown. With two
samples, descriptive ranges and sample standard deviations can still be
computed; distinguish limited statistical inference from an inability to report
any dispersion. Do not invent a minimum sample count for descriptive statistics.

Use enough bounded repetitions to expose variation; preserve each raw sample.
Define warm-up and outlier handling before examining favorable results. Report
sample counts and dispersion, not just the best run. Where appropriate, use
paired inputs and alternate/randomize method order to reduce drift/order bias.
Keep workloads and included phases comparable across methods.

Do not conflate repeated timings of one dataset with independent scientific
samples. A convergence claim needs refinement checks; a stochastic effect needs
appropriate independent seeds/replicates and uncertainty. Choose domain-specific
tests rather than imposing a universal tolerance or significance threshold.

## Cache, memory, and I/O

Define warm/cold-cache claims and how the state is established. A cache-drop
request is not proof that pages were evicted. Verify residency when a comparison
depends on it, or label the state unverified. Avoid system-wide cache changes
for a local experiment without the required scope.

Distinguish current/peak, allocated/reserved, process/system, and per-rank/global
memory. Reset/read peak counters over the intended interval and identify the
allocator/instrument used. Cumulative I/O/CPU counters generally require
end-minus-start differences. Lazy loading, mmap, zero-copy views, cached files,
compression, and write buffering can change which work actually occurred.
Check the intended path before interpreting an unexpectedly cheap measurement.
