# MLST

This image implements the assembly improvement and strain variation detection program [MLST](https://github.com/tseemann/mlst).
Documentation is available at https://github.com/tseemann/mlst. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get input data (a genome assembly)
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna

# Run program to scan a genome assembly against PubMLST
mlst NCTC13799.fna > mlst-results.tsv
```

## Example output

The on-screen output tells you what the program did:
```
This is mlst 2.19.0 running on linux with Perl 5.026001
Checking mlst dependencies:
Found 'blastn' => /ncbi-blast-2.9.0+/bin/blastn
Found 'any2fasta' => /usr/local/bin/any2fasta
Found blastn: 2.9.0+ (002009)
Excluding 2 schemes: abaumannii ecoli_2
Found exact allele match neisseria.gdh-148
Found exact allele match neisseria.aroE-67
Found exact allele match neisseria.pdhC-153
Found exact allele match neisseria.fumC-111
Found exact allele match neisseria.adk-39
Found exact allele match neisseria.pgm-133
Found exact allele match neisseria.abcZ-126
If you like MLST, you're absolutely going to love wgMLST!
Done.
```
View the results file from this command with:
```
cat mlst-results.tsv 
# NCTC13799.fna   neisseria       1580    abcZ(126)       adk(39) aroE(67)        fumC(111)       gdh(148)        pdhC(153)       pgm(133)
```