#!/usr/bin/env python3
"""Build a static comparison gallery from recorded outputs; no model calls."""
import argparse
import base64
import html
import json
from pathlib import Path
from urllib.parse import quote

RASTER = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
          '.gif': 'image/gif', '.webp': 'image/webp'}
STATUSES = {'completed', 'failed', 'timed_out', 'unavailable'}


def escape(value):
    return html.escape(str(value), quote=True)


def local_file(root, value):
    path = Path(value)
    if path.is_absolute():
        raise ValueError('artifact paths must be relative')
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root) or not resolved.is_file():
        raise ValueError(f'artifact missing or outside comparison directory: {value}')
    return resolved


def build(manifest):
    root = manifest.parent.resolve()
    data = json.loads(manifest.read_text(encoding='utf-8'))
    runs = data.get('runs')
    if not isinstance(runs, list) or not runs:
        raise ValueError('runs must be a nonempty list')
    cards = []
    for run in runs:
        if not run.get('model') or run.get('status') not in STATUSES:
            raise ValueError('each run needs a model and a valid status')
        artifacts = []
        for item in run.get('artifacts', []):
            original = local_file(root, item['path'])
            preview = local_file(root, item['preview']) if item.get('preview') else original
            mime = RASTER.get(preview.suffix.lower())
            if item.get('preview') and not mime:
                raise ValueError('previews must be PNG, JPEG, GIF, or WebP')
            visual = ''
            if mime:
                encoded = base64.b64encode(preview.read_bytes()).decode('ascii')
                visual = f'<img alt="{escape(item.get("label", "Artifact"))}" src="data:{mime};base64,{encoded}">'
            href = quote(original.relative_to(root).as_posix(), safe='/')
            artifacts.append(f'<figure>{visual}<figcaption><a href="{href}">{escape(item.get("label", original.name))}</a></figcaption></figure>')
        cards.append('<article><h2>' + escape(run['model']) + '</h2><p>'
                     + escape(run['status']) + ' · ' + escape(run.get('route', 'unspecified route'))
                     + '</p><p>' + escape(run.get('settings', '')) + '</p>'
                     + ''.join(artifacts) + '<p>' + escape(run.get('summary', '')) + '</p></article>')
    title = escape(data.get('title', 'Model comparison'))
    return f'''<!doctype html>
<html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src data:; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>{title}</title><style>
body{{font:16px system-ui,sans-serif;color:#17212b;background:#f5f7fa;margin:24px}}
main{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:20px}}
article{{background:white;border:1px solid #cdd5df;border-radius:10px;padding:18px;min-width:0}}
h2{{font-size:20px;overflow-wrap:anywhere}} p{{white-space:pre-wrap;overflow-wrap:anywhere}}
figure{{margin:16px 0}} img{{width:100%;height:360px;object-fit:contain;background:#f8f8f8}}
figcaption{{padding:8px 0}} a{{color:#075cab}}
</style><body><h1>{title}</h1><p>{escape(data.get('task', ''))}</p>
<main>{''.join(cards)}</main></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--overwrite', action='store_true')
    args = parser.parse_args()
    try:
        content = build(args.manifest.resolve())
        output = args.manifest.resolve().parent / 'gallery.html'
        with output.open('w' if args.overwrite else 'x', encoding='utf-8') as stream:
            stream.write(content)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f'gallery error: {error}\n')
    print(output)


if __name__ == '__main__':
    main()
