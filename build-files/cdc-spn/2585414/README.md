# cdc-spn container

Main tool: [SPN_Serotyper.pl](https://github.com/BenJamesMetcalf/Spn_Scripts_Reference)

Code repository: [https://github.com/BenJamesMetcalf/Spn_Scripts_Reference](https://github.com/BenJamesMetcalf/Spn_Scripts_Reference)

Additional tools:
- samtools: 0.1.18 (via conda, used by srst2)
- samtools: 1.19 (available as `samtools-1.19`)
- srst2: 0.2.0
- bowtie2: 2.5.1
- freebayes: 1.3.6
- ncbi-blast+: 2.14.0
- bedtools: 2.31.0
- prodigal: 2.6.3

Basic information on how to use this tool:
- executable: `SPN_Serotyper.pl`
- help: run with no arguments
- description: Types *Streptococcus pneumoniae* isolates from paired-end Illumina reads, calling serotype and pilus island using srst2 and freebayes against a curated reference database

Additional information:  
Container includes the full `SPN_Reference_DB` from the Spn_Scripts_Reference repository (commit 2585414), which contains pre-built bowtie2 indexes and FASTA databases for serotyping, resistance typing, and MLST. The reference database is located at `/Spn_Scripts_Reference/SPN_Reference_DB/`.

Full documentation: [https://github.com/BenJamesMetcalf/Spn_Scripts_Reference](https://github.com/BenJamesMetcalf/Spn_Scripts_Reference)

## Example Usage
```bash
SPN_Serotyper.pl \
  -1 sample_R1.fastq \
  -2 sample_R2.fastq \
  -r /Spn_Scripts_Reference/SPN_Reference_DB/SPN_Sero_Gene-DB_Final.fasta \
  -o output_dir \
  -n sample_name
```
