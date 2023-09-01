# longshot container

Main tool : [longshot](https://github.com/pjedge/longshot)

Full documentation: [https://github.com/artic-network/fieldbioinformatics](https://github.com/artic-network/fieldbioinformatics)

> Longshot is a variant calling tool for diploid genomes using long error prone reads such as Pacific Biosciences (PacBio) SMRT and Oxford Nanopore Technologies (ONT). It takes as input an aligned BAM/CRAM file and outputs a phased VCF file with variants and haplotype information. It can also genotype and phase input VCF files. It can output haplotype-separated BAM files that can be used for downstream analysis. Currently, it only calls single nucleotide variants (SNVs), but it can genotype indels if they are given in an input VCF.

## Example Usage

```bash
longshot --bam example_data/pacbio_reads_30x.bam --ref example_data/genome.fa --out example_data/longshot_output.vcf
```
