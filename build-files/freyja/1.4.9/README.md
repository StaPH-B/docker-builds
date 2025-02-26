# freyja container

Main tool & documentation: [freyja](https://github.com/andersen-lab/Freyja)

Freyja is a tool to recover relative lineage abundances from mixed SARS-CoV-2 samples from a sequencing dataset (BAM aligned to the Hu-1 reference). The method uses lineage-determining mutational "barcodes" derived from the UShER global phylogenetic tree as a basis set to solve the constrained (unit sum, non-negative) de-mixing problem.

## Additional tools

- biopython 1.82
- ivar 1.4.2
- mafft 7.520
- matplotlib-base 3.8.2
- pandas 2.1.4
- samtools 1.19
- scipy 1.11.4
- seaborn 0.12.2
- ucsc-fatovcf 448
- usher 0.6.3

## freyja barcodes

This docker image was built on **2024-02-13** and the command `freyja update` is run as part of the build to retrieve the most up-to-date barcode file `freyja/data/usher_barcodes.csv` file from Freyja's GitHub repo. The barcode version included in this docker image is **`12_29_2023-00-41`** as reported by `freyja demix --version`

This image is rebuilt every day on Dockerhub with the tag ${freyja version}-${freyja database version}-${data image was deployed}.

## Example Usage

```bash
# run freyja variants to call variants from an aligned SC2 bam file
freyja variants [bamfile] --variants [variant outfile name] --depths [depths outfile name] --ref [reference.fa]

# run freyja demix to identify lineages based on called variants 
freyja demix [variants-file] [depth-file] --output [output-file]
```

Warning: `freyja update` does not work under all conditions. You may need to specify an output directory (`freyja update --outdir /path/to/outdir`) for which your user has write priveleges, such as a mounted volume.
