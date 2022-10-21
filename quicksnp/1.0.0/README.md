# QuickSNP
A python script to quickly build a Neighbor Joining tree using only a SNP distance matrix.

This image implements Kelsey Florek's [QuickSNP](https://github.com/k-florek/QuickSNP).

```
usage: QuickSNP <dm> <outtree>

QuickSNP builds a NJ tree from a SNP distance matrix.

positional arguments:
  dm          SNP distance matrix CSV/TSV file with column headers and row names in square format.
  outtree     File name for Newick format tree.

optional arguments:
  -h, --help  show this help message and exit
```

### Python Dependencies:
- pandas==1.4.3 
- numpy==1.22.4
- scikit-bio==0.5.7
- scipy==1.8.0