---
name: update-container
description: Check if a bioinformatics tool in StaPH-B/docker-builds has a newer upstream release, scaffold the new version directory, build and test all Dockerfile stages, update README.md and Program_Licenses.md, and open a PR. Use when a user asks "Does <tool> need an update?" or requests updating a container.
---

# Update Container Workflow

Execute this workflow when asked to check for or apply a version update to `<tool>` in `StaPH-B/docker-builds`.

## 1. Version Check
- Find the latest non-variant version directory under `build-files/<tool>/`.
- Read its `Dockerfile` (`LABEL website` and download/install commands) to determine the upstream source.
- Check upstream for the latest stable version. If `build-files/<tool>/` already has the latest stable version, report this to the user and exit.

## 2. Scaffold & Version Bump
- Create `build-files/<tool>/<new_version>/` and copy all files from `build-files/<tool>/<latest_version>/` (`Dockerfile`, `README.md`, and any auxiliary scripts, YAML files, or `tests/` directories).
- Update `Dockerfile`:
  - Set `<TOOL>_VER` / `<TOOL>_VERSION` to `<new_version>` (including any `ARG` re-declarations in `app` and `test` stages).
  - Ensure `LABEL software.version="${<TOOL>_VER}"` and `LABEL dockerfile.version="1"`.
  - Update any hardcoded URLs, directory paths, or package pins.
- Update `build-files/<tool>/<new_version>/README.md` to reflect `<new_version>`.

## 3. Multi-Stage Docker Build & Failure Recovery
Run builds stage-by-stage with `--progress=plain`:
```bash
# Optional builder stage (only if "AS builder" is in Dockerfile):
docker build --progress=plain --target builder -t staphb/<tool>:<new_version>-builder build-files/<tool>/<new_version>

# Production app stage:
docker build --progress=plain --target app -t staphb/<tool>:<new_version> build-files/<tool>/<new_version>

# Validation test stage:
docker build --progress=plain --target test -t staphb/<tool>:<new_version>-test build-files/<tool>/<new_version>
```

If a build fails:
1. Do **not** create a commit or PR.
2. Check the failing stage:
   - `builder` / `app` download or compile error: verify upstream release archive URL/tag format, missing `apt-get` build/runtime dependencies, or EOL base images (upgrade to `ubuntu:noble` if needed).
   - `test` failure: check whether CLI flags, version output format, or test data URLs changed in `<new_version>`.
3. Patch `build-files/<tool>/<new_version>/Dockerfile` and rebuild through `test` (max 3 attempts). If still failing, stop and report the failing stage, error logs, and attempted fixes.

## 4. Update `README.md` & `Program_Licenses.md`
- **Root `README.md`**: Add `[<new_version>](build-files/<tool>/<new_version>)` to `<tool>`'s row matching the surrounding version link syntax.
- **`Program_Licenses.md`**: Confirm `<tool>` is listed alphabetically with a valid license name and working upstream license URL; add or repair the row and `LABEL license` in the `Dockerfile` if missing.

## 5. Git Branch & Pull Request
```bash
git checkout -b add-<tool>-<new_version>
git add build-files/<tool>/<new_version> README.md Program_Licenses.md
git commit -m "adding <tool> version <new_version>"
git push -u origin add-<tool>-<new_version>
```
Read `.github/PULL_REQUEST_TEMPLATE.md` and run `gh pr create` with a completed PR description (or provide the push/PR details if `gh` is unavailable).
