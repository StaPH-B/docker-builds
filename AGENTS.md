# AGENTS.md — StaPH-B/docker-builds

## Repository Overview
`StaPH-B/docker-builds` maintains reproducible, Singularity/Apptainer-compatible Dockerfiles and documentation for public health bioinformatics tools.

- `build-files/<tool>/<version>/` — Container build contexts (`Dockerfile`, `README.md`, and optional helper/test files such as `env.yaml` or `test.sh`).
- `dockerfile-template/` — Reference multi-stage templates (`Dockerfile`, `Dockerfile_builder`, `Dockerfile_mamba`, `Dockerfile_python3`, `README.md`).
- `docs/make_containers.md` & `docs/contribute.md` — Container authoring standards and contribution guidelines.
- `README.md` — Root catalog table listing every tool and its available version tags.
- `Program_Licenses.md` — Alphabetical table mapping each software package to its license and upstream license URL.
- `tests/` — Standalone test scripts and sample datasets referenced across containers.
- `.github/PULL_REQUEST_TEMPLATE.md` — Required checklist and structure for Pull Requests.
- `.github/workflows/test-PR-dockerfiles.yml` — CI workflow that builds PR Dockerfiles.

---

## Workflow 1: Updating an Existing Tool Container

Triggered when a user asks **"Does `<tool>` need an update?"** (or asks to update an existing tool under `build-files/<tool>/`).

### Step 1: Check Current vs. Upstream Version
1. Inspect `build-files/<tool>/` to identify the latest standard version directory (ignore specialized variant suffixes such as `-db`, `-slim`, `-no_model`, or custom database builds unless requested).
2. Read `build-files/<tool>/<latest_version>/Dockerfile` (and `README.md`) to locate the upstream source (`LABEL website`, GitHub repo, PyPI package, Bioconda recipe, or download URL).
3. Query the upstream source for the latest **stable** release (skip pre-releases, `alpha`, `beta`, and `rc` tags unless explicitly requested).
4. Compare versions:
   - **If already up to date**: Report the current version in `build-files/<tool>/` and the latest upstream version, then stop.
   - **If a newer version exists**: State the current version and target `<new_version>`, then proceed immediately to Step 2.

### Step 2: Create Branch, Copy Directory & Update Files
1. Create a new branch from `master`:
   ```bash
   git checkout -b adding-<tool>-<new_version>
   ```
2. Create `build-files/<tool>/<new_version>/` and copy all files and subdirectories from `build-files/<tool>/<latest_version>/` (`Dockerfile`, `README.md`, and any supporting scripts, `env.yaml`, or `tests/` directories).
   - Normalize `Readme.md` to `README.md` if needed.
3. Update `build-files/<tool>/<new_version>/Dockerfile`:
   - Update the version `ARG` (e.g., `ARG BCFTOOLS_VER="<new_version>"` or `ARG <TOOL>_VERSION="<new_version>"`), including any `ARG` re-declarations in `FROM ... AS app` and `FROM app AS test` blocks.
   - Ensure `LABEL software.version="${<TOOL>_VER}"` (or matches `<new_version>`).
   - Reset `LABEL dockerfile.version="1"`.
   - Update all `wget`/`curl` URLs, archive folder paths, `pip install` pins, and `env.yaml` pins so no stale references to `<latest_version>` remain.
4. Update `build-files/<tool>/<new_version>/README.md` with `<new_version>` and any updated tool versions or example tags.

### Step 3: Build All Stages, Verify License & Update `README.md`
1. Build all Dockerfile stages sequentially (`builder` if present -> `app` -> `test`) following **Shared Build & Failure Protocol** below.
2. Add `[<new_version>](build-files/<tool>/<new_version>)` to `<tool>`'s row in the root `README.md`, matching existing formatting.
3. Verify `<tool>` is listed in `Program_Licenses.md` and `LABEL license` in the `Dockerfile` is valid; fix either if missing or outdated.
4. Commit (`adding <tool> version <new_version>`), push `adding-<tool>-<new_version>`, and open a PR using `.github/PULL_REQUEST_TEMPLATE.md`.

---

## Workflow 2: Creating a New Tool Container

Triggered when a user asks **"I'd like to create an image for `<tool>`"** (or asks to add a new tool not yet in `build-files/`).

