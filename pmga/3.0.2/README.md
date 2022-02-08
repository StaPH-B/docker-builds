# pmga v3.0.2

Main tool: [pmga](https://github.com/rpetit3/pmga)

In addition to `pmga`, this docker image contains the required databases built by `pmga-build`. The pre-built databases are located in `/pmga/blastdb`.

## Example commands

```{bash}
# Test H. influenzae genome
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data pmga:latest pmga /data/GCF_900478275.fna --blast /pmga/blastdb

# Force H. influenzae genome (via --species)
docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data pmga:latest pmga /data/GCF_900478275.fna --blast /pmga/blastdb --species hinfluenzae
```

View full pmga help options: `docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data pmga:latest pmga --help `
