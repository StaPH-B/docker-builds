# Primer3 v2.3.4 Docker Image

This Docker image provides **Primer3 v2.3.4**, a command-line application for high-throughput PCR primer design, compiled from source and packaged with all necessary thermodynamic parameter files.


---

## 📦 Included Tools

- **primer3_core** (v2.3.4)
- **primer3_config/** — thermodynamic parameter files (e.g. `tm_santalucia.txt`)

---

## 🧱 Base Image

- `ubuntu:16.04`

---

## 🛠️ Build Overview

The image was built using a multi-stage Dockerfile:
- Stage 1: Downloads, compiles Primer3 v2.3.4 from source
- Stage 2: Copies only the final `primer3_core` binary and configuration files
- Stage 3: (optional) Functional test using a basic input

The build uses:
- GCC (via `build-essential`)
- `wget`, `ca-certificates`
- No runtime dependencies beyond system certs

---

## 🐳 Usage

### Example: Run with input file

```bash
docker run --rm -v $(pwd):/data staphb/primer3:2.3.4 \
  primer3_core < /data/input.txt > /data/output.txt
```


If thermodynamic parameters are required, the config is available at:

```
/usr/local/share/primer3_config
```
