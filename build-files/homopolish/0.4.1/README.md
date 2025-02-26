# homopolish container

Main tool: [homopolish](https://github.com/ythuang0522/homopolish)

Full Documentation: https://github.com/ythuang0522/homopolish/blob/master/README.md

Homopolish is a genome polisher originally developed for Nanopore and subsequently extended for PacBio CLR. It generates a high-quality genome (>Q50) for virus, bacteria, and fungus. Nanopore/PacBio systematic errors are corrected by retreiving homologs from closely-related genomes and polished by an SVM. When paired with Racon and Medaka, the genome quality can reach Q50-90 (>99.999%) on Nanopore R9.4/10.3 flowcells (Guppy >3.4). For PacBio CLR, Homopolish also improves the majority of Flye-assembled genomes to Q90 (see Accuracy).

# Example Usage

``` bash
homopolish polish -a yourgenome.fasta -s bacteria.msh -m R9.4.pkl -o youroutput

homopolish polish -a yourgenome.fasta -l path_to_your_genomes.fasta -m R9.4.pkl -o youroutput
```
