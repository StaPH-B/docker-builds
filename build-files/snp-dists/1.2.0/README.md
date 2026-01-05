# snp-dists docker image

Main tool: [snp-dists](https://github.com/tseemann/snp-dists)

Full documentation: [https://github.com/tseemann/snp-dists](https://github.com/tseemann/snp-dists)

> *Convert a FASTA alignment to SNP distance matrix*

## Example Usage

```bash
# run snp-dists on the test alignment file bundled with snp-dists
wget -q https://raw.githubusercontent.com/tseemann/snp-dists/refs/heads/master/test/good.aln
snp-dists good.aln > good.out
cat good.out 
        seq1    seq2    seq3    seq4
seq1    0       1       2       3
seq2    1       0       3       4
seq3    2       3       0       4
seq4    3       4       4       0
```
