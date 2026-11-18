---
name: create-container
description: Create a new bioinformatics tool container in StaPH-B/docker-builds from scratch. Checks that the tool is not already present, creates branch adding-<tool>-<version>, searches the repo for license and installation patterns, selects an Ubuntu-first template from dockerfile-template/, generates worthwhile tests, builds all Dockerfile stages, updates README.md and Program_Licenses.md, and opens a PR. Use when a user says "I'd like to create an image for <tool>" or requests adding a new tool.
---

# Create New Container Workflow

Execute this workflow when asked to create a new container image for `<tool>` in `StaPH-B/docker-builds`.

## 1. Check Existing Repo & Resolve Upstream Version
- Check `build-files/` (case-insensitive) and root `README.md` to confirm `<tool>` does not already exist. If it exists, inform the user and offer to update it instead.
- Normalize `<tool>` to lowercase directory format (matching `build-files/`).
- Check the upstream source (GitHub Releases/Tags, PyPI, CRAN, Bioconda, or official website) for the latest **stable** release `<version>` (unless the user specified a version).

## 2. Create Branch & Directory
```bash
git checkout -b adding-<tool>-<version>
mkdir -p build-files/<tool>/<version>
```

## 3. Search Repo & Upstream for License Info
- Search `Program_Licenses.md` and `build-files/*/Dockerfile` for `<tool>` or related packages.
- Check the upstream repository's `LICENSE` / `COPYING` file to verify the license type and direct URL.
- Set `LABEL license="<license_url>"` in the `Dockerfile`, and add an alphabetical row to `Program_Licenses.md` (`| <Software> | <License> | <Link to license> |`) if missing.

## 4. Pick Template (Ubuntu Before Micromamba)
Inspect `dockerfile-template/` and `docs/make_containers.md` and select the base template in strict priority order:
1. **`dockerfile-template/Dockerfile` (`ubuntu:noble`)** — Default for `apt-get` packages, precompiled binaries, Perl/R/Java tools, and straightforward builds.
2. **`dockerfile-template/Dockerfile_builder` (`ubuntu:noble` multi-stage)** — For C/C++/Rust/Go tools needing separate build toolchains and lean runtime images.
3. **`dockerfile-template/Dockerfile_python3`** — For Python/PyPI packages with clean `pip` installs.
4. **`dockerfile-template/Dockerfile_mamba`** — Last resort only when complex bioinformatics dependencies cannot be cleanly resolved on Ubuntu.

## 5. Scaffold Files & Generate Worthwhile Tests
- Search `build-files/` for similar tools to reuse proven `apt-get` dependency lists, `ENV LC_ALL=C`, `WORKDIR /data`, and `CMD` conventions.
- Create `build-files/<tool>/<version>/README.md` modeled on `dockerfile-template/README.md`.
- Write `build-files/<tool>/<version>/Dockerfile` with:
  - All required `LABEL`s (`base.image`, `dockerfile.version="1"`, `software`, `software.version`, `description`, `website`, `license`, `maintainer`, `maintainer.email`).
  - `FROM app AS test` containing:
    1. `--help` and `--version` CLI checks.
    2. A real functional execution using small upstream test data (or minimal synthetic input) and assertions (`test -s`, `grep`) verifying non-empty, valid outputs.

## 6. Build Stages, Update `README.md` & Open PR
- Build all stages sequentially with `--progress=plain` (`--target builder` if present, `--target app`, and `--target test`).
- If any stage fails, diagnose and fix (up to 3 attempts). Never commit or push a failing build.
- Add `<tool>` in **alphabetical order** to the root `README.md` table with `[<version>](build-files/<tool>/<version>)`.
- Commit and open a PR using `.github/PULL_REQUEST_TEMPLATE.md`:
  ```bash
  git add build-files/<tool>/<version> README.md Program_Licenses.md
  git commit -m "adding <tool> version <version>"
  git push -u origin adding-<tool>-<version>
  gh pr create --title "Add <tool> <version>" --body "<filled PR template>"
  ```