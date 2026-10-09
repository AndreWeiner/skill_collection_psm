# Fields and I/O

Use release-matched examples for `argList`, time selection, region selection,
`Time`, mesh creation, and `IOobject`. Do not invent option spellings, constructor
signatures, or dictionary methods from another fork or release.

Specify whether data belong to cells, faces, points, patches, or an internal
field. Retain physical dimensions through field operations and reductions;
extract plain numerical values only at an intentional output/API boundary.
Test missing fields, unexpected field types, or dimension mismatches when they
affect the new behavior. Distinguish dimensional compatibility from physical
validity, such as a zero normalization denominator.

Use OpenFOAM field algebra and established integration/statistics operations
when available. Check whether an API integrates local entries or globally
reduces them and whether it includes patch contributions. A volume-weighted
mean is not generally the arithmetic mean of cells.

Use framework ownership (`tmp`, `autoPtr`, references) according to the inspected
API. Keep owners alive while references are used, and avoid references into
cleared temporaries. Avoid full copies of large fields/meshes without a reason.

Choose read/write and registration behavior intentionally. Do not overwrite
inputs merely to inspect them. Use OpenFOAM streams and filesystem facilities
for OpenFOAM objects instead of rebuilding their formats manually. Error messages
should identify the relevant option, field, or dictionary entry.

Document defaults, units, input requirements, output format, time/region behavior,
and restart/append behavior when applicable. Moving or changing meshes require
checking when geometry, addressing, or cached weights become invalid; do not
add that machinery to a static-mesh task without a requirement.
