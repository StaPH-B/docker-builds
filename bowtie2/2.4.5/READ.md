bowtie2 container
Main tool : bowtie2

Required tool : samtools

Bowtie2 : Genome assembler using a reference and mapping

Samtools: a set of tools for interacting with and reformatting sequence data

Example Usage
bowtie2-build lambda_virus.fa /index/lambda_virus
bowtie2 -x /index/lambda_virus -U longreads.fq
bowtie2-inspect --summary /index/lambda_virus
samtools ampliconclip -b bed.file input.bam
samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam
Better documentation can be found at https://github.com/BenLangmead/bowtie2
