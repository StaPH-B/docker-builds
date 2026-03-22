# gambit container

Main tool : [gambit](github.com/jlumpe/gambit)

Full documentation: https://gambit-genomics.readthedocs.io/en/latest/

GAMBIT (Genomic Approximation Method for Bacterial Identification and Tracking) is a tool for rapid taxonomic identification of microbial pathogens. It uses an extremely efficient genomic distance metric along with a curated database of approximately 50,000 reference genomes (derived from NCBI RefSeq) to identify unknown bacterial genomes within seconds.

## Dependencies

GAMBIT is built using [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) with the following dependencies:

<details>
<summary>Dependencies</summary>
  
| Dependency | Version | Notes |
|---|---|---|
| Python | ==3.11 | |
| NumPy | >=1.24, <2.0 | Pinned to 1.x; GAMBIT C extensions are incompatible with NumPy 2.x |
| SciPy | >=1.11 | |
| SQLAlchemy | >=2.0 | |
| Alembic | >=1.13 | |
| BioPython | >=1.80 | |
| h5py | >=3.9 | |
| attrs | >=23 | |
| cattrs | >=23.0 | |
| click | >=8.0 | |
| setuptools | | |
| pandas | >=2.0 | |
</details>

## Example Usage

```bash
# run gambit on assembly 
gambit query GCF_000240185.1_ASM24018v2_genomic.fna
```
