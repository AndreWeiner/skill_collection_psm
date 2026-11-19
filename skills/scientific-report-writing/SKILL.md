---
name: scientific-report-writing
description: Draft, revise, or restructure scientific reports and technical manuscripts. Use for building an argument from supplied evidence, explaining methods and equations, designing explanatory figures and tables, and preparing a readable LaTeX report. For an audit of a finished document, use report-consistency.
---

# Scientific report writing

Write for a knowledgeable reader who has not seen the code, analysis notebook,
or preceding discussion. Inspect the supplied material and current document
before editing. Preserve the author's claims, citation style, and working
document template unless the task calls for a change. Flag evidence gaps
explicitly.

## Build the argument

- Open with the problem and contribution. For a benchmark, state the baseline,
  resource budget, and principal measured result in absolute and relative terms.
- Separate the general method, its implementation, and the application when
  those distinctions matter. Establish the method before describing code
  responsibilities. Put case-specific input values and configurations next to
  the results that depend on them.
- Define each operation when it first matters. Explain its input, output, and
  role in the next step. Use descriptive headings and short connected
  paragraphs. Keep one main thought per sentence. Use informative phrases
  for outline bullets and complete prose for the finished argument.
- Introduce the evidence in the order in which the reader needs it. State what
  the results establish and the limits of that conclusion. Merge overlapping
  passages. Keep useful scientific context and move routine execution details
  into supporting material when appropriate.

## Present methods and evidence

- Define notation at first use, including coordinates, reference scales,
  time levels, and units. Distinguish running indices from descriptive
  subscripts. Give each independent relation its own equation number and
  group a coherent sequence with lettered subequations where useful.
- For an established algorithm, cite its source, present the equations
  together, then explain the dependencies that matter. Refer back to the
  report's own equation labels. Verify any implementation-specific change
  to a model term or time level against the implementation.
- Give each figure a question to answer. Use the caption to identify what is
  shown and the discussion to interpret it. Label panels consistently and
  define scales, encodings, and statistics. Combine common setup values and
  boundary conditions in a compact table. Give tabular values explicit units
  or normalization.
- Distinguish measurements, analytical references, reconstructed quantities,
  and estimates. State the assumptions behind comparisons. For timings,
  identify the measured interval and aggregation, name the baseline, and
  distinguish sequential costs from concurrent work. Read
  [figures and benchmarks](references/figures-and-benchmarks.md) for explanatory
  diagrams, timing breakdowns, or parameter sweeps.

## Verify and deliver

Use the existing LaTeX entry point, engine, and bibliography workflow. For a new
document, choose a layout and build workflow that fit the requested venue and
available tools. Use cross-references and citations instead of fixed numbers.
If the notation warrants a nomenclature, give each populated group a heading.

Use [scientific-visualization](../scientific-visualization/SKILL.md) for
quantitative plots and [report-consistency](../report-consistency/SKILL.md) to
review a substantial draft. If those skills are unavailable, check claims
against the supplied evidence and inspect the rendered figures directly.
Review changed pages at their intended reading size. Check the build log,
equation references, figure labels, centering, and page breaks. Record any
checks that could not be completed. Deliver the editable sources, supporting
figures and bibliography, and the compiled document when requested.
