# Gate record

Before a substantial run, save a JSON record in the run directory with:

- `schema_version`: `1`.
- `checks`: entries for `correctness`, `measurement`, `execution_path`,
  `artifact_integrity`, and `resource_estimate`. Each has `status` (`pass`,
  `fail`, or `unverified`) and `evidence`, a path to the actual check record.
- `fingerprints`: mapping of relative file paths to SHA-256 values. Include
  the relevant executed code, input/configuration or generation recipe, and
  every referenced evidence file. Include transitive code/config dependencies
  that affect this experiment; hashing only a launcher can miss changed modules.
- `proposed_run`: `estimated_seconds` and `budget_seconds`, positive finite numbers
  reflecting the authorized run scope. The estimate must include the intended
  number of trials and phases, not just one timing sample. Record additional
  memory/disk/GPU/job limits in the resource evidence when they matter.

Paths are relative to the gate file's directory. Evidence must describe the
observed check, method, expected/actual results, and relevant limitations, not
just repeat the word "pass". A gate can have additional contextual fields.

Run with Python 3, resolving the helper relative to the discovered skill folder:

```bash
python3 "$SKILL_DIR/scripts/check_gate.py" /absolute/run/path/gate.json
```

The checker exits nonzero for a failed/unverified required check, missing or
modified evidence/input/code, an invalid record, or an over-budget estimate.
It does not dispatch jobs, change records, prove scientific correctness, or
detect an omitted dependency automatically. The agent must inspect the evidence
before recording a pass. If relevant files change, revalidate affected checks
and record fresh fingerprints; do not blindly copy old passes into a new gate.
