# SKESA container

Main tool : [SKESA](https://github.com/ncbi/SKESA)

Additional tools:
- gfa_connector
- kmercounter

Full documentation: https://github.com/ncbi/SKESA

> SKESA is a de-novo sequence read assembler for microbial genomes.

# Example Usage

```
#  Assemble PE, interleaved reads
skesa --fastq /data/Ecoli-PE-interleaved.fastq.gz --use_paired_ends --cores 8 --contigs_out /data/Ecoli.skesa.contigs.fasta

# Example from SKESA readme, download K. pneumoniae reads from SRA and assemble
skesa --sra_run SRR1510963 --hash_count --contigs_out /data/SRR1510963_skesa.fasta

# example using PE reads
kesa --cores 8 --memory 24 --reads /data/SRR11306390.sra_1.fastq /data/SRR11306390.sra_2.fastq --hash_count --contigs_out /data/SRR11306390.skesa.contigs.fasta

# View full SKESA help options
skesa -h
```
