# GitHub Copilot Instructions — StaPH-B/docker-builds

Follow the workflows and container standards in `AGENTS.md` for both updating existing tools and creating new tool containers:

## Workflow A: Updating an Existing Tool (*"Does `<tool>` need an update?"*)
1. Compare the latest standard version in `build-files/<tool>/` against upstream stable releases. If up to date, report that and stop.
2. Create branch `adding-<tool>-<new_version>`, copy `build-files/<tool>/<latest_version>/` to `build-files/<tool>/<new_version>/`, and update version `ARG`s, `LABEL software.version`, `LABEL dockerfile.version="1"`, URLs, and `README.md`.
3. Build `--target builder` (if present), `--target app`, and `--target test` sequentially. Fix and rebuild up to 3 times on failure; never commit a failing build.
4. Add `[<new_version>](build-files/<tool>/<new_version>)` to `<tool>`'s row in root `README.md`, verify `Program_Licenses.md` and `LABEL license`, commit (`adding <tool> version <new_version>`), and open a PR using `.github/PULL_REQUEST_TEMPLATE.md`.

## Workflow B: Creating a New Tool (*"I'd like to create an image for `<tool>`"*)
1. Confirm `<tool>` does not exist in `build-files/`, find its latest stable upstream `<version>`, and create branch `adding-<tool>-<version>`.
2. Search `Program_Licenses.md`, `build-files/`, and upstream license files to populate `LABEL license` and add an alphabetical row to `Program_Licenses.md` if missing.
3. Choose a template from `dockerfile-template/` **preferring Ubuntu over Micromamba**: `Dockerfile` (`ubuntu:noble`) -> `Dockerfile_builder` -> `Dockerfile_python3` -> `Dockerfile_mamba` (last resort only).
4. Use existing `build-files/` Dockerfiles and upstream docs to write clean installation steps and worthwhile tests in `FROM app AS test` (`--help`, `--version`, and a real functional run with output checks).
5. Build all stages (`builder` -> `app` -> `test`), add an alphabetical row for `<tool>` in root `README.md`, commit (`adding <tool> version <version>`), and open a PR using `.github/PULL_REQUEST_TEMPLATE.md`.