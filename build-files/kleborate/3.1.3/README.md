# Kleborate container

Main tool : [Kleborate](https://github.com/katholt/Kleborate)

:warning: **Note:** Kleborate v3 is different from v2, please see here for the differences: https://kleborate.readthedocs.io/en/latest/index.html#changes-from-v2

Additional tools:

- [mash](https://github.com/marbl/Mash) version 2.3
- [minimap2](https://github.com/lh3/minimap2) version 2.28
- [kaptive](https://github.com/klebgenomics/Kaptive) version 3.0.0b6
- biopython 1.84
- dna-features-viewer 3.1.3
- matplotlib 3.9.2
- numpy 2.1.3

Full documentation: [https://github.com/katholt/Kleborate/wiki](https://github.com/katholt/Kleborate/wiki)

Description:
> Kleborate is a tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC) for:
> 
> - MLST sequence type
> - species (e.g. K. pneumoniae, K. quasipneumoniae, K. variicola, etc.)
> - ICEKp associated virulence loci: yersiniabactin (ybt), colibactin (clb), salmochelin (iro), hypermucoidy (rmpA)
> - virulence plasmid associated loci: salmochelin (iro), aerobactin (iuc), hypermucoidy (rmpA, rmpA2)
> - antimicrobial resistance determinants: acquired genes, SNPs, gene truncations and intrinsic β-lactamases
> - K (capsule) and O antigen (LPS) serotype prediction, via wzi alleles and Kaptive

## Included models

Kleborate has models for both Klebsiella and Escherichia species. The available presets and models are listed below.

Available presets: kpsc, kosc, escherichia

```
Available modules for Kleborate
-------------------------------
enterobacterales__species: Mash-based species detection for enterobacterales species

escherichia__mlst_achtman: chromosomal MLST for Escherichia coli using the Achtman scheme

escherichia__mlst_pasteur: chromosomal MLST for Escherichia coli using the Pasteur scheme

general__contig_stats: basic stats on the assembly's contigs

klebsiella__abst: MLST on the KpSC aerobactin locus (iuc genes)

klebsiella__cbst: MLST on the KpSC colibactin locus (clb genes)

klebsiella__rmpa2: typing for the rmpA2 gene

klebsiella__rmst: MLST on the KpSC Rmp locus (rmp genes)

klebsiella__smst: MLST on the KpSC salmochelin locus (iro genes)

klebsiella__ybst: MLST on the KpSC yersiniabactin locus (ybt and irp genes)

klebsiella_oxytoca_complex__mlst: chromosomal MLST for the Klebsiella oxytoca species complex

klebsiella_pneumo_complex__amr: Genotyping acquired genes and mutations for the Klebsiella pneumoniae species complex

klebsiella_pneumo_complex__kaptive: In silico serotyping of K and L locus for the Klebsiella pneumoniae species complex

klebsiella_pneumo_complex__mlst: chromosomal MLST for the Klebsiella pneumoniae species complex

klebsiella_pneumo_complex__resistance_class_count: Resistance gene classes count, excluding the Bla_chr class which is intrinsicresults of the
klebsiella_pneumo_complex__amr module

klebsiella_pneumo_complex__resistance_gene_count: Resistance genes counts, excluding the Bla class which is intrinsicresults of the
klebsiella_pneumo_complex__amr module

klebsiella_pneumo_complex__resistance_score: resistance score (0-3) for the Klebsiella pneumoniae species complex, based on the results of the
klebsiella_pneumo_complex__amr module

klebsiella_pneumo_complex__virulence_score: virulence score (0-5) for the Klebsiella pneumoniae species complex, based on the results of the abst, cbst
and ybst modules

klebsiella_pneumo_complex__wzi: WZI typing for K antigen prediction
```

## Example Usage

```bash
kleborate -a sample.fasta -o outdir -p preset
```
