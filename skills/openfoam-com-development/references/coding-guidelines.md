# Coding guidelines

Verified against the official OpenFOAM.com contribution guide and wiki on
2026-10-09. Distinguish upstream rules from the practical development advice
in the other references. Use the target project's established exceptions and
recheck upstream guidance when proposing an upstream contribution.

## Official sources

- [v2606 contribution guide](https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2606/CONTRIBUTING.md)
- [Coding style](https://gitlab.com/openfoam/core/openfoam/-/wikis/coding/style/style)
- [File naming](https://gitlab.com/openfoam/core/openfoam/-/wikis/coding/style/filenames)
- [Coding patterns](https://gitlab.com/openfoam/core/openfoam/-/wikis/coding/patterns/patterns)
- [Coding scripts](https://gitlab.com/openfoam/core/openfoam/-/wikis/coding/scripts/scripts)
- [Git workflow](https://gitlab.com/openfoam/core/openfoam/-/wikis/coding/git-workflow)

The v2606 guide is an example verified release, not a requirement to develop
only for v2606. Read the chosen release's contribution file when available.

## Practical style checklist

Use four spaces for each indentation level, no tabs or trailing whitespace,
and an 80-character line limit. Follow upstream brace, continuation, declaration,
and documentation conventions by comparing with nearby maintained code.
Document public classes/options and non-obvious numerical assumptions.

Follow the component's file layout and header guards. `.H` and `.C` are
established conventions; the naming guide also discusses `.cxx` and `.txx`.
Do not rename unrelated files or impose one extension on every component.
Preserve existing license/copyright notices when adapting source.
For newly authored files, follow the project's applicable header without
inventing copyright ownership or implying that a local extension was authored
by the upstream vendor or is part of the official release.

## Standard file headers

Include the standard OpenFOAM.com comment banner in newly created C++ source
and header files and standalone case dictionaries. Obtain its layout from the
target installation's `etc/codeTemplates` or a comparable maintained file;
do not substitute another fork's banner or hardcode v2606 into future work.
Retain the normal section dividers and closing file marker where the template
uses them.

For C++ files, use the applicable source/class template with accurate
`Application` or `Class`, `Description`, and relevant usage documentation.
Keep copyright and license text consistent with the project's actual provenance
and applicable license. Adapting upstream code requires preserving its notices;
using the standard banner in an original file does not justify inventing vendor
authorship. The banner is distinct from C++ include guards, which are also needed
for ordinary standalone headers.

For standalone OpenFOAM dictionaries, use the dictionary-style banner followed
by a correct `FoamFile` block, for example:

```text
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      controlDict;
}
```

Set `object` to the actual dictionary name and `location` when required by the
chosen template. `version 2.0` describes the file format, not the OpenFOAM
release. If the banner includes a release version, use the actual target release.
For field files, use their actual class (for example `volScalarField`) and field
name rather than copying `class dictionary` blindly. Included fragments that
must fit inside another dictionary/list should follow that context; do not add
a standalone `FoamFile` block where it would break inclusion semantics.

## Upstream contributions

For upstream commits, consult the contribution guide's tags and formatting
(for example `BUG`, `ENH`, `COMP`, `DOC`, `TUT`, or `STYLE`). Local project
conventions still govern local-only changes. Posting issues, pushing branches,
and opening merge requests require authorization for those actions.
