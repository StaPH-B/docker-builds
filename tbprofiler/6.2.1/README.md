# TBProfiler Container

Main tool: [TBProfiler](https://github.com/jodyphelan/TBProfiler)

The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database. It also predicts the number of reads supporting drug resistance variants as an insight into hetero-resistance.

## Database

This tool relies on a database to run. The version (AKA git commit hash) of the database that is included in the docker image is `97b5876`. This is from the GitHub repository https://github.com/jodyphelan/tbdb. This can be confirmed in the json file: `/opt/conda/share/tbprofiler/tbdb.version.json`:

```bash
$ grep 'commit' /opt/conda/share/tbprofiler/tbdb.version.json
{"name": "tbdb", "commit": "5f3c51e", "Merge": "b1a2549 abddb8e", "Author": "Jody Phelan <jody.phelan@lshtm.ac.uk>", "Date": "Thu Jan 19 10:47:32 2023 +0000"}
```

Additionally you can run the command `tb-profiler list_db` to list the same information

```bash
$ tb-profiler list_db
tbdb    97b5876 Jody Phelan <jody.phelan@lshtm.ac.uk>   Wed May 8 13:53:15 2024 +0100   /opt/conda/share/tbprofiler/tbdb
```

## Additional included tools/dependencies

- bedtools 2.31.1
- gatk4 4.5.0.0
- kmc 3.2.4
- pathogen-profiler 4.2.0
- perl 5.32.1
- python 3.10.14
- trimmomatic 0.39
- bwa 0.7.18
- minimap2 2.28
- samtools 1.20
- bcftools 1.20
- freebayes 1.3.6
- tqdm 4.66.4
- parallel 20240522
- samclip 0.4.0
- snpeff 5.2

## Example Usage

Run whole pipeline on Illumina paired-end reads:

```bash
tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 4 -p ERR1664619 --txt
```

Make alternative database:

```bash
tb-profiler create_db --prefix <new_library_name>
tb-profiler load_library --prefix <new_library_name>
```

## Updates
Release 5.0.1 implemented sqlite3 database locking with https://py-filelock.readthedocs.io/en/latest/index.html. This should fix issues using it over network filing systems (NFS). For more information, official documentation can be found [here.](https://jodyphelan.gitbook.io/tb-profiler/)
