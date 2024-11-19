# bowtie2 container
Main tool : [bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml)

Bowtie2 : Genome assembler using a reference and mapping

Additional tools:
- Samtools version 1.19

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
Better documentation can be found at [https://github.com/BenLangmead/bowtie2](https://github.com/BenLangmead/bowtie2)
