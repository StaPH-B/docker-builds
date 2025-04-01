# FreeBayes Container

## Documentation and Overview

Main Tool: FreeBayes - [Haplotype-based variant detection from short-read sequencing](https://arxiv.org/abs/1207.3907)

Full documentation: https://github.com/freebayes/freebayes 

FreeBayes is a haplotype-based variant detector and is a great tool for calling variants from a population.

FreeBayes is a Bayesian genetic variant detector designed to find small polymorphisms, specifically SNPs (single-nucleotide polymorphisms), indels (insertions and deletions), MNPs (multi-nucleotide polymorphisms), and complex events (composite insertion and substitution events) smaller than the length of a short-read sequencing alignment.

FreeBayes is haplotype-based, in the sense that it calls variants based on the literal sequences of reads aligned to a particular target, not their precise alignment. This model is a straightforward generalization of previous ones (e.g. PolyBayes, samtools, GATK) which detect or report variants based on alignments. This method avoids one of the core problems with alignment-based variant detection — that identical sequences may have multiple possible alignments:”

## Usage

Basic usage:
```
freebayes -f [REFERENCE] [OPTIONS] [BAM FILES] >[OUTPUT]
```
Example usage:
```
freebayes --bam Sample_1_sorted.bam --ploidy 1 --fasta-reference reference.fasta --vcf Sample1_freebayes.vcf
```

There are LOTS of options so use `freebayes --help` to get full list. 
