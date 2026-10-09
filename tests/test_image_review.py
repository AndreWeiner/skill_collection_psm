"""Local request and failure-path checks; never calls the remote API."""
import contextlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('image_review', ROOT / 'skills/image-review/review_images.py')
review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(review)


class ImageReviewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'plot.png'
        self.path.write_bytes(b'\x89PNG\r\n\x1a\nfixture')
        key = patch.dict(os.environ, {'SCADSAI_API_KEY': 'test-placeholder-only'})
        key.start()
        self.addCleanup(key.stop)

    def response(self, content='Reviewed'):
        return io.BytesIO(json.dumps({'choices': [{'message': {'content': content}}]}).encode())

    def test_supported_formats_and_jpeg_normalization(self):
        for extension, signature, mime in [
            ('png', b'\x89PNG\r\n\x1a\n', 'image/png'),
            ('jpg', b'\xff\xd8\xff', 'image/jpeg'),
            ('JPEG', b'\xff\xd8\xff', 'image/jpeg'),
            ('gif', b'GIF89a', 'image/gif'),
            ('webp', b'RIFF0000WEBP', 'image/webp'),
        ]:
            with self.subTest(extension=extension):
                path = self.path.with_suffix('.' + extension)
                path.write_bytes(signature + b'fixture')
                self.assertEqual(review.load_image(path)[0], mime)

    def test_unsupported_pdf(self):
        with self.assertRaisesRegex(review.ReviewError, 'Unsupported'):
            review.load_image(self.path.with_suffix('.pdf'))

    def test_empty_and_wrong_signature(self):
        for data in [b'', b'not an image']:
            self.path.write_bytes(data)
            with self.assertRaisesRegex(review.ReviewError, 'Unrecognized'):
                review.load_image(self.path)

    def test_mislabeled_image(self):
        self.path.write_bytes(b'\xff\xd8\xfffixture')
        with self.assertRaisesRegex(review.ReviewError, 'does not match'):
            review.load_image(self.path)

    def test_missing_file(self):
        with self.assertRaisesRegex(review.ReviewError, 'Cannot read'):
            review.load_image(self.path.with_name('missing.png'))

    def test_missing_or_blank_key_makes_no_request(self):
        for key in ['', '   ']:
            with patch.dict(os.environ, {'SCADSAI_API_KEY': key}), patch.object(review.urllib.request, 'urlopen') as remote:
                with self.assertRaisesRegex(review.ReviewError, 'missing or empty'):
                    review.ask(self.path, 'review')
                remote.assert_not_called()

    def test_request_payload_and_custom_options(self):
        with patch.object(review.urllib.request, 'urlopen', return_value=self.response()) as remote:
            self.assertEqual(review.ask(self.path, 'Check units', model='vision-test', timeout=12), 'Reviewed')
        request = remote.call_args.args[0]
        data = json.loads(request.data)
        self.assertEqual(request.full_url, 'https://llm.scads.ai/v1/chat/completions')
        self.assertEqual(data['model'], 'vision-test')
        self.assertEqual(data['messages'][0]['content'][0]['text'], 'Check units')
        self.assertTrue(data['messages'][0]['content'][1]['image_url']['url'].startswith('data:image/png;base64,'))
        self.assertEqual(remote.call_args.kwargs['timeout'], 12)

    def test_remote_failures_do_not_expose_error_body(self):
        for error, expected in [
            (urllib.error.HTTPError('https://example.invalid', 401, 'sensitive-body', {}, None), 'HTTP 401'),
            (urllib.error.URLError('sensitive-body'), 'connection failed'),
            (TimeoutError('sensitive-body'), 'timed out'),
        ]:
            with patch.object(review.urllib.request, 'urlopen', side_effect=error):
                with self.assertRaises(review.ReviewError) as caught:
                    review.ask(self.path, 'review')
                self.assertIn(expected, str(caught.exception))
                self.assertNotIn('sensitive-body', str(caught.exception))

    def test_bad_json(self):
        with patch.object(review.urllib.request, 'urlopen', return_value=io.BytesIO(b'not JSON')):
            with self.assertRaisesRegex(review.ReviewError, 'invalid JSON'):
                review.ask(self.path, 'review')

    def test_missing_or_empty_review_text(self):
        for result in [{}, {'choices': []}, {'choices': [{'message': {'content': None}}]}, {'choices': [{'message': {'content': '  '}}]}]:
            with patch.object(review.urllib.request, 'urlopen', return_value=io.BytesIO(json.dumps(result).encode())):
                with self.assertRaisesRegex(review.ReviewError, 'no review text'):
                    review.ask(self.path, 'review')

    def test_all_inputs_checked_before_upload(self):
        with patch.object(review.urllib.request, 'urlopen') as remote, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(review.main([str(self.path), str(self.path.with_name('missing.png'))]), 1)
            remote.assert_not_called()

    def test_cli_multiple_images(self):
        out = io.StringIO()
        with patch.object(review.urllib.request, 'urlopen', side_effect=[self.response('First'), self.response('Second')]) as remote, contextlib.redirect_stdout(out):
            self.assertEqual(review.main([str(self.path), str(self.path)]), 0)
            self.assertEqual(remote.call_count, 2)
        self.assertIn('First', out.getvalue())
        self.assertIn('Second', out.getvalue())

    def test_partial_failure_preserves_success_and_stops(self):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(review.urllib.request, 'urlopen', side_effect=[self.response('First'), TimeoutError()]) as remote, contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(review.main([str(self.path)] * 3), 1)
            self.assertEqual(remote.call_count, 2)
        self.assertIn('First', out.getvalue())
        self.assertIn('not reviewed', err.getvalue())

    def test_timeout_rejects_nonfinite_zero_negative(self):
        for value in ['nan', 'inf', '0', '-1', 'nonsense']:
            with self.subTest(value=value), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                review.main([str(self.path), '--timeout', value])
            self.assertEqual(caught.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
