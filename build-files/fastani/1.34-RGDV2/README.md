# fastANI container

Main tool : [fastANI](https://github.com/ParBLiSS/FastANI)

Full documentation: https://github.com/ParBLiSS/FastANI

FastANI was developed for fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI). ANI is defined as mean nucleotide identity of orthologous gene pairs shared between two microbial genomes.

This docker image contains the Reference Genome Database version 2 (RGDv2) from the Enteric Diseases Laboratory Branch at the CDC. It contains the genomes of 43 enteric bacterial isolates that are used to for species identification of bacterial isolate WGS data. This database is NOT meant to be comprehensive - it contains the genomes of enteric pathogens commonly sequenced by EDLB and some closely related species. Here is the publication describing the database: [https://doi.org/10.3389/fmicb.2023.1225207](https://doi.org/10.3389/fmicb.2023.1225207)

The FASTA files for RGDv2 can be found within `/RGDv2/` inside the docker image.

## Example Usage

```bash
# query one genome against another genome
fastANI -t 8 -q bacterial-genome1.fasta -r bacterial-genome2.fasta -o fastANI.out.tsv

# query one genome against the 43 genomes in RGDv2 (requires a File Of FileNames as input)
fastANI -t 8 -q bacterial-genome.fasta --rl /RGDv2/FOFN-RGDv2.txt -o fastANI.RGDv2.out.tsv
```
