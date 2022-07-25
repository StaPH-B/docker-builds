# GAMMA Container

## Documentation and Overview

Main Tool: [GAMMA: a tool for the rapid identification, classification and annotation of translated gene matches from sequencing data](https://academic.oup.com/bioinformatics/article/38/2/546/6355578)

Full documentation: [GAMMA Github](https://github.com/rastanton/GAMMA) 

GAMMA (Gene Allele Mutation Microbial Assessment) is a command line tool that finds gene matches in microbial genomic data using protein coding (rather than nucleotide) identity, and then translates and annotates the match by providing the type (i.e., mutant, truncation, etc.) and a translated description (i.e., Y190S mutant, truncation at residue 110, etc.). Because microbial gene families often have multiple alleles and existing databases are rarely exhaustive, GAMMA is helpful in both identifying and explaining how unique alleles differ from their closest known matches.

## Usage

Basic usage for GAMMA:
```
usage: GAMMA.py [-h] [-a] [-e] [-f] [-g] [-n] [-l] [-i PERCENT_IDENTITY]
                input_fasta database output

This scripts makes annotated gene calls from matches in an assembly using a
gene database

positional arguments:
  input_fasta           input fasta
  database              input database
  output                output name

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             include all gene matches, even overlaps
  -e, --extended        writes out all protein mutations
  -f, --fasta           write fasta of gene matches
  -g, --gff             write gene matches as gff file
  -n, --name            writes name in front of each gene match line
  -l, --headless        removes the header from the output gamma file
  -i PERCENT_IDENTITY, --percent_identity PERCENT_IDENTITY
                        minimum nucleotide identity for blat search (default = 90)
```

Basic usage for GAMMA-S:
```
usage: GAMMA-S.py [-h] [-a] [-e] [-p] [-m MINIMUM] [-i PERCENT_IDENTITY]
                  input_fasta database output

This scripts makes sequence (nucleotide or protein) match calls from matches
in an assembly using a sequence database

positional arguments:
  input_fasta           input fasta
  database              input database
  output                output name

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             include all gene matches, even overlaps
  -e, --extended        writes out all protein mutations
  -p, --protein         for protein-protein comparisons
  -m MINIMUM, --minimum MINIMUM
                        minimum length percent match for output (default = 20)
  -i PERCENT_IDENTITY, --percent_identity PERCENT_IDENTITY
                        minimum nucleotide identity for blat search (default = 90)
```

Example usage:
```
GAMMA-S.py GCF_008632635.1_ASM863263v1_genomic.fna db.fasta GCF_008632635.1
```

