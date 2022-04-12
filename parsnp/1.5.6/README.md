## ParSNP

This container implements [ParSNP](https://github.com/marbl/parsnp) from the [Harvest suite](https://harvest.readthedocs.io/en/latest/).

### Includes
- ParSNP: `parsnp`
- FastTree: `FastTree` or `fasttree`
- RAxML: `raxmlHPC-PTHREADS`
- Mash: `mash`
- PhiPack: `Phi`
- HarvestTools: `harvesttools`

### Requirements
- [Docker](https://docs.docker.com/get-docker/) 

### Running a container
Pull the image from Docker Hub.
```
docker pull staphb/parsnp:latest
```
OR, clone this repository to build & test the image yourself.
```
git clone git@github.com:StaPH-B/docker-builds.git
cd docker-builds/parsnp/1.5.6
# Run tests
docker build --target=test -t parsnp-test .
# Build production image
docker build --target=app -t parsnp .
```

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
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) staphb/parsnp:latest parsnp \
-d input_dir \
-o outdir_parsnp \
--use-fasttree \
-v \
-c \
-r !
```
