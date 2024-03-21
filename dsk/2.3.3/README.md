# DSK

This image implements the k-mer counting software [DSK](https://gatb.inria.fr/software/dsk/).
Documentation is available at https://github.com/GATB/dsk. 

## Example usage

```bash
# Count k-mers
dsk \
  -nb-cores 4 \
  -file my_assembly.fasta \
  -kmer-size 7 \
  -out my_assembly_7mers.h5

# Export k-mers in tab-delimited format
dsk2ascii \
  -file my_assembly_7mers.h5 \
  -out my_assembly_7mers.txt
```

## Example output 

The output looks like this:
```
AAAAAAA 10681
AAAAAAC 5286
AAAAAAT 11051
AAAAAAG 6523
AAAAACA 3994
AAAAACC 2610
AAAAACT 4378
```
