# KRAKEN2-2.0.9-beta docker image

Main tool: [KRAKEN2](https://ccb.jhu.edu/software/kraken2/)

This kraken2 docker image does include a kraken2 database along with the kraken2 program and its dependencies. It contains the "Minikraken v2 8GB" database, which contains "Refseq: bacteria, archaea, viral, and human" sequences. It was downloaded from the AWS site hosted by Ben Langmead on 2020-09-16 
  * https://benlangmead.github.io/aws-indexes/k2

If you have your own kraken2 database, please use the docker image that does not contain a database, as the docker image will be MUCH smaller in size and easier to work with. See here for example usage and link to dockerhub:
  * https://github.com/StaPH-B/docker-builds/blob/master/kraken2/2.0.9-beta-no-db/README.md
  * docker image name and tag: `staphb/kraken2:2.0.9-beta-no-db` https://hub.docker.com/r/staphb/kraken2/tags

## Example Usage: Docker

```bash
# download the docker image
# (this will likely take a while, maybe 10-15 min, due to the size of the database)
$ docker pull staphb/kraken2:2.0.9-beta

# directory inside the docker image that contains kraken2 db files 
$ docker run --rm staphb/kraken2:2.0.9-beta ls /kraken2-db
database100mers.kmer_distrib
database150mers.kmer_distrib
database200mers.kmer_distrib
hash.k2d
opts.k2d
taxo.k2d

# fastq files in my $PWD
$ ls 
SRR500494_1.fastq.gz SRR500494_2.fastq.gz

# run kraken2 via docker, mount $PWD to /data in the container
# super long oneliner broken into multiple lines for readability
$ docker run --rm -u $(id -g):$(id -g) -v $PWD:/data \
    staphb/kraken2:2.0.9-beta-no-db \
  kraken2 --db /kraken2-db --threads 16 \
    --output /data/kraken2.output --report /data/kraken2.report \
    --paired /data/SRR500494_1.fastq.gz /data/SRR500494_2.fastq.gz
# OUTPUT:
Loading database information... done.
558374 sequences (168.63 Mbp) processed in 5.100s (6568.7 Kseq/m, 1983.74 Mbp/m).
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
# (this will likely take a while, maybe 10-15 min, due to the size of the database)
$ singularity build kraken2.2.0.9-beta.sif docker://staphb/kraken2:2.0.9-beta

# directory inside the singularity image that contains kraken2 db files
$ singularity exec kraken2.2.0.9-beta.sif ls /kraken2-db
database100mers.kmer_distrib  database150mers.kmer_distrib  database200mers.kmer_distrib  hash.k2d  opts.k2d  taxo.k2d

# fastq files in my $PWD
$ ls
SRR500494_1.fastq.gz SRR500494_2.fastq.gz

# run kraken2 via singularity, mount $PWD to /data in the container
# super long oneliner broken into multiple lines for readability
$ singularity exec --no-home \
    -B $PWD:/data \
    kraken2.2.0.9-beta.sif \
  kraken2 --db /kraken2-db --threads 16 \
    --output /data/kraken2.output --report /data/kraken2.report \
    --paired /data/SRR500494_1.fastq.gz /data/SRR500494_2.fastq.gz
# OUTPUT:
Loading database information... done.
558374 sequences (168.63 Mbp) processed in 4.749s (7055.0 Kseq/m, 2130.61 Mbp/m).
  555247 sequences classified (99.44%)
  3127 sequences unclassified (0.56%)
# SUCCESS!
```
