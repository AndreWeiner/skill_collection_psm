---
name: scientific-visualization
description: Create, improve, or review scientific plots and spatial-field figures for papers, reports, and presentations. Use for readable typography, project-wide sizing, LaTeX rendering, accurate visual encodings, and verified exports, including Matplotlib and CFD figures. Does not validate the underlying numerical experiment or generate illustrative artwork.
---

# Scientific visualization

Produce scientifically faithful figures that remain readable at their intended
placement size. This skill works in Codex and OpenCode through ordinary plotting,
file, and image-inspection tools. Respect the user's plotting software and
publication requirements; no single journal style is a universal standard.

## Establish a project figure contract

Inspect existing plotting code, styles, manuscript dimensions, and project
instructions. Identify the quantities, units, figure purpose, target medium,
and intended physical placement size. Reuse a suitable existing project style.
If none exists, establish one shared, editable configuration for figure widths,
font sizes, strokes, colors, rendering, and export settings, and reuse it across
scripts. Avoid independent style definitions for every figure.

Use a small set of named sizes: typically single-column and double-column for
papers, with a separate presentation preset when needed. Figures in one preset
must share physical width and typography; use a common height where appropriate,
but adapt height to panel count or geometry. Record explicit size/style exceptions
and their reason. Do not force spatial fields into an aspect ratio that distorts
geometry. A different width preset can use the same point-size typography.

Design at final placement size: resizing the exported figure also resizes its
text and strokes. Equal source font sizes do not guarantee equal apparent sizes
when placement scales differ. Verify exported dimensions as well as configured
sizes, especially after automatic cropping. Use target journal specifications
when supplied; otherwise treat 89/180 mm widths, 9–11 pt text, 1.2–1.8 pt main
curves, and 0.7–1.0 pt axes as adaptable starting points, not acceptance thresholds.

## Render text consistently

Prefer LaTeX rendering by default in tools that support it. In Matplotlib set
`text.usetex=True` explicitly, with shared font configuration and a minimal
preamble; match the manuscript when available. Test an actual representative
export containing math, labels, and the intended font before producing the set.
Finding a `latex` executable is not enough: backend tools and packages may fail.

Do not derive the final renderer from an availability probe or automatically
retry with mathtext after a failed export. Keep `use_tex=True` as the default
and provide a named opt-out such as `--no-tex` or an explicit configuration
setting. A failed LaTeX smoke test should produce an actionable error until
that opt-out is explicitly selected.

Disabling LaTeX must be an explicit project or invocation option, with a reason
such as user preference, performance, or an unavailable dependency. If the smoke
export fails, report the cause and record any fallback as `use_tex=False` with
its reason; never silently catch an error and switch rendering. Do not install
system packages or change global fonts to make a local plot work. Keep fallback
fonts/math consistent and disclose which renderer produced the final figures.
For Matplotlib read [the implementation guidance](references/matplotlib.md).

## Encode the science accurately

Check plotted shapes, quantities, units, coordinate conventions, normalization,
and transformations against the supplied data. Label axes and colorbars with
quantities and units (or state dimensionless quantities). Legends/direct labels
must identify compared series; panel labels must be unambiguous.

Distinguish observations, models, and reference values. Define uncertainty bands
or error bars and sample counts when relevant; do not invent uncertainty. Preserve
missing/failed observations explicitly and avoid connecting curves across gaps.
Disclose smoothing, interpolation, binning, decimation, clipping, and aggregation
when they affect interpretation. Retain raw inputs; a visual cleanup is not
permission to rerun an experiment or alter data.

Choose scales and limits that answer the question without concealing important
behavior. Bars normally require a zero baseline; line/scatter axes need not.
Mark log scales and handle nonpositive values explicitly. Use common axes and
normalization across comparable panels, or explain a deliberate exception.
Choose sequential maps for ordered magnitudes, diverging maps around a meaningful
reference, and cyclic maps for periodic variables. Prefer perceptually uniform,
color-vision-accessible choices; avoid rainbow defaults for scalar magnitude.
Distinguish series with markers/styles as well as color when useful. Use
restrained gridlines and sufficient contrast. Do not add decorative 3D effects.
For geometry, contours, vectors, and CFD read [spatial fields](references/spatial-fields.md).

## Export and inspect the actual deliverables

Prefer PDF/SVG for suitable vector plots and PNG/TIFF or mixed vector/raster
exports for dense fields. Start raster exports at 300 DPI at final size; honor
higher resolution requirements when relevant. DPI affects raster content, not
vector strokes or the point size of text. Preserve editable text where practical;
LaTeX/backend font limitations should be stated rather than hidden.

Render and inspect the actual exports at intended size and in a larger detail
view. Check the available review capability: a file-reading tool returning an
image does not establish that the selected model can understand it. Prefer
direct image inspection; when that is unavailable, use a compatible `image-review`
skill or vision tool if installed and transmitting the figures is within the
user-authorized scope. Supply the expected quantities, units, legends, and
placement size. Treat the reviewer findings as evidence to verify, not automatic
approval; vision review can miss defects and cannot establish numerical fidelity.
Re-export and re-review affected figures after concrete repairs. Stop after two
unproductive review/repair cycles and report unresolved issues. Check clipping, overlaps, label completeness, contrast, curve distinction,
font substitution, uncertainty visibility, colorbars, and panel spacing. Verify
physical dimensions, raster pixel dimensions, and representative numerical
values independently of the plotting script's own claims. Repair visible problems
and re-export the affected figures. If image viewing is unavailable, state that
visual QA remains unverified; successful execution is not visual approval.
Keep QA proportional: use an available viewer and ordinary export/data checks.
Do not build a bespoke pixel-recognition system to substitute for visual review.
When viewing is unavailable, finish the useful checks, disclose that limitation,
and deliver the artifacts; do not repeatedly repair a speculative QA detector.

Verify the reproduction command in an isolated copy with no pre-existing output
directory; create required directories before smoke tests or exports. Check an
explicit rendering opt-out when one is provided.

Deliver final figures, reusable plotting code/configuration, input references,
and a reproduction command. State rendering mode, placement size, justified
exceptions, and checks actually performed. Keep claims proportional: attractive
figures do not validate the underlying computation or statistical conclusions.
