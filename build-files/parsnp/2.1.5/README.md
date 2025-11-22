# ParSNP

This container implements [ParSNP](https://github.com/marbl/parsnp) from the [Harvest suite](https://harvest.readthedocs.io/en/latest/).

## Includes

- ParSNP: `parsnp`
- [FastTree](https://github.com/morgannprice/fasttree/): `FastTree` or `fasttree` : 2.2.0
- [RAxML](https://github.com/stamatak/standard-RAxML): `raxmlHPC-PTHREADS` : 8.2.12
- [Mash](https://github.com/marbl/Mash/): `mash` : 2.3
- [PhiPack](https://www.maths.otago.ac.nz/~dbryant/software/phimanual.pdf): `Phi` : 1.1
- [HarvestTools](https://harvest.readthedocs.io/en/latest/): `harvesttools` : 1.3
- [FastANI](https://github.com/ParBLiSS/FastANI/): `fastani` : 1.34

## Running a container

Pull the image from Docker Hub.

```bash
docker pull staphb/parsnp:latest
```

OR, clone this repository to build & test the image yourself.

```bash
git clone git@github.com:StaPH-B/docker-builds.git
cd docker-builds/build-files/parsnp/2.1.5
# Run tests
docker build --target=test -t parsnp-test .
# Build production image
docker build --target=app -t parsnp .
```

## Example data analysis

Set up some input data.

```bash
mkdir -p parsnp/input_dir
cd parsnp/input_dir
wget \
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/698/515/GCA_000698515.1_CFSAN000661_01.0/GCA_000698515.1_CFSAN000661_01.0_genomic.fna.gz \
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/749/005/GCA_000749005.1_CFSAN000669_01.0/GCA_000749005.1_CFSAN000669_01.0_genomic.fna.gz
gunzip *.gz
cd ../
```

Run the container to generate a core genome alignment, call SNPs, and build a phylogeny. Output files are written to `output_dir`.

```bash
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) staphb/parsnp:latest parsnp \
-d input_dir \
-o outdir_parsnp \
--use-fasttree \
-v \
-c \
-r !
```
