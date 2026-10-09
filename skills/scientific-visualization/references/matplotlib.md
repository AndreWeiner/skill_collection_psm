# Matplotlib implementation

Use the object-oriented API and a local `matplotlib.rc_context` or
`plt.style.context`; do not modify user-wide `matplotlibrc`. The bundled
[scientific.mplstyle](../assets/scientific.mplstyle) is a starting point, not a
complete project contract. Explicitly set sizes in the shared project code:

```python
WIDTH_MM = {"single": 89.0, "double": 180.0}
USE_TEX = True  # Explicit False requires a documented reason.
STYLE = Path(__file__).parent / "scientific.mplstyle"

with plt.style.context(STYLE), mpl.rc_context({"text.usetex": USE_TEX}):
    fig, ax = plt.subplots(figsize=(WIDTH_MM["single"] / 25.4, 65 / 25.4),
                           layout="constrained")
    # Plot actual quantities; label axes, units, and uncertainty semantics.
    fig.savefig("figure.pdf")
    fig.savefig("figure.png", dpi=300)
```

Copy/adapt the asset once into the project or reference a stable maintained path;
do not create a dependency on a temporary evaluation directory. Keep the chosen
widths, heights/presets, palette, renderer, preamble, and export DPI together.
Share colors for the same physical quantity/method across related figures.
Presentation sizes require separate typography; do not enlarge paper figures
and assume their labels are suitable for a projected slide.

Smoke-test the actual backend with representative math and text. Keep the
selected renderer fixed during export; an availability probe must not set
`use_tex` automatically. Expose `--no-tex` or a shared explicit setting for
intentional fallback, and raise a useful error if the chosen renderer fails. `usetex` has
external dependencies that differ by output backend; inspect the traceback rather
than treating every error as a missing executable. The default style uses serif
text compatible with typical LaTeX output; match a supplied manuscript font and
check glyph coverage. TeX strings require escaping literal percent, underscore,
and other special characters. Do not add a large preamble without a reason.

`bbox_inches="tight"` changes the exported page size. Prefer layout adjustment
inside a fixed canvas when exact project widths matter. If cropping is used,
measure the output and ensure manuscript placement does not introduce unequal
text scaling. Raster pixels approximately equal inches times export DPI.
High DPI cannot restore detail absent from the input raster.

Rasterize dense meshes/scatter artists selectively to keep vector files manageable,
while leaving labels and axes vector. Retain physical aspect ratio with
`ax.set_aspect("equal")` for spatial coordinates when appropriate. Check imshow
`origin`, `extent`, interpolation, and cell-versus-point association explicitly.
Use one norm/colorbar for quantitatively comparable fields.

References (consult current installed-version documentation for API details):
- https://matplotlib.org/stable/users/explain/text/usetex.html
- https://matplotlib.org/stable/users/explain/colors/colormaps.html
- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
- https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/
