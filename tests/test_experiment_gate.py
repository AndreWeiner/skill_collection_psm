"""Exercise acceptance and rejection of actual saved experiment gates."""
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/numerical-experiments/scripts/check_gate.py'
spec = importlib.util.spec_from_file_location('experiment_gate', SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'code.py').write_text('result = 3\n')
        (self.root / 'input.json').write_text('{"values": [1, 4], "weights": [1, 2]}\n')
        (self.root / 'evidence.json').write_text('{"expected": 3, "actual": 3, "pilot_seconds": 0.01}\n')
        self.record = {
            'schema_version': 1,
            'checks': {n: {'status': 'pass', 'evidence': 'evidence.json'} for n in gate.REQUIRED},
            'fingerprints': {n: hashlib.sha256((self.root / n).read_bytes()).hexdigest() for n in ['code.py', 'input.json', 'evidence.json']},
            'proposed_run': {'estimated_seconds': 2, 'budget_seconds': 5},
        }
        self.path = self.root / 'gate.json'
        self.save()

    def save(self):
        self.path.write_text(json.dumps(self.record))

    def test_valid_record_cli_passes_without_mutation(self):
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        r = subprocess.run([sys.executable, str(SCRIPT), str(self.path)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_required_checks_must_pass(self):
        original = copy.deepcopy(self.record)
        for n in gate.REQUIRED:
            for status in ['fail', 'unverified', 'PASS', None]:
                with self.subTest(check=n, status=status):
                    self.record = copy.deepcopy(original)
                    self.record['checks'][n]['status'] = status
                    self.save()
                    self.assertFalse(gate.check(self.path)[0])

    def test_stale_code_inputs_or_evidence_block(self):
        for filename in ['code.py', 'input.json', 'evidence.json']:
            p = self.root / filename
            old = p.read_bytes()
            p.write_bytes(old + b' ')
            with self.subTest(filename=filename):
                self.assertFalse(gate.check(self.path)[0])
            p.write_bytes(old)

    def test_missing_artifact_blocks(self):
        (self.root / 'evidence.json').unlink()
        self.assertFalse(gate.check(self.path)[0])

    def test_unfingerprinted_evidence_blocks(self):
        del self.record['fingerprints']['evidence.json']
        self.save()
        self.assertFalse(gate.check(self.path)[0])

    def test_budget_constraints_and_nonfinite_values(self):
        for estimate, budget in [(6, 5), (-1, 5), (0, 5), (2, 0), (True, 5), (2, False), (float('nan'), 5), (2, float('inf'))]:
            with self.subTest(estimate=estimate, budget=budget):
                self.record['proposed_run'] = {'estimated_seconds': estimate, 'budget_seconds': budget}
                self.save()
                self.assertFalse(gate.check(self.path)[0])

    def test_malformed_record_cli_fails_cleanly(self):
        for value in [[], {}, {'schema_version': True}, {'schema_version': 1, 'checks': [], 'fingerprints': {}}]:
            self.path.write_text(json.dumps(value))
            r = subprocess.run([sys.executable, str(SCRIPT), str(self.path)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 1)
            self.assertNotIn('Traceback', r.stderr)

    def test_invalid_hash_and_absolute_path_block(self):
        self.record['fingerprints']['code.py'] = 'not-a-sha256'
        self.save()
        self.assertFalse(gate.check(self.path)[0])
        del self.record['fingerprints']['code.py']
        self.record['fingerprints'][str(self.root / 'input.json')] = hashlib.sha256((self.root / 'input.json').read_bytes()).hexdigest()
        self.save()
        self.assertFalse(gate.check(self.path)[0])


if __name__ == '__main__':
    unittest.main()