### Step 1: Verify Tool Absence & Determine Target Version
1. Check `build-files/` (including case variations, hyphens vs. underscores, and `README.md`) to confirm `<tool>` does not already exist.
   - If `<tool>` already exists, inform the user and offer to run **Workflow 1 (Update)** instead.
2. Normalize the directory name `<tool>` to lowercase (matching `build-files/` conventions, e.g., `bcftools`, `ncbi-amrfinderplus`, `assembly_snptyper`).
3. Research the upstream project (GitHub, GitLab, PyPI, CRAN, Bioconda, or official website) to determine:
   - Latest **stable** release `<version>` (unless the user requested a specific version).
   - Official installation method, system/runtime dependencies, primary executable name, `--version` and `--help` flags, and sample test inputs.

### Step 2: Create Branch & Directory Structure
1. Create a new branch from `master`:
   ```bash
   git checkout -b adding-<tool>-<version>
   ```
2. Create `build-files/<tool>/<version>/` and scaffold:
   - `build-files/<tool>/<version>/Dockerfile`
   - `build-files/<tool>/<version>/README.md` (using `dockerfile-template/README.md` as a structural guide)
   - Any supporting test scripts or small fixtures if required by the `test` stage.

### Step 3: Search the Repo for License Information
1. Search `Program_Licenses.md` (case-insensitive) and existing `build-files/*/Dockerfile` files—the tool may already be documented in `Program_Licenses.md` or bundled inside another container.
2. Also inspect the upstream repository (`LICENSE`, `COPYING`, `pyproject.toml`, `setup.py`, `DESCRIPTION`, or upstream `README.md`) to confirm the exact license name and direct URL to the license file.
3. Ensure `LABEL license="<upstream_license_url>"` is set in `build-files/<tool>/<version>/Dockerfile`.
4. If `<tool>` is not yet in `Program_Licenses.md` (or its row is incomplete), add a new row in **alphabetical order**:
   ```markdown
   | <Tool Display Name> | <License Type> | <Direct License URL to> |
   ```

### Step 4: Select the Appropriate Repo Template (Ubuntu Before Micromamba)
Read `dockerfile-template/` and `docs/make_containers.md` and choose the base template using this strict priority order—**always prefer Ubuntu-based templates over Micromamba** unless dependency resolution makes Ubuntu impractical:

1. **`dockerfile-template/Dockerfile` (`ubuntu:noble`) — First Choice**:
   - Use for tools distributed as precompiled Linux binaries, `apt-get` packages, Perl/R/Java tools, or straightforward source builds (`make` / `./configure`).
2. **`dockerfile-template/Dockerfile_builder` (`ubuntu:noble` multi-stage `builder` -> `app` -> `test`) — Second Choice**:
   - Use for compiled C, C++, Rust, or Go tools that require heavy build toolchains (`build-essential`, `cmake`, `cargo`, `golang`, `-dev` headers) so only compiled binaries and runtime libraries are copied into `app`.
3. **`dockerfile-template/Dockerfile_python3` (Python slim or `ubuntu:noble` + `pip`) — Third Choice**:
   - Use for pure-Python tools or PyPI packages whose dependencies install cleanly via `pip`.
4. **`dockerfile-template/Dockerfile_mamba` (`mambaorg/micromamba`) — Last Resort Only**:
   - Use **only** when complex bioinformatics dependency trees (e.g., mixed R/Bioconductor, Conda-only C++ libraries, or conflicting Python/system pins) cannot be cleanly installed on Ubuntu via `apt-get`, `pip`, or source/binary builds.

### Step 5: Generate Installation Instructions & Worthwhile Tests
1. **Use repo patterns for installation**:
   - Search `build-files/` for tools in the same language/ecosystem (e.g., Rust `cargo`, C `htslib`/autotools, Python `pip`, Java `.jar`, Perl scripts) to reuse proven `apt-get` dependency lists, `ENV PATH`, `ENV LC_ALL=C`, `WORKDIR /data`, and `CMD` conventions.
   - Follow upstream documentation for exact build flags, binary placement (`/usr/local/bin/`), and environment variables.
