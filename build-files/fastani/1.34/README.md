# fastANI container

Main tool : [fastANI](https://github.com/ParBLiSS/FastANI)

Full documentation: https://github.com/ParBLiSS/FastANI

FastANI was developed for fast alignment-free computation of whole-genome Average Nucleotide Identity (ANI). ANI is defined as mean nucleotide identity of orthologous gene pairs shared between two microbial genomes.

This docker image contains no references.

## Example Usage

```bash
# query one genome against another genome
fastANI -t 8 -q bacterial-genome1.fasta -r bacterial-genome2.fasta -o fastANI.out.tsv

# query one genome against the 43 genomes in RGDv2 (requires a File Of FileNames as input)
fastANI -t 8 -q bacterial-genome.fasta --rl /RGDv2/FOFN-RGDv2.txt -o fastANI.RGDv2.out.tsv
```
