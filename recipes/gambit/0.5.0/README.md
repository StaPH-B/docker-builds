# gambit container

Main tool : [gambit](github.com/hesslab-gambit/gambit)

Full documentation: https://gambit-genomics.readthedocs.io/en/latest/

GAMBIT (Genomic Approximation Method for Bacterial Identification and Tracking) is a tool for rapid taxonomic identification of microbial pathogens. It uses an extremely efficient genomic distance metric along with a curated database of approximately 50,000 reference genomes (derived from NCBI RefSeq) to identify unknown bacterial genomes within seconds.

## Example Usage

```bash
# run gambit on assembly 
gambit query GCF_000240185.1_ASM24018v2_genomic.fna
```