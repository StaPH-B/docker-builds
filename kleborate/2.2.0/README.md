# Kleborate container

Main tool : [Kleborate](https://github.com/katholt/Kleborate) 2.2.0

Additional tools:

- [kaptive](https://github.com/katholt/Kaptive) 2.0.3
- ncbi-blast+ 2.9.0
- [mash](https://github.com/marbl/Mash) 2.3
- python 3.8.2

Full documentation: [https://github.com/katholt/Kleborate/wiki](https://github.com/katholt/Kleborate/wiki)

Kleborate is a tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC) for:

- MLST sequence type
- species (e.g. K. pneumoniae, K. quasipneumoniae, K. variicola, etc.)
- ICEKp associated virulence loci: yersiniabactin (ybt), colibactin (clb), salmochelin (iro), hypermucoidy (rmpA)
- virulence plasmid associated loci: salmochelin (iro), aerobactin (iuc), hypermucoidy (rmpA, rmpA2)
- antimicrobial resistance determinants: acquired genes, SNPs, gene truncations and intrinsic β-lactamases
- K (capsule) and O antigen (LPS) serotype prediction, via wzi alleles and Kaptive

## Example Usage

```bash
# run Kleborate on assembly supplied with Kleborate code
kleborate --resistance --kaptive --all \
        --assemblies /Kleborate/test/test_genomes/172.fasta.gz \
        --outfile /data/strain172-kleborate-test-out.tsv
```
