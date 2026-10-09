# Reproducibility and recovery

Keep a lightweight machine-readable run record rather than building an
orchestration framework for a small experiment. Record what affects the claim:
run ID/time, commands/arguments, resolved configuration, code revision and dirty
changes or content hashes, actual import/binary path, input identity/hash or
deterministic generation recipe, seeds, relevant dependency/compiler versions,
hardware/backend, dtype, thread/rank counts, and measurement definitions/units.
Record actual/effective settings separately from requested ones when they differ.
Do not dump credentials or the complete process environment into provenance.

A matching hash establishes file identity, not numerical correctness or timing
validity. If raw records lack their measurement harness/provenance, aggregation
can be checked while the underlying measurement methodology remains unverified.

Use unique run directories and explicit trial IDs. Save raw samples, errors,
logs, and the exact analysis code/configuration needed to reproduce the report.
Keep large data in established storage with a verifiable identity; copying every
input into each run is unnecessary. Hash relevant files, not unrelated projects
or secrets. Seed reproducible generators, but do not claim that a seed guarantees
bitwise determinism across hardware, parallel reductions, or library versions.

Before extending a sweep, verify that completed trials match the current code,
inputs, configuration, and measurement definition. Resume only those compatible
records. Preserve failed attempts and use separate retry IDs; bound retries and
state their reason. Capture failures promptly and use the smallest diagnostic
reproduction instead of repeating a long failing workload.

Classify a correction by its dependency boundary:

- **Presentation/aggregation:** if raw values and metadata are sufficient and
  still valid, correct the analysis and regenerate derived outputs only.
- **One trial/configuration:** invalidate and rerun that subset after a new pilot.
- **Algorithm, data, timing, or backend:** invalidate the affected measurements;
  prove the repaired path on a small instance before repeating them.

Do not relabel CPU results as GPU, rescale an interval to compensate for missing
work, or repair a missing measurement by inventing data. If a pure unit conversion
is justified by raw metadata, record the conversion and retain the raw record.
Code-hash changes require reviewing impact; a comment-only change does not by
itself require recomputing valid numerical data.
