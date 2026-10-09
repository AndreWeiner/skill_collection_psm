# Interfaces, persistence and documentation

Extend existing interfaces consistently. Make defaults, units, shapes, ownership,
mutability, device placement, failure behavior and compatibility explicit.
Document non-obvious scientific assumptions, not every routine line of code.
Use project file headers/license notices; preserve attribution when adapting
source and do not invent ownership for new files.

For persistent state, identify what must be stored and what can be recomputed.
Reuse established serialization/checkpoint facilities. Record relevant schema,
shape, numerical settings and input identity, and reject incompatible state
clearly. Define cache invalidation, bounded state growth, and compatibility with
changed datasets, meshes, worker counts or software only where promised.

Specify append/overwrite/idempotence and duplicate-processing behavior. A restart
or retried call must not silently double-count work or reinterpret partial output
as complete. For multi-file/rank outputs, define completeness explicitly; a single
rename or successful rank does not prove the whole checkpoint is committed.
Choose failure-safe writing appropriate to the actual filesystem/application
and avoid unsupported crash-durability guarantees.

Test incomplete/corrupt state or interruption on tiny disposable fixtures when
the change affects recovery. Preserve the last valid data and distinguish missing
required state from reconstructible caches. Report unsupported restart/failure
scenarios instead of adding generic recovery machinery outside task scope.
