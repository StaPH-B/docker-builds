# VirulenceFinder Docker Image

A docker image  that contains VirulenceFinder, a tool for identifying virulence factors in E. coli isolates from reads or assemblies

[Link to StaPH-B DockerHub repository](https://hub.docker.com/r/staphb/virulencefinder)

Main tool:

- Main Code Repo: [https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/](https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/)
- VirulenceFinder database: [https://bitbucket.org/genomicepidemiology/virulencefinder_db/src/master/](https://bitbucket.org/genomicepidemiology/virulencefinder_db/src/master/)
- You may be familiar with the web version of VirulenceFinder: [https://cge.food.dtu.dk/services/VirulenceFinder/](https://cge.food.dtu.dk/services/VirulenceFinder/)

Additional tools:

- python 3.8.10
- biopython 1.73
- [kma](https://bitbucket.org/genomicepidemiology/kma/src/master/) 1.0.0
- ncbi-blast+ 2.9.0

## Version information

VirulenceFinder version: 2.0.4 [https://bitbucket.org/genomicepidemiology/virulencefinder/src/2.0.4/](https://bitbucket.org/genomicepidemiology/virulencefinder/src/2.0.4/) made on 2020-02-06

VirulenceFinder database version: commit `f678bdc15283aed3a45f66050d2eb3a6c9651f3f` made on 2023‑05‑03. [Link to commit history](https://bitbucket.org/genomicepidemiology/virulencefinder_db/commits/)

## Requirements

- Docker or Singularity
- E. coli raw reads (fastq.gz) or assembly (fasta)
  - Illumina, Ion Torrent, Roche 454, SOLiD, Oxford Nanopore, and PacBio reads are supported. (I've only tested Illumina reads)

## Usage

```bash
usage: virulencefinder.py [-h] -i INFILE [INFILE ...] [-o OUTDIR] [-tmp TMP_DIR] [-mp METHOD_PATH] [-p DB_PATH] [-d DATABASES] [-l MIN_COV] [-t THRESHOLD] [-x] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE [INFILE ...], --infile INFILE [INFILE ...]
                        FASTA or FASTQ input files.
  -o OUTDIR, --outputPath OUTDIR
                        Path to blast output
  -tmp TMP_DIR, --tmp_dir TMP_DIR
                        Temporary directory for storage of the results from the external software.
  -mp METHOD_PATH, --methodPath METHOD_PATH
                        Path to method to use (kma or blastn)
  -p DB_PATH, --databasePath DB_PATH
                        Path to the databases
  -d DATABASES, --databases DATABASES
                        Databases chosen to search in - if non is specified all is used
  -l MIN_COV, --mincov MIN_COV
                        Minimum coverage
  -t THRESHOLD, --threshold THRESHOLD
                        Minimum threshold for identity
  -x, --extented_output
                        Give extented output with allignment files, template and query hits in fasta and a tab seperated file with gene profile results
  -q, --quiet
```

## Notes and Recommendations

- You do not need to supply a database or use the `-p` or `-d` flags
  - Database is included in the image and is in the default/expected location within the image filesystem: `/database`
  - (*NOT RECOMMENDED*) If you do need to use your own database, you will need to first index it with `kma` and use the `virulencefinder.py -p` flag. You can find instructions for this on the VirulenceFinder Bitbucket README. `kma` is included in this docker image for database indexing.
  - VirulenceFinder does **NOT** create an output directory when you use the `-o` flag. You MUST create it beforehand or it will throw an error.
  - **Default % Identity threshold: 90%**. Adjust with `-t 0.95`
  - **Default % coverage threshold: 60%**. Adjust with `-l 0.70`
  - Use the `-x` flag (extended output) if you want the traditional/legacy VirulenceFinder output files `results_tab.tsv  results.txt  Virulence_genes.fsa  Hit_in_genome_seq.fsa`. Otherwise you will need to parse the default output file `data.json` for results
  - (*RECOMMENDED*) Use raw reads due to the increased sensitivity (without loss of specificity) and the additional information gleaned from KMA output (specifically the depth metric). You also save time from having to assemble the genome first. [CITATION NEEDED, PROBABLY THE KMA PAPER]
- Querying reads:
  - This will run VirulenceFinder with `kma` (instead of ncbi-blast+)
  - Only one of the PE read files is necessary. There is likely little benefit to using both R1 and R2. It will take longer to run if you use both R1 and R2 files.
- Querying assemblies:
  - This will run VirulenceFinder with `ncbi-blast+`
  - VirulenceFinder does not clean up after itself. `tmp/` (which contains 7 different `.xml` files) will exist in the specified output directory

## Example Usage: Docker

```bash
# download the image
$ docker pull staphb/virulencefinder:2.0.4

# input files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads, mount PWD to /data inside container (broken into two lines for readabilty)
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/virulencefinder:2.0.1 \
    virulencefinder.py -i /data/E-coli.R1.fastq.gz -o /data/output-dir-reads

# query assembly
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/virulencefinder:2.0.1 \
    virulencefinder.py -i /data/E-coli.skesa.fasta  -o /data/output-dir-asm
```

## Example Usage: Singularity

```bash
# download the image
$ singularity build virulencefinder.2.0.4.sif docker://staphb/virulencefinder:2.0.4

# files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads; mount PWD to /data inside container
$ singularity exec --no-home -B $PWD:/data virulencefinder.2.0.4.sif \
    virulencefinder.py -i /data/E-coli.R1.fastq.gz -o /data/output-dir-reads

# assembly
$ singularity exec --no-home -B $PWD:/data virulencefinder.2.0.4.sif \
    virulencefinder.py -i /data/E-coli.skesa.fasta  -o /data/output-dir-asm
```
