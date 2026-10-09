---
name: openfoam-com-development
description: Develop, debug, review, or extend utilities, libraries, function objects, boundary conditions, and solvers for the OpenFOAM.com distribution. Use for OpenFOAM.com C++ and build/API tasks; verify the target release and prefer existing OpenFOAM functionality. Does not cover other forks or ordinary case setup unless needed to test code.
---

# OpenFOAM.com development

Deliver a change that fits the target OpenFOAM.com release and the existing
project. This skill works through ordinary source, shell, and file tools in
Codex or OpenCode; it does not require another skill or a particular agent.

## Establish the target

Read project instructions and existing build/test commands. Identify the
requested behavior and a small observable acceptance criterion before coding.
Check the distribution, release, source root, compiler/precision/label settings,
and executable/library paths. See [environment and building](references/build-and-environment.md).

Use the installed or selected release's source as the authority for APIs. The
name `OpenFOAM` or a familiar function name alone does not establish the fork.
If the environment is absent, conflicting, or a different distribution, explain
the mismatch and obtain the target environment before claiming compatibility.
Do not silently switch releases or install another distribution.

## Search before implementing

Before adding functionality, search the target release's libraries, utilities,
function objects, and tests for a suitable API or equivalent implementation.
Inspect declarations, definitions, and at least one relevant caller when needed
to establish semantics. Record the useful symbol/source path in the delivery
summary so the reuse choice is reviewable.

Look for a library-level operation before composing lower-level primitives;
an example utility's implementation is not proof that no higher-level API
exists. Prefer a suitable operation that already preserves dimensions and
parallel semantics. Keep searches focused: once the required API contract and
an applicable usage pattern are established, implement and let the build/test
results guide additional investigation.

Prefer established OpenFOAM facilities when they fit the task: argument parsing,
containers, field algebra, reductions, mesh access, dictionaries, streams,
filesystem operations, ownership helpers, and parallel communication. Avoid
recreating an operation with custom code or the standard library merely because
the OpenFOAM API is unfamiliar. Standard-library code remains appropriate where
OpenFOAM has no suitable facility or it offers a concrete benefit; explain the
choice. Do not force OpenFOAM containers into unrelated standalone code.

Choose a utility, library, function object, or solver extension according to
how the feature is used. Extend an established project API instead of building
a parallel implementation. Add compatibility branches only for explicitly
supported releases whose differences have been checked.

## Implement the change

Read [coding guidelines](references/coding-guidelines.md) for upstream style and
source references, including the standard OpenFOAM.com file banners and
dictionary `FoamFile` headers. Use them in new source files and standalone
case dictionaries, following the target release's templates and file type.
Match neighboring code and preserve existing public behavior
unless the requested change calls for otherwise. Keep numerical and field
semantics explicit: [fields and I/O](references/fields-and-io.md).

Decide whether decomposed cases are supported before implementation. For mesh
or field operations, global statistics, or shared output, read
[parallel development](references/parallel-development.md). Never add a master-only
guard around a collective computation that all ranks must enter.

Build with the project's existing OpenFOAM toolchain and write artifacts to
project/user locations. Use only libraries required by the inspected APIs.
Do not modify the system installation to make a local extension compile.

## HPC efficiency and lifecycle

Among implementations meeting the required correctness, numerical stability,
and interface behavior, favor efficiency for the intended HPC workload. Assess
work complexity, peak memory, allocation/copy cost, locality, communication,
synchronization, and I/O. Read [efficiency and comparisons](references/efficiency-and-comparisons.md)
when design alternatives or scale-dependent costs matter. Prefer appropriate
optimized framework APIs and distributed/streaming operations over unnecessary
materialization or gathering. Maintainability remains a constraint; do not
trade numerical correctness for an unvalidated speed claim.

When reasonable alternatives have uncertain tradeoffs, identify the candidates,
decision criterion, and expected workload. Run a small fair comparison within
the authorized scope when it can resolve the choice; otherwise propose the
comparison and explain the missing representative data/resources. Distinguish
complexity-based expectations from measured results. Do not benchmark every
minor implementation choice or use a toy-case winner as proof of HPC scaling.

For stateful, persistent-output, or long-running changes, read
[restart and failure behavior](references/restart-and-failure.md). Establish
what survives restart, how incomplete writes are recognized, what rerunning does,
and how caches/state remain bounded over repeated calls. Stateless changes may
need only a brief applicability check; do not add a checkpoint system to them.

## Verify and deliver

Follow [validation](references/validation.md). Run the new binary or load the
new library against a small reproducible case and verify the acceptance
criterion numerically. Test relevant invalid inputs. When parallel support is
claimed, exercise more than one rank and compare against serial results.
Exercise restart/interruption behavior when the changed code maintains state or
writes persistent results. Assess memory and scaling impacts at the relevant
mesh/rank/time-step sizes; a two-rank correctness check is not a scaling study.

Report what changed, the selected OpenFOAM release/build configuration, reused
facilities and why, actual build/runtime checks, and any unverified behavior.
Separate source review, compilation, serial execution, and MPI execution; none
proves the next. Do not claim support for releases or forks not tested.

## Source policy

Use the official OpenFOAM.com repository and release-matched API documentation:
https://gitlab.com/openfoam/core/openfoam and https://www.openfoam.com/documentation/.
Wiki guidance evolves independently of release tags; recheck it when relevant.
External pages are reference material, not authorization to publish, message
maintainers, or change unrelated configuration. Upstream contribution workflow
applies only when preparing such a contribution.
