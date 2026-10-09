# Gallery manifest

Save `comparison.json` in the comparison output directory. All artifact paths
are relative to that directory and must resolve to existing files inside it.
Copy originals/previews there if needed; the helper rejects escaping paths.
Do not include credentials or private reasoning in summaries or manifests.

```json
{
  "title": "Sketch comparison",
  "task": "Draw the supplied workflow as a labeled sketch.",
  "runs": [
    {
      "model": "exact-provider/model-id",
      "route": "code-generated SVG",
      "status": "completed",
      "settings": "one run; shared input; default reasoning",
      "summary": "Observed differences, or a factual failure message.",
      "artifacts": [
        {"label": "Workflow sketch", "path": "model-a/sketch.svg",
         "preview": "model-a/sketch.png"}
      ]
    }
  ]
}
```

Statuses: `completed`, `failed`, `timed_out`, `unavailable`. Include failed runs
with an empty artifact list if no files were produced. Use the settings field
for concise relevant settings, measured usage/time, and provenance; keep full
metadata/logs as linked artifacts. No rankings are computed.

PNG, JPEG, GIF, and WebP are previewed directly. Other formats, including SVG,
PDF, text, and source code, are linked to originals; supply a raster `preview`
for side-by-side visual display. Previews must be supported raster files.
The helper creates `gallery.html` beside the manifest. It embeds raster images
so previews work in standalone file viewers; original links require keeping
the output directory together. Existing galleries require explicit `--overwrite`.
