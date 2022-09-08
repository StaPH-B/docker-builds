# GAMMA Container

## Documentation and Overview

Main Tool: [GAMMA: a tool for the rapid identification, classification and annotation of translated gene matches from sequencing data](https://academic.oup.com/bioinformatics/article/38/2/546/6355578)

Full documentation: [GAMMA Github](https://github.com/rastanton/GAMMA) 

GAMMA (Gene Allele Mutation Microbial Assessment) is a command line tool that finds gene matches in microbial genomic data using protein coding (rather than nucleotide) identity, and then translates and annotates the match by providing the type (i.e., mutant, truncation, etc.) and a translated description (i.e., Y190S mutant, truncation at residue 110, etc.). Because microbial gene families often have multiple alleles and existing databases are rarely exhaustive, GAMMA is helpful in both identifying and explaining how unique alleles differ from their closest known matches.

## Usage

Example usage:
```
# run GAMMA
GAMMA-S.py GCF_008632635.1_ASM863263v1_genomic.fna db.fasta GCF_008632635.1
```

