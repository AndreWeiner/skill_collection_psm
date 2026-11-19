# Figures and benchmarks

## Explanatory figures

Use an illustrative diagram to introduce a general method. Show actual inputs
and decompositions in a case figure. If both are needed, identify each clearly.
For an algorithm diagram, show time direction, stage boundaries, and the
dependency that releases the next operation. Use separate lanes for concurrent
work. Check that every arrow reaches its intended endpoint and that all legend
entries occur in the artwork.

Use symbol-based axis labels when the notation is unambiguous. Give dimensional
quantities units and define every normalization used. Put panel letters near the
upper-left corner of each panel and map them in a caption that starts with a
short title. An inset belongs to its parent panel. Keep its data and scale
definitions consistent with the overview. Give each legend clear ownership and
space outside the plotted data.

Check the visible artwork, not just its bounding box. Center the content, trim
unused margins, and preserve enough room for labels. As a starting point for a
technical report with 12 pt text, use figure labels near 10 pt at final placement
size. Follow the venue and figure style when they prescribe different sizes.
Keep table typography consistent. Inspect the rendered page after resizing.

## Timing and parameter comparisons

State whether each performance quantity is wall time, a rank-specific timer,
a mean, a range, or a critical-path measurement. Identify the measurement
window, aggregation over ranks and stages, and independent repetitions when
available. Keep implementation identifiers when they are needed to interpret a
measurement. Keep raw logs alongside the reproducible inputs and scripts.

Use a comparison baseline that fits the question. For a within-method
breakdown, divide disjoint sequential intervals by their common parent
measured over the same samples. A complete breakdown sums to one. Show nested
components separately with their own parent denominator. For comparing
implementations, give absolute wall time and, if useful, normalize by a named
shared baseline. Fractions and seconds per step have distinct meanings.

Concurrent durations may overlap the main work path. Avoid summing them into
the same bar or adding independent rank maxima to construct a timestep. Define
the endpoints of the compared windows. When traces permit, pair each producer
interval with the corresponding consumer interval for the same request and
stage. A global worker maximum and a fluid-rank mean characterize different
populations. Local durations alone cannot establish cross-rank overlap. State
clock-alignment assumptions when using cross-rank timestamps.

Distinguish result readiness, communication, installation, and exposed waiting
when the evidence supports the split. Waiting can appear in a later
synchronization timer. Attribute it to an earlier operation only when the trace
supports the dependency.

Report allocated resources and active ranks or threads when they differ. Match
the resource budget, execution conditions, and numerical work when attributing
a speedup to a method. Report the absolute difference and the percentage
reduction relative to the same baseline. Highlight the fastest tested
configuration in a sweep. If repeated measurements overlap, report the
observed variability and scope the optimum to the configurations tested.
