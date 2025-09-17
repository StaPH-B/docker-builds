# trycycler container

Main tool: [trycycler](https://github.com/rrwick/Trycycler)

Additional tools:

- [miniasm](https://github.com/lh3/miniasm) 0.3-r179
- [minimap2](https://github.com/lh3/minimap2) 2.24-r1122
- [muscle](https://www.ebi.ac.uk/Tools/msa/muscle/) 3.8.1551 (recommended version)
- [mash](https://github.com/marbl/Mash) 2.3
- R package ['ape'](https://cran.r-project.org/web/packages/ape/index.html) 5.7
- R package ['phangorn'](https://cran.r-project.org/web/packages/phangorn/index.html) 2.11.1

Trycycler "tries" different assemblies to find the one most supported by long reads.

## Example Usage

```bash
trycycler subsample --reads reads.fastq --out_dir read_subsets
```

```bash
trycycler cluster --assemblies assemblies/*.fasta --reads reads.fastq --out_dir trycycler
```

```bash
trycycler reconcile --reads reads.fastq --cluster_dir trycycler/cluster_001
```

```bash
trycycler consensus --cluster_dir trycycler/cluster_001
```

It is highly recommended to read Trycycler's [wiki](https://github.com/rrwick/Trycycler/wiki) for full usability and reasoning.
