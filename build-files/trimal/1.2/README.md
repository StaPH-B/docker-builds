# trimal v1.2rev59 Docker Image

This Docker image provides **trimal v1.2rev59**, a command-line tool for automated trimming of multiple sequence alignments.

Maintained as part of the [StaPH-B/docker-builds](https://github.com/StaPH-B/docker-builds) repository.

---

## 📦 Included Tools

- **trimal** (v1.2rev59)

---

## 🧱 Base Image

- `ubuntu:16.04`

---

## 🛠️ Build Overview

This image is built from source using:
- `make` from the official `trimal.v1.2rev59.tar.gz` archive
- Only the compiled `trimal` binary is retained in the runtime image

---

## 🐳 Usage

### Example: Display version

```bash
docker run --rm staphb/trimal:1.2rev59 trimal --version

