# CLAUDE.md

@AGENTS.md

## Claude Code Execution Notes
- **Updating an existing tool** (*"Does `<tool>` need an update?"*): Check upstream, and if a newer stable version exists, execute the full pipeline end-to-end (`adding-<tool>-<new_version>` branch -> scaffold & bump -> build `builder`/`app`/`test` -> update `README.md` & `Program_Licenses.md` -> commit & `gh pr create`).
- **Creating a new tool** (*"I'd like to create an image for `<tool>`"*): Check that `<tool>` is not already in `build-files/`, create branch `adding-<tool>-<version>`, search `Program_Licenses.md` and `build-files/` for license/install/test patterns, select an Ubuntu template from `dockerfile-template/` before falling back to Micromamba, write functional tests in `FROM app AS test`, build all stages, update `README.md` and `Program_Licenses.md`, commit, and run `gh pr create`.
- Always pass `--progress=plain` to `docker build` so compiler/package errors appear directly in output.
- Always read `.github/PULL_REQUEST_TEMPLATE.md` before calling `gh pr create` so the PR description follows the repository template.