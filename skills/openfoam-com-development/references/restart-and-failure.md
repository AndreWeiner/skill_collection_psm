# Restart, interruption, and repeated execution

Assess the behavior affected by the change; document genuinely inapplicable
items briefly instead of building generic recovery machinery.

For accumulated statistics, history-dependent models, function objects and
other stateful extensions, identify persistent state versus reconstructible
caches. Check the target release's existing read/write and restart mechanisms
before implementing a new format. Specify required metadata, version/shape and
mesh/decomposition compatibility, and behavior for missing or incompatible state.

Test a continuous short run against a split run restarted from a valid written
time/checkpoint, comparing state and outputs with appropriate tolerances. Use
only information persisted at that checkpoint. Do not compare a checkpointed
prefix to later unpersisted state as if it should be recoverable. Check changed
rank counts/mesh topology only when that compatibility is claimed.

Define append, overwrite, duplicate-record and repeated-processing behavior.
Restarting a function object must not silently count the same samples twice or
reset a required accumulator. Re-running a utility should preserve inputs and
handle existing output predictably. Invalidate geometry/addressing caches when
the relevant mesh/state changes; check long-run state/buffer growth.

For persistent writes, distinguish complete output from a partially written
file/time directory. Reuse framework mechanisms; when a new format is necessary,
choose an appropriate completion/commit strategy and validation. Do not imply
that flushing a stream guarantees crash durability, or that a rename gives a
multi-rank/multi-file transaction by itself.

Use a tiny isolated interruption/corrupt-state test when relevant: partial or
truncated output, a missing shard, or a process failure during a write. Require
clear diagnostics and explicit rejection or documented recovery; preserve the
last valid state and avoid treating partial output as a completed result.
Account for one-rank failure/collectives when parallel support is affected.

Report which crash/interruption scenarios were actually tested. A clean restart
test does not prove recovery after arbitrary crashes or power loss. Keep user
production cases and checkpoints untouched during these tests.
