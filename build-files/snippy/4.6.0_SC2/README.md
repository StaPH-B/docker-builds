# Snippy docker image

> Snippy: Rapid haploid variant calling and core genome alignment

Main tool : [Snippy](https://github.com/tseemann/snippy)

Additional tools:
- perl 5.26.1
- bioperl 1.7.2
- hmmer
- python 2.7.17
- python3 3.6.9

## Example Usage
```bash
# paired end Illumina reads with reference genome in fasta format
$ snippy \
      --ref CVOW01.fasta \
      --R1 SRR1157476_1.fastq.gz \
      --R2 SRR1157476_2.fastq.gz \
      --cpus 2 \
      --outdir results

# Example of successful snippy run
[19:12:16] Creating extra output files: BED GFF CSV TXT HTML
[19:12:16] Identified 17 variants.
[19:12:16] Result folder: results
[19:12:16] Result files:
[19:12:16] * results/snps.aligned.fa
[19:12:16] * results/snps.bam
[19:12:16] * results/snps.bam.bai
[19:12:16] * results/snps.bed
[19:12:16] * results/snps.consensus.fa
[19:12:16] * results/snps.consensus.subs.fa
[19:12:16] * results/snps.csv
[19:12:16] * results/snps.filt.vcf
[19:12:16] * results/snps.gff
[19:12:16] * results/snps.html
[19:12:16] * results/snps.log
[19:12:16] * results/snps.raw.vcf
[19:12:16] * results/snps.subs.vcf
[19:12:16] * results/snps.tab
[19:12:16] * results/snps.txt
[19:12:16] * results/snps.vcf
[19:12:16] * results/snps.vcf.gz
[19:12:16] * results/snps.vcf.gz.csi
[19:12:16] Walltime used: 33 seconds
[19:12:16] Wishing you a life free of homopolymer errors.
[19:12:16] Done.

# snippy-core on multiple snippy results directories
$ snippy-core --prefix core results1 results2 results3 results4
```
