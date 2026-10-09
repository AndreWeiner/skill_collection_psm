# Parallel development

Establish whether the utility or library supports decomposed cases. For a
serial-only operation, use the target release's standard parallel exclusion
mechanism and test that rejection, instead of letting ranks run independently.

For supported parallel operation, inspect which helpers already perform global
reductions or communication. Every participating rank must enter collective
operations in a compatible order. Compute collective results before applying
master-only guards to presentation or shared file writing.

Distinguish local labels from global identifiers. Check coupled/processor
boundaries, communication-aware field operations, empty local partitions,
and whether data are duplicated or uniquely owned. Do not replace framework
communication with direct MPI calls without a concrete need and compatibility
analysis.

Define output ownership: one master-written summary, independent per-rank files,
or an established parallel writer. Avoid concurrent writes to the same ordinary
file. Do not gather complete meshes/fields to rank zero for an operation that
can use distributed reductions.

Compare a serial result with at least a two-rank result on the same case. Use
numeric tolerances appropriate to the algorithm, precision, and reduction
ordering, not bitwise equality by default. Exercise an uneven decomposition or
empty local input when those conditions can affect the changed algorithm.

A launcher/socket failure is not proof of a code defect. Preserve its diagnostics
and report that MPI execution was blocked unless it can be rerun in an authorized
environment with local networking. Do not claim tested parallel support based
only on the presence of reduction calls in source.
