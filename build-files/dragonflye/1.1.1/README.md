# dragonflye docker image

Main tool : [dragonflye v1.1.1](https://github.com/rpetit3/dragonflye)

> dragonflye: Assemble bacterial isolate genomes from Nanopore reads

## Additional tools

Protip: run command `docker run staphb/dragonflye:latest micromamba list` to see full micromamba environment:

- [any2fasta 0.4.2](https://github.com/tseemann/any2fasta)
- [assembly-scan 0.4.1](https://github.com/rpetit3/assembly-scan)
- [bwa 0.7.17-r1188](https://github.com/lh3/bwa)
- [bcftools 1.15.1](https://github.com/samtools/bcftools)
- biopython 1.80
- [fastp 0.23.2](https://github.com/OpenGene/fastp)
- [flye 2.9.1](https://github.com/fenderglass/Flye)
- [kmc 3.2.1](https://github.com/refresh-bio/KMC)
- [medaka 1.6.1](https://github.com/nanoporetech/medaka)
- [miniasm 0.3](https://github.com/lh3/miniasm)
- [minimap2 2.24-r1122](https://github.com/lh3/minimap2)
- [nanoq 0.9.0](https://github.com/esteinig/nanoq)
- perl 5.32.1
- [pigz 2.6](https://zlib.net/pigz/)
- [polypolish 0.5.0](https://github.com/rrwick/Polypolish)
- [porechop 0.2.4](https://github.com/rrwick/Porechop)
- python 3.8.15
- [racon 1.5.0](https://github.com/lbcb-sci/racon)
- [rasusa 0.7.0](https://github.com/mbhall88/rasusa)
- [raven 1.8.1](https://github.com/lbcb-sci/raven)
- [samclip 0.4.0](https://github.com/tseemann/samclip)
- [samtools 1.15.1](https://github.com/samtools/samtools)
- [seqtk 1.3-r106](https://github.com/lh3/seqtk)

## Example Usage

```bash
# download ONT FASTQs for testing
wget https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz

# run dragonflye using flye as the assembly algorithm
dragonflye --reads /test/ERR3772599.fastq.gz --prefix ERR3772599-nano.hq --cpus 0 --nopolish --outdir flyehq --gsize 300000 --assembler flye --nanohq
```
