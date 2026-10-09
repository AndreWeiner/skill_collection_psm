# Spatial fields and CFD

Identify cell/point association, mesh coordinates, units, reference frame,
instantaneous/averaged state, and slice location/time. State nondimensionalization
and reference quantities where used. Do not imply that interpolated rendering
adds measured or simulated resolution.

Preserve physical geometry and aspect ratio for spatial views. For 3D views,
choose a camera that exposes the relevant structure, use consistent cameras
across comparisons, and explain projection where it affects interpretation.
Label orientation or provide a scale when axes are absent. Avoid perspective
views for quantitative distance comparison when an orthographic view suffices.

Use shared ranges/norms for comparable fields. Diverging quantities require a
meaningful center; symmetric limits are useful for signed departures when
appropriate, not for every variable. Show saturated/out-of-range values and
masked/missing regions explicitly. Colorbars require quantity, units, and
readable ticks. Keep contour levels reproducible across comparisons.

Distinguish vector direction from magnitude. State arrow normalization, scale,
and subsampling; provide a scale key where magnitude is encoded by length.
Streamlines depend on seed placement and are not particle trajectories in a
time-varying field. State seeds or selection rules when they affect the claim.

Dense fields can be rasterized within a vector document. Preserve vector labels
and export at sufficient resolution for the intended placement. For time series
or animations, keep camera, limits, size, and color normalization stable unless
changes are intentional and clearly disclosed.
