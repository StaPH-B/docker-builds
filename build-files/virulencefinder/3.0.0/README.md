# VirulenceFinder 3.0.0 Docker Image

A docker image  that contains VirulenceFinder, a tool for identifying virulence factors in E. coli, Enterococcus, S. aureus, and Listeria isolates from reads or assemblies

[Link to StaPH-B DockerHub repository](https://hub.docker.com/r/staphb/virulencefinder)

Main tool:

- Main Code Repo: [https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/](https://bitbucket.org/genomicepidemiology/virulencefinder/src/master/)
- VirulenceFinder database: [https://bitbucket.org/genomicepidemiology/virulencefinder_db/src/master/](https://bitbucket.org/genomicepidemiology/virulencefinder_db/src/master/)
- You may be familiar with the web version of VirulenceFinder: [https://cge.food.dtu.dk/services/VirulenceFinder/](https://cge.food.dtu.dk/services/VirulenceFinder/)

Additional tools:

- python 3.10.12
- cgecore 1.5.6
- biopython 1.84
- numpy 2.1.3
- pandas 2.2.3
- tabulate 0.9.0
- [kma](https://bitbucket.org/genomicepidemiology/kma/src/master/) 1.4.15
- ncbi-blast+ 2.12.0

Database version:

VirulenceFinder database version: tag 2.0.0 made on 2024-05-29. [Link to commit history](https://bitbucket.org/genomicepidemiology/virulencefinder_db/downloads/?tab=tags)

## Usage

```bash
$ virulencefinder.py -h
usage: __main__.py [-h] [-ifa INPUTFASTA [INPUTFASTA ...]] [-ifq INPUTFASTQ [INPUTFASTQ ...]] [--nanopore] [-o OUTPUTPATH] [-tmp TMP_DIR] [-b BLASTPATH] [-k KMAPATH] [-p DB_PATH] [-d DATABASES] [-l MIN_COV]
                   [-t THRESHOLD] [-x] [--speciesinfo_json SPECIESINFO_JSON] [-db_vir_kma DB_PATH_VIR_KMA] [-q] [-j OUT_JSON] [-v] [--overlap OVERLAP]

options:
  -h, --help            show this help message and exit
  -ifa INPUTFASTA [INPUTFASTA ...], --inputfasta INPUTFASTA [INPUTFASTA ...]
                        FASTA or FASTQ input files.
  -ifq INPUTFASTQ [INPUTFASTQ ...], --inputfastq INPUTFASTQ [INPUTFASTQ ...]
                        Input fastq file(s). Assumed to be single-end fastq if only one file is provided, and assumed to be paired-end data if two files are provided.
  --nanopore            If nanopore data is used
  -o OUTPUTPATH, --outputPath OUTPUTPATH
                        Path to blast output
  -tmp TMP_DIR, --tmp_dir TMP_DIR
                        Temporary directory for storage of the results from the external software. Defaults to 'tmp' dir in the given output dir.
  -b BLASTPATH, --blastPath BLASTPATH
                        Path to blastn
  -k KMAPATH, --kmaPath KMAPATH
                        Path to KMA
  -p DB_PATH, --databasePath DB_PATH
                        Path to the databases
  -d DATABASES, --databases DATABASES
                        Databases chosen to search in - if non or all is specified all is used
  -l MIN_COV, --mincov MIN_COV
                        Minimum coverage
  -t THRESHOLD, --threshold THRESHOLD
                        Minimum hreshold for identity
  -x, --extented_output
                        Give extented output with allignment files, template and query hits in fasta and a tab seperated file with gene profile results
  --speciesinfo_json SPECIESINFO_JSON
                        Argument used by the cge pipeline. It takes a list in json format consisting of taxonomy, from domain -> species. A database is chosen based on the taxonomy.
  -db_vir_kma DB_PATH_VIR_KMA, --db_path_vir_kma DB_PATH_VIR_KMA
                        Path to the virulencefinder databases indexed with KMA. Defaults to the value of the --db_res flag.
  -q, --quiet
  -j OUT_JSON, --out_json OUT_JSON
                        Specify JSON filename and output directory. If the directory doesn't exist, it will be created.
  -v, --version         Version of Virulencefinder
  --overlap OVERLAP     Genes are allowed to overlap this number ofnucleotides.
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
$ docker pull staphb/virulencefinder:latest

# input files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads, mount PWD to /data inside container (broken into two lines for readabilty)
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/virulencefinder:latest \
    virulencefinder.py -ifq /data/E-coli.R1.fastq.gz -o /data/output-dir-reads -x

# query assembly
$ docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/virulencefinder:latest \
    virulencefinder.py -ifa /data/E-coli.skesa.fasta  -o /data/output-dir-asm -x
```

## Example Usage: Singularity

```bash
# download the image
$ singularity build virulencefinder.latest.sif docker://staphb/virulencefinder:latest

# files are in my PWD
$ ls
E-coli.skesa.fasta  E-coli.R1.fastq.gz  E-coli.R2.fastq.gz

# make an output directory
$ mkdir output-dir-reads output-dir-asm

# query reads; mount PWD to /data inside container
$ singularity exec --no-home -B $PWD:/data virulencefinder.latest.sif \
    virulencefinder.py -ifq /data/E-coli.R1.fastq.gz /data/E-coli.R2.fastq.gz -o /data/output-dir-reads -x

# assembly
$ singularity exec --no-home -B $PWD:/data virulencefinder.latest.sif \
    virulencefinder.py -ifa /data/E-coli.skesa.fasta -o /data/output-dir-asm -x
```
