## Description

*Please fill in so we understand what this PR is for*

**Tool Name:** (e.g., samtools)

**Tool Version:** (e.g., 1.16.1)

**Purpose of PR:** (e.g., New tool addition / Version bump / Bug fix)

---

## PR Checklist
*Replace '[ ]' with '[x]' to mark off your progress.*
*Leave them blank if you're stuck!*

### 1. Repository Standards
*These are also checked in github actions. Don't panic if one or more of these fail.
- [ ] **Pathing:** Files are in `build-files/<tool_name>/<version>/` (lowercase).
- [ ] **Stages:** Dockerfile includes both `AS app` and `AS test` stages.
- [ ] **Runtime:** `WORKDIR` is set to `/data` and a `CMD` is defined.
- [ ] **Security:** Container is configured to run as a **non-root** user.
- [ ] **Linting:** Required OCI Labels are included in the Dockerfile.

### 2. Documentation & Metadata
- [ ] **Tool README:** A `README.md` exists in the tool's version directory.
- [ ] **Central Registry:** Main `README.md` and `Program_Licenses.md` are updated.

### 3. Verification
- [ ] **Local Build:** I have verified the build locally:
  `docker build --target test -t tool:test build-files/<tool>/<version>/`

> ### A Note on Automated Tests
> To help keep our containers secure and consistent, a bot will scan your PR 
> for layout and security standards. **If the tests fail, don't worry!** It's a 
> normal part of our process. We’ll work with you to fix any red flags.