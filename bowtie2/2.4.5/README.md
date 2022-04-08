# bowtie2 container
Main tool : [bowtie2](https://github.com/BenLangmead/bowtie2)

Additional tools:
- [samtools](https://www.htslib.org/)

Full documentation: http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml

> Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes. 

# Example Usage

```
bowtie2-build lambda_virus.fa /index/lambda_virus
```
```
bowtie2 -x /index/lambda_virus -U longreads.fq
```
```
bowtie2-inspect --summary /index/lambda_virus
```
```
samtools ampliconclip -b bed.file input.bam
```
```
samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam
```
