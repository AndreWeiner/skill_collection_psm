# Testing and validation

Use the project's tests and the changed entry point, not an unrelated example.
Design the smallest checks that discriminate correct from plausible incorrect
behavior. Use independent references/invariants with explicit tolerances and
verify that fixtures actually exercise the relevant branch, data shape, dtype
and backend. Do not write tests that merely echo implementation details.

Test relevant invalid/degenerate inputs and useful errors, without imposing
an exhaustive matrix on every small edit. For stochastic work, record seeds
and choose tests appropriate to distributions; reproducibility does not imply
bitwise determinism across hardware/versions or parallel reduction order.

For stateful/persistent changes, compare uninterrupted and checkpoint/restarted
execution, repeated calls, duplicate input/retry behavior and incomplete-state
handling where applicable. Compare to the state actually persisted, not later
uncheckpointed work. For memory-sensitive changes, inspect allocation complexity
and test repeated-use growth or a representative-size peak with suitable tools.

For performance choices, verify correctness before a small fair comparison.
Validate timing definitions and wait for completion. Report raw samples and
variation; do not infer scalability from a two-worker correctness check.
Use the numerical-experiments workflow for substantial measurements if available.

Preserve raw evidence and distinguish generation, build, unit/integration,
numerical, restart, resource and distributed tests. Record unavailable checks
as limitations rather than passed tests. Broaden validation only when scope,
a change or a demonstrated failure warrants it.
