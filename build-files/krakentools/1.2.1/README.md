# KrakenTools container

Main tool [KrakenTools](https://github.com/jenniferlu717/KrakenTools)

Code repository: https://github.com/jenniferlu717/KrakenTools

Additional tools:

- python 3.10.12
- biopython 1.84
- pandas 2.2.3
- numpy 2.1.2

Basic information on how to use this tool:

- executable: various python scripts
- help: most scripts have -h options
- version: most scripts do not have versioning information
- description: "KrakenTools is a suite of scripts to be used alongside the Kraken, KrakenUniq, Kraken 2, or Bracken programs. These scripts are designed to help Kraken users with downstream analysis of Kraken results."

Additional information:

Full documentation: [https://github.com/jenniferlu717/KrakenTools](https://github.com/jenniferlu717/KrakenTools)

Current available python scripts
```
combine_kreports.py
combine_mpa.py
extract_kraken_reads.py
filter_bracken.out.py
fix_unmapped.py
kreport2krona.py
kreport2mpa.py
make_kreport.py
make_ktaxonomy.py
```

## Example Usage

```bash
extract_kraken_reads.py \
    -k classifiedreads.txt \
    -r kraken2_report.txt \
    -s1 cseqs_1.fq \
    -s2 cseqs_2.fq \
    -t 2697049 \
    --fastq-output \
    -o extracted_1.fq \
    -o2 extracted_2.fq

# note that krona is not included here
kreport2krona.py -r kraken2_report.txt -o krona.txt

kreport2mpa.py -r kraken2_report.txt -o mpa.txt

combine_kreports.py \
    -r kraken2_report.txt kraken2_report.txt \
    -o combined.txt
```
