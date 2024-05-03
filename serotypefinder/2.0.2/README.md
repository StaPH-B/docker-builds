# SerotypeFinder Container

A docker container that contains SerotypeFinder, a tool for serotyping E. coli isolates from reads or assemblies

[Link to StaPH-B DockerHub repository](https://hub.docker.com/r/staphb/serotypefinder)

Main tool:

- Main Code Repo: [https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/](https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/)
- You may be familiar with the web version of SerotypeFinder: [https://cge.cbs.dtu.dk/services/SerotypeFinder/](https://cge.cbs.dtu.dk/services/SerotypeFinder/)

Additional tools:

- python 3.8.10
- biopython 1.73
- [kma](https://bitbucket.org/genomicepidemiology/kma/src/master/) 1.4.14
- ncbi-blast+ 2.9.0

## Database Version information

SerotypeFinder database version: Git commit `ada62c62a7fa74032448bb2273d1f7045c59fdda` made on 2022‑05‑16. [Link to commit history](https://bitbucket.org/genomicepidemiology/serotypefinder_db/commits/)

## Requirements

- Docker or Singularity
- E. coli raw reads (fastq.gz) or assembly (fasta)
  - Illumina, Ion Torrent, Roche 454, SOLiD, Oxford Nanopore, and PacBio reads are supported. (I've only tested Illumina reads)

## Usage

```bash
usage: serotypefinder.py [-h] -i INFILE [INFILE ...] [-o OUTDIR] [-tmp TMP_DIR] [-mp METHOD_PATH] [-p DB_PATH] [-d DATABASES] [-l MIN_COV] [-t THRESHOLD] [-x] [-q]

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
  - Database is included in the container and is in the default/expected location within the container: `/database`
  - (*NOT RECOMMENDED*) If you do need to use your own database, you will need to first index it with `kma` and use the `serotypefinder.py -p` flag. You can find instructions for this on the SerotypeFinder Bitbucket README. `kma` is included in this docker container for database indexing.
  - SerotypeFinder does **NOT** create an output directory when you use the `-o` flag. You MUST create it beforehand or it will throw an error.
  - **Default % Identity threshold: 90%**. Adjust with `-t 0.95`
  - **Default % coverage threshold: 60%**. Adjust with `-l 0.70`
  - Use the `-x` flag (extended output) if you want the traditional/legacy SerotypeFinder output files `results_tab.tsv  results.txt  Serotype_allele_seq.fsa  Hit_in_genome_seq.fsa`. Otherwise you will need to parse the default output file `data.json` for results
  - (*RECOMMENDED*) Use raw reads due to the increased sensitivity (without loss of specificity) and the additional information gleaned from KMA output (specifically the depth metric). You also save time from having to assemble the genome first. [CITATION NEEDED, PROBABLY THE KMA PAPER]
- Querying reads:
  - This will run SerotypeFinder with `kma` (instead of ncbi-blast+)
  - Only one of the PE read files is necessary. There is likely little benefit to using both R1 and R2. It will take slightly longer to run (a few extra seconds) if you use both R1 and R2 files.
- Querying assemblies:
  - This will run SerotypeFinder with `ncbi-blast+`
  - SerotypeFinder does not clean up after itself. `tmp/out_H_type.xml` and `tmp/out_O_type.xml` will exist in the specified output directory

## Example Usage: Docker

```bash
# download the image
$ docker pull staphb/serotypefinder:latest

# input files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads, mount PWD to /data inside container (broken into two lines for readabilty)
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/serotypefinder:latest \
    serotypefinder.py -i /data/E-coli.R1.fastq.gz /data/E-coli.R2.fastq.gz -o /data/output-dir-reads

# query assembly
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/serotypefinder:latest \
    serotypefinder.py -i /data/E-coli.skesa.fasta  -o /data/output-dir-asm
```

## Example Usage: Singularity

```bash
# download the image
$ singularity build serotypefinder.latest.sif docker://staphb/serotypefinder:latest

# files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads; mount PWD to /data inside container
$ singularity exec --no-home -B $PWD:/data serotypefinder.latest.sif \
    serotypefinder.py -i /data/E-coli.R1.fastq.gz /data/E-coli.R2.fastq.gz -o /data/output-dir-reads

# assembly
$ singularity exec --no-home -B $PWD:/data serotypefinder.latest.sif \
    serotypefinder.py -i /data/E-coli.skesa.fasta  -o /data/output-dir-asm
```
