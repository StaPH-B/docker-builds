## ParSNP

This image implements [ParSNP](https://github.com/marbl/parsnp) from the [Harvest suite](https://harvest.readthedocs.io/en/latest/).

### Includes
- ParSNP: `parsnp`
- FastTree: `FastTree` or `fasttree`
- RAxML: `raxmlHPC-PTHREADS`
- Mash: `mash`
- PhiPack: `Phi`
- HarvestTools: `harvesttools`

### Example data analysis
Set up some input data.
```
mkdir -p parsnp/input_dir
cd parsnp/input_dir
wget \
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/698/515/GCA_000698515.1_CFSAN000661_01.0/GCA_000698515.1_CFSAN000661_01.0_genomic.fna.gz \
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/749/005/GCA_000749005.1_CFSAN000669_01.0/GCA_000749005.1_CFSAN000669_01.0_genomic.fna.gz
gunzip *.gz
cd ../
```
Run the container to generate a core genome alignment, call SNPs, and build a phylogeny. Output files are written to `output_dir`.
```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) staphb/parsnp:1.5.6 parsnp \
-d input_dir \
-o outdir_parsnp \
--use-fasttree \
-v \
-c \
-r !
```
