# trycycler container

Main tool : [trycycler](https://github.com/rrwick/Trycycler)

The container also contains :
- [miniasm](https://github.com/lh3/miniasm)
- [minimap2](https://github.com/lh3/minimap2)
- [muscle](https://www.ebi.ac.uk/Tools/msa/muscle/)
- [mash](https://github.com/marbl/Mash)
- R package ['ape'](https://cran.r-project.org/web/packages/ape/index.html)
- R package ['phangorn'](https://cran.r-project.org/web/packages/phangorn/index.html)

Trycycler "tries" different assemblies to find the one most supported by long reads.

# Example Usage

```
trycycler subsample --reads reads.fastq --out_dir read_subsets
```
```
trycycler cluster --assemblies assemblies/*.fasta --reads reads.fastq --out_dir trycycler
```
```
trycycler reconcile --reads reads.fastq --cluster_dir trycycler/cluster_001
```
```
trycycler consensus --cluster_dir trycycler/cluster_001
```

It is highly recommended to read Trycycler's [wiki](https://github.com/rrwick/Trycycler/wiki) for full usability and reasoning.
