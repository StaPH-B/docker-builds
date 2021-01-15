# SerotypeFinder Container How-To

### Description
A docker container that contains SerotypeFinder, a tool for serotyping E. coli isolates from reads or assemblies

### Version information
SerotypeFinder version: 2.0.1 https://bitbucket.org/genomicepidemiology/serotypefinder/src/2.0.1/

SerotypeFinder database version: Git commit `39c68c6e1a3d94f823143a2e333019bb3f8dddba` made on 2020‑09‑24. [Link to commit history](https://bitbucket.org/genomicepidemiology/serotypefinder_db/commits/)

You may be familiar with the web version of SerotypeFinder: https://cge.cbs.dtu.dk/services/SerotypeFinder/

## Requirements
  * Docker or Singularity
  * E. coli raw reads (fastq.gz) or assembly (fasta)
    * Illumina, Ion Torrent, Roche 454, SOLiD, Oxford Nanopore, and PacBio reads are supported. (I've only tested ILMN reads)

## Notes and Recommendations
  * You do not need to supply a database or use the `-p` or `-d` flags
    * Database is included in the container and is in the default/expected location within the container: `/database`
    * (NOT RECOMMENDED) If you do need to use your own database, you will need to first index it with `kma` and use the `serotypefinder.py -p` flag. You can find instructions for this on the SerotypeFinder Bitbucket README. `kma` is included in this docker container.
  * SerotypeFinder does **NOT** create an output directory when you use the `-o` flag. You MUST create it beforehand or it will throw an error.
  * Default % Identity threshold: 90%. Adjust with `-t 0.95`
  * Default % coverage threshold: 60%. Adjust with `-l 0.70`
  * Use the `-x` flag (extended output) if you want the traditional/legacy SerotypeFinder output files `results_tab.tsv  results.txt  Serotype_allele_seq.fsa  Hit_in_genome_seq.fsa`. Otherwise you will need to parse the default outputfile `data.json` for the results.
  * (RECOMMENDED) use raw reads due to the increased sensitivity (without loss of specificity) and the additional information gleaned from KMA output (specifically the depth metric). You also save time from having to assemble the genome first.
  * Querying reads:
    * Only one of the PE read files is necessary. There is likely no benefit to using both R1 and R2. It will take slightly longer to run (a few extra seconds) if you use both R1 and R2 files.
  * Querying assemblies:
    * a

## Example Usage: Docker
```bash
# download the image
$ docker pull staphb/serotypefinder:2.0.1

# input files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads, mount PWD to /data inside container (broken into two lines for readabilty)
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/serotypefinder:2.0.1 \
  serotypefinder.py -i /data/E-coli.R1.fastq.gz /data/E-coli.R2.fastq.gz -o /data/output-dir-reads

# query assembly
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/serotypefinder:2.0.1 \
  serotypefinder.py -i /data/E-coli.skesa.fasta  -o /data/output-dir-asm
```

## Example Usage: Singularity
```bash
# download the image
$ singularity build serotypefinder.2.0.1.sif docker://staphb/serotypefinder:2.0.1

# files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# reads


# assembly

```