2. **Generate worthwhile tests in `FROM app AS test`**:
   - Search `build-files/*/Dockerfile` and `tests/` for testing idioms used in this repo.
   - Every `test` stage MUST include:
     1. **CLI smoke checks**: Verify `<executable> --help` and `<executable> --version` (or equivalent subcommands) exit cleanly.
     2. **Functional execution test**: Download or copy a small, real sample dataset (from the upstream repo's `test/` or `example/` folder, or minimal synthetic input) and run the tool's core workflow end-to-end.
     3. **Output assertions**: Verify that expected output files exist, are non-empty (`test -s` or `ls`), and contain expected headers/results (`grep` or `head`).

### Step 6: Build Stages, Update Root `README.md` & Open PR
1. Build all Dockerfile stages sequentially (`builder` if present -> `app` -> `test`) following **Shared Build & Failure Protocol** below.
2. Open the root `README.md` and insert a new row in **alphabetical order** for `<tool>` with `[<version>](build-files/<tool>/<version>)`, matching the exact table column structure and link style of neighboring rows.
3. Verify `git status` contains only:
   - `build-files/<tool>/<version>/`
   - `README.md`
   - `Program_Licenses.md` (if added/updated)
4. Commit, push, and open a PR using `.github/PULL_REQUEST_TEMPLATE.md`:
   ```bash
   git add build-files/<tool>/<version> README.md Program_Licenses.md
   git commit -m "adding <tool> version <version>"
   git push -u origin adding-<tool>-<version>
   gh pr create --title "Add <tool> <version>" --body "<filled PR template>"
   ```

---

## Shared Build & Failure Protocol

### Sequential Multi-Stage Builds
Inspect `Dockerfile` for named stages (`FROM ... AS <stage>`) and build each stage sequentially with `--progress=plain`:
```bash
# 1. Optional builder stage (only if "AS builder" exists):
docker build --progress=plain --target builder -t staphb/<tool>:<version>-builder build-files/<tool>/<version>

# 2. Required production app stage:
docker build --progress=plain --target app -t staphb/<tool>:<version> build-files/<tool>/<version>

# 3. Required validation test stage:
docker build --progress=plain --target test -t staphb/<tool>:<version>-test build-files/<tool>/<version>
```

### What to Do If a Stage Fails
- **Never commit or open a PR with a failing build.**
- Diagnose by stage:
  - **`builder` or download/compile failure in `app`**:
    - *404 / archive not found*: Verify upstream tag prefixes (`v1.2.3` vs `1.2.3`) or release asset names and fix the URL.
    - *Missing compiler/library*: Add missing `apt-get` build packages (`build-essential`, `zlib1g-dev`, `libbz2-dev`, `liblzma-dev`, `libcurl4-openssl-dev`, `cmake`, etc.) or companion libraries.
    - *EOL base image*: Upgrade outdated bases (`ubuntu:bionic`/`focal`) to `ubuntu:noble` and update `LABEL base.image`.
  - **`app` runtime failure**:
    - *Missing shared library or binary*: Install runtime libraries (non-`-dev`) in `app` and verify `COPY --from=builder` paths and `ENV PATH`.
    - *Singularity/Apptainer compatibility*: Keep `ENV LC_ALL=C` and `WORKDIR /data`; avoid `USER` directives or writing to root-owned directories at runtime.
  - **`test` stage failure**:
    - *CLI flag or output mismatch*: Align test flags and `grep` assertions with the tool's actual CLI behavior.
    - *Dead test data URL*: Replace broken external test file links with a valid upstream test file or inline test fixture.
- Patch the `Dockerfile`, rebuild from the failed stage through `test`, and confirm exit code `0`.
- **Retry limit**: Attempt up to **3 targeted fix-and-rebuild cycles**. If still failing, stop before pushing/opening a PR and report:
  1. Which stage failed (`builder`, `app`, or `test`).
  2. The exact command and error output.
  3. Fixes attempted and what manual input is needed.

---

## Container Standards Checklist
- **Multi-stage layout**: `FROM <base> AS app` followed by `FROM app AS test` (plus optional `AS builder`).
- **Required `LABEL`s in `app`**: `base.image`, `dockerfile.version`, `software`, `software.version`, `description`, `website`, `license`, `maintainer`, `maintainer.email`.
- **Locale & Workdir**: Always include `ENV LC_ALL=C` and `WORKDIR /data` in `app`.
- **Clean layers**: Combine `apt-get update && apt-get install -y --no-install-recommends ... && apt-get autoclean && rm -rf /var/lib/apt/lists/*` into single `RUN` layers.