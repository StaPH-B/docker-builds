# dragonflye docker image

Main tool : [dragonflye](https://github.com/rpetit3/dragonflye)

> dragonflye: Assemble bacterial isolate genomes from Nanopore reads

## Example Usage

```bash
# download ONT FASTQs for testing
wget https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz

# run dragonflye using flye as the assembly algorithm
dragonflye --reads /test/ERR3772599.fastq.gz --prefix ERR3772599-nano.hq --cpus 0 --nopolish --outdir flyehq --gsize 300000 --assembler flye --nanohq
```
