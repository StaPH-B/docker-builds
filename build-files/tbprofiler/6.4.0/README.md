# TBProfiler Container

Main tool: [TBProfiler](https://github.com/jodyphelan/TBProfiler)

The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database. It also predicts the number of reads supporting drug resistance variants as an insight into hetero-resistance.

## Database

This tool relies on a database to run. The version (AKA git commit hash) of the database that is included in the docker image is `2c92475`. This is from the GitHub repository https://github.com/jodyphelan/tbdb. This can be confirmed in the json file: `/opt/conda/share/tbprofiler/tbdb.variables.json`:

```bash
$ grep 'commit' /opt/conda/share/tbprofiler/tbdb.variables.json
{"db-schema-version": "1.0.0", "snpEff_db": "Mycobacterium_tuberculosis_h37rv", "drugs": ["rifampicin", "isoniazid", "ethambutol", "pyrazinamide", "moxifloxacin", "levofloxacin", "bedaquiline", "delamanid", "pretomanid", "linezolid", "streptomycin", "amikacin", "kanamycin", "capreomycin", "clofazimine", "ethionamide", "para-aminosalicylic_acid", "cycloserine"], "tb-profiler-version": ">=6.0.0,<7.0.0", "version": {"name": "tbdb", "commit": "2c92475", "Merge": "8918884 2a51937", "Author": "Jody Phelan <jody.phelan@lshtm.ac.uk>", "Date": "Mon Oct 7 17:06:42 2024 +0100", "db-schema-version": "1.0.0"}, "amplicon": false, "files": {"ref": "tbdb.fasta", "gff": "tbdb.gff", "bed": "tbdb.bed", "json_db": "tbdb.dr.json", "variables": "tbdb.variables.json", "spoligotype_spacers": "tbdb.spoligotype_spacers.txt", "spoligotype_annotations": "tbdb.spoligotype_list.csv", "bedmask": "tbdb.mask.bed", "barcode": "tbdb.barcode.bed", "rules": "tbdb.rules.txt"}}
```

Additionally you can run the command `tb-profiler list_db` to list the same information

```bash
$ tb-profiler list_db
tbdb    2c92475 Jody Phelan <jody.phelan@lshtm.ac.uk>   Mon Oct 7 17:06:42 2024 +0100   /opt/conda/share/tbprofiler/tbdb
```

## Additional included tools/dependencies

- bedtools 2.31.1
- gatk4 4.6.1.0
- kmc 3.2.4
- pathogen-profiler 4.5.0
- perl 5.32.1
- python 3.12.3
- trimmomatic 0.39
- bwa 0.7.18
- minimap2 2.28
- samtools 1.21
- bcftools 1.21
- freebayes 1.3.6
- tqdm 4.66.6
- parallel 20240922
- samclip 0.4.0
- snpeff 5.2
- delly 1.2.6 (the more recent version 1.3.1 did not allow for the conda environment to resolve. More info here: https://github.com/jodyphelan/TBProfiler/issues/393#issuecomment-2452076859)

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
