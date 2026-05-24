# LongQC container

Main tool: [LongQC](https://github.com/yfukasawa/LongQC)
  
Code repository: https://github.com/yfukasawa/LongQC

Additional tools:
- python: 3.9
- minimap2-coverage: 1.2.0c

Basic information on how to use this tool:
- executable: `longQC.py`, `longqc`, `LongQC`
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: A tool for the data quality control of the PacBio and ONT long reads, and it has two functionalities: sample QC and platform QC.

Additional information:

Publication: https://pmc.ncbi.nlm.nih.gov/articles/PMC7144081/

LongQC: A Quality Control Tool for Third Generation Sequencing Long Read Data.
Yoshinori Fukasawa, Luca Ermini, Hai Wang, Karen Carty, Ming-Sin Cheung.
G3: Genes, Genomes, Genetics, 10(4): 1193-1196, 2020

## Example Usage

For inpatient persons using RS-II:
```bash
python longQC.py sampleqc -x pb-rs2 -o out_dir input_reads.(fa,fq)
```
For Sequel:
```bash
python longQC.py sampleqc -x pb-sequel -o out_dir input_reads.bam
```
For ONT (1D ligation):
```bash
python longQC.py sampleqc -x ont-ligation -o out_dir input_reads.fq
```
For ONT (rapid):
```bash
python longQC.py sampleqc -x ont-rapid -o out_dir input_reads.fq
```