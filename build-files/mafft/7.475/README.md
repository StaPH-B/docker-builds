# MAFFT container

Main tool : [MAFFT](https://mafft.cbrc.jp/alignment/software/)

MAFFT is a multiple sequence alignment program for unix-like operating systems..

# Example Usage

```
# have mafft detect what to do
mafft --auto input > output
# filter out sequences with too many ambiguous values with --maxambiguous (only available in version greater than 7.473) and compare to reference
mafft --auto --maxambiguous 0.05 --addfragments othersequences referencesequence > output
```

## Other noteworthy options include
```
--thread # allows parallelization
--large # reduces memory burden
```
