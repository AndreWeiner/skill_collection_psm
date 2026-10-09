# Validation

Choose checks that exercise the changed behavior. Prefer existing project tests
and a tiny deterministic case to a full production simulation. Preserve user
cases and write generated meshes, fields, logs, and binaries into isolated paths.
Do not run cleanup commands against a production case.

For a field-processing utility, use a field with analytically known statistics
or integrals; include nonuniform cell volumes when weighting matters. Compare
actual output to expected values with an explicit tolerance. Check output units
and dimensions, not just a process exit code or the presence of a file.

Test relevant command-line and field errors: missing mandatory options, invalid
values, absent/wrong-type fields, zero denominators, or unsupported parallel
execution. Require actionable errors and a failing exit status. Do not add a
generic edge-case matrix unrelated to the task.

For parallel support, test the same numerical quantity in serial and with
multiple ranks. Inspect output ownership and the number of summary records.
For libraries/function objects, actually load the built library and invoke the
changed behavior; building an unrelated executable does not exercise it.

Report the selected release/build settings, commands, expected and actual
results, and incomplete checks. Keep source inspection, build, runtime, and
cross-release compatibility claims separate. Broaden testing when a failure
or new change warrants it, not merely to accumulate successful checks.

For affected persistent state/output, test continuous versus checkpointed/restarted
execution, repeated invocation, and incomplete-state handling. For resource-impact
changes, estimate peak-memory growth and check representative sizes/repeated calls;
measure scaling only when it is relevant and resources permit. State untested
restart, failure, memory or scaling behavior explicitly.

When evaluating this skill itself, give the agent a realistic requirement and
raw fixtures rather than a prescribed implementation. Check whether it searched
for and reused appropriate OpenFOAM facilities, respected the distribution and
output scope, compiled and ran the code, and verified meaningful results.
