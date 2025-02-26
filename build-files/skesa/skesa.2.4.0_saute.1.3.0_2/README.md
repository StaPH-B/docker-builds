# skesa container

Strategic K-mer Extension for Scrupulous Assemblies

Main tool: [skesa](https://github.com/ncbi/SKESA)

Included tools and their respective versions:
- skesa: 2.5.1
- saute: 1.3.0
- saute_prot: 1.3.0
- gfa_connector: 1.1.1
- kmercounter: 2.1.1

Code repository: https://github.com/ncbi/SKESA

Basic information on how to use this tool:
- executable: skesa
- help: -h
- version: -v
- description: Short read assembly
  
Full documentation: https://github.com/ncbi/SKESA

## Example Usage

```bash
##  Assemble PE, interleaved reads in your $PWD
skesa --fastq /data/Ecoli-PE-interleaved.fastq.gz --use_paired_ends --cores 8 --contigs_out /data/Ecoli.skesa.contigs.fasta

## Example from SKESA readme, download K. pneumoniae reads from SRA and assemble
skesa --sra_run SRR1510963 --hash_count --contigs_out /data/SRR1510963_skesa.fasta

## example using PE reads that are in your PWD
skesa --cores 8 --memory 24 --reads /data/SRR11306390.sra_1.fastq /data/SRR11306390.sra_2.fastq --hash_count --contigs_out /data/SRR11306390.skesa.contigs.fasta
```
