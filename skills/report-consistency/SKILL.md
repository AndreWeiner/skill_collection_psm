---
name: report-consistency
description: Review completed or substantially revised reports, papers, thesis chapters, READMEs, and other documents for internal consistency before delivery, or when explicitly asked to audit a document. Check numbers, references, terminology, claims, and figures; minor ongoing wording edits do not require a full review.
---

# Report consistency check

Review the supplied document and relevant source data. Keep the review read-only
unless the user also requests fixes. Identify the document root, included files,
and applicable project conventions before checking individual sections.

## Numbers and evidence

Compare numerical claims with their tables, figures, and supplied source data.
Recompute derived quantities such as speedups, percentages, means, and totals;
check units and rounding. Cite the conflicting values and their locations.
If the supporting data are missing, label the claim unverified rather than
inventing a source or declaring the number wrong.

## References and build

For LaTeX, use the project's documented build command, root document, engine,
and bibliography workflow. If none is documented, inspect the source before
choosing a suitable available compiler; allow the passes needed to resolve
references and citations. Use a temporary output directory where practical.
Check the final log for unresolved or multiply defined references and citations.
Compilation success alone does not establish numerical or visual correctness.
If tools, bibliography files, or dependencies are unavailable, report which
checks remain incomplete. Do not download or install dependencies just to review.

For Markdown, check local link targets and heading anchors against the intended
renderer when known. Distinguish broken links from links outside the available
workspace. Report untested external URLs as unchecked, not broken.

Check that references point to the intended material. Flag missing references
when the document relies on them; do not treat every unused label, bibliography
entry, standalone illustration, or intentionally unreferenced item as an error.

## Terminology, claims, and figures

Check consistent notation, units, abbreviation definitions, and terminology.
Flag differences that change meaning or create ambiguity; valid synonyms are
not automatically inconsistencies.

Check that conclusions and summary claims are supported by the body and that
captions describe the actual figures. Inspect rendered pages or image files
directly when the current agent can view them. Otherwise use `image-review`
if available and appropriate for the supplied images. If neither route works,
state that visual checks were not performed. Increase rendering resolution
when text or labels are unreadable. Verify precise values against data rather
than estimating them from pixels.

Check for unintended draft markers and unfinished passages in prose, while
allowing deliberate examples of TODOs or similar markers in code/documentation.

## Findings and completion

Report actionable findings as:

`file:line (or page/section) — issue — severity — evidence`

- **blocker:** the required deliverable cannot be produced or a central result
  is invalidated.
- **major:** a substantive numerical, reference, or meaning error affects an
  interpretation or conclusion.
- **minor:** a local clarity or presentation problem does not affect results.

Separate confirmed findings from incomplete checks and uncertain concerns.
Missing access or an unavailable tool is a validation limitation, not proof of
a defect in the document. Finish with what was actually checked and what remains
unverified. When no confirmed errors are found, state that with the same limits.
