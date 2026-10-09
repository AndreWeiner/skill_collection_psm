# Environment and building

Inspect `WM_PROJECT`, `WM_PROJECT_VERSION`, `WM_PROJECT_DIR`, `WM_OPTIONS`,
`FOAM_USER_APPBIN`, and `FOAM_USER_LIBBIN`; check the actual `wmake` and utility
paths. Environment variables can be stale, so corroborate the distribution
against the selected source's headers/version information and installed tools.
OpenFOAM.com source normally identifies `www.openfoam.com` and its API release.
Do not rely on historical copyright attribution to identify the distribution.

If activation is needed, source the specific installation's `etc/bashrc` in the
task shell. Avoid changing login/startup files. Do not silently select a release
because it is first on PATH. Record precision and label width where they affect
compatibility or data interpretation.

Inspect `Allwmake`, `Make/files`, `Make/options`, and any existing test runner.
Use `wmake` for an executable and the appropriate library target (commonly
`wmake libso`) for a library, as established by the project. Put extension
binaries/libraries in user or isolated project output directories, never the
installed system tree. Do not replace the established build with CMake merely
to compile a small extension.

Choose includes and linked libraries from inspected APIs and comparable targets;
avoid copying an unrelated solver's entire dependency list. Retain complete
build diagnostics and fix warnings introduced by the change.

Not every `.H` found by a symbol search is a standalone public header. Some
companion/template fragments are included by their owning header and lack
include guards. Follow the caller's public include pattern; directly including
such a fragment again can cause template redeclaration errors.

Verify the exact executable path or loaded library path after building. Run
an isolated test binary by absolute path to avoid accidentally testing an older
installed version. A missing compiler, library, or environment is a validation
limitation; record it without claiming the code compiles.
