# kSNP4 container

Main tool: kSNP4 https://sourceforge.net/projects/ksnp/files/

Additional tools: None

Full documentation: https://sourceforge.net/projects/ksnp/files/kSNP4%20User%20Guide.pdf/download

Summary:

kSNP4 is a program that identifies the pan-genome SNPs in a set of genome sequences, and estimates
phylogenetic trees based upon those SNPs. Because there are many potential downstream applications of SNP
information, kSNP4 also provides output files that include a multiple alignment of all of the SNP positions and
files that provide information about the positions of each SNP in each genome and annotations. kSNP4 can
analyze both complete (finished) genomes and unfinished genomes in assembled contigs or raw, unassembled
reads. Finished and unfinished genomes can be analyzed together, and kSNP4 can automatically download
Genbank files of the finished genomes (and annotated genome assemblies) and incorporate the information in
those files into the SNP annotation. Core SNPs, those present in all of the genomes, can optionally be
analyzed separately to generate a multiple SNP alignment and trees based on only the core SNPs. kSNP4 also
can provide a separate analysis of those SNPS that occur in at least a user-determined fraction of the genomes.


# Example Usage

```bash
kSNP4 -in Eco100.in -k 21 -outdir Run1 -annotate annotatedGenomes
```
