# ParSNP container

Main tool : [ParSNP](https://github.com/marbl/parsnp)

Additional tools:
- ParSNP: `parsnp`
- FastTree: `FastTree` or `fasttree`
- RAxML: `raxmlHPC-PTHREADS`
- Mash: `mash`
- PhiPack: `Phi`
- HarvestTools: `harvesttools`

Full documentation: https://harvest.readthedocs.io/en/latest/

# Example Usage

Run the container to generate a core genome alignment, call SNPs, and build a phylogeny. Input fasta files are in input_dir. Output files are written to `output_dir`.

```
parsnp \
  -d input_dir \
  -o outdir_parsnp \
  --use-fasttree \
  -v \
  -c \
  -r !
```
