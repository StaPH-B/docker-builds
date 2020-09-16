# KRAKEN2-2.0.9-beta-no-db docker image

Main tool: [KRAKEN2](https://ccb.jhu.edu/software/kraken2/)

This kraken2 docker image does NOT include a kraken2 database, it only contains the kraken2 program and dependencies. 

The user will need to mount/bind a directory from their host machine that contains kraken2 database files (hash.k2d, opts.k2d, taxo.k2d) to a directory in the container. `/kraken2-db` exists inside the docker image for this purpose, but feel free to use another location.


## Example Usage: Docker

```bash
# download the docker image
$ docker pull staphb/kraken2:2.0.9-beta-no-db

# directory containing kraken2 db files (in $PWD)
$ ls minikraken2_v2_8GB_201904_UPDATE/
database100mers.kmer_distrib  database150mers.kmer_distrib  database200mers.kmer_distrib  hash.k2d  opts.k2d  taxo.k2d

# fastq files in my $PWD
$ ls 
minikraken2_v2_8GB_201904_UPDATE/ SRR500494_1.fastq.gz SRR500494_2.fastq.gz

# run kraken2 via docker, mount $PWD to /data in the container, and mount my local kraken2 db to /kraken2-db inside the container
# super long oneliner broken into multiple lines for readability
$ docker run --rm -u $(id -g):$(id -g) \
    -v $PWD:/data \
    -v $PWD/minikraken2_v2_8GB_201904_UPDATE:/kraken2-db \
    staphb/kraken2:2.0.9-beta-no-db \
  kraken2 --db /kraken2-db --threads 16 --output /data/kraken2.output --report /data/kraken2.report --paired /data/SRR500494_1.fastq.gz /data/SRR500494_2.fastq.gz
# OUTPUT:
Loading database information... done.
558374 sequences (168.63 Mbp) processed in 5.035s (6654.4 Kseq/m, 2009.64 Mbp/m).
  555247 sequences classified (99.44%)
  3127 sequences unclassified (0.56%)
# SUCCESS!

# After kraken2 finishes running, and the container exits,
# output files will be in your PWD if you correctly specify the PATHs and mounted them proprely like the above example
$ head kraken2.report
  0.56  3127    3127    U       0       unclassified
 99.44  555247  151     R       1       root
 99.41  555092  1       R1      131567    cellular organisms
 99.41  555089  133     D       2           Bacteria
 99.39  554954  70      P       1224          Proteobacteria
 99.37  554876  441     C       1236            Gammaproteobacteria
 99.29  554412  3364    O       91347             Enterobacterales
 98.67  550969  8633    F       543                 Enterobacteriaceae
 97.06  541941  6277    G       590                   Salmonella
 95.92  535616  479206  S       28901                   Salmonella enterica
```
## Example usage: Singularity

```bash
# download the docker image via singularity, convert to singularity image format
$ singularity build kraken2.2.0.9-beta-no-db.sif docker://staphb/kraken2:2.0.9-beta-no-db

# directory containing kraken2 db files
$ ls minikraken2_v2_8GB_201904_UPDATE/
database100mers.kmer_distrib  database150mers.kmer_distrib  database200mers.kmer_distrib  hash.k2d  opts.k2d  taxo.k2d

# fastq files in my $PWD
$ ls
minikraken2_v2_8GB_201904_UPDATE/ SRR500494_1.fastq.gz SRR500494_2.fastq.gz

# run kraken2 via singularity, mount $PWD to /data in the container, and mount my local kraken2 db to /kraken2-db inside the container
# super long oneliner broken into multiple lines for readability
$ singularity exec --no-home \
    -B $PWD:/data \
    -B $PWD/minikraken2_v2_8GB_201904_UPDATE:/kraken2-db \
    kraken2.2.0.9-beta-no-db.sif \
  kraken2 --db /kraken2-db --threads 16 --output /data/kraken2.output --report /data/kraken2.report --paired /data/SRR500494_1.fastq.gz /data/SRR500494_2.fastq.gz
# OUTPUT:
Loading database information... done.
558374 sequences (168.63 Mbp) processed in 4.553s (7357.8 Kseq/m, 2222.06 Mbp/m).
  555247 sequences classified (99.44%)
  3127 sequences unclassified (0.56%)
# SUCCESS!
```
