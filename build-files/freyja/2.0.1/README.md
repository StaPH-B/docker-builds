# freyja container

Main tool & documentation: [freyja](https://github.com/andersen-lab/Freyja)

Freyja is a tool to recover relative lineage abundances from mixed samples from a sequencing dataset . The method uses lineage-determining mutational "barcodes" derived from the UShER global phylogenetic tree as a basis set to solve the constrained (unit sum, non-negative) de-mixing problem.

<details>

<summary>Additional tools installed via micromamba:</summary>

```
  Name                           Version       Build                    Channel    
─────────────────────────────────────────────────────────────────────────────────────

```
</details>

## freyja barcodes

This docker image was built on **2025-07-22** and the command `freyja update` is run as part of the build to retrieve the most up-to-date database. The barcode version included in this docker image is **`07_21_2025-00-46`** as reported by `freyja demix --version`

This image is rebuilt every week on Dockerhub and Quay.io with the tag ${freyja version}-${freyja database version}-${data image was deployed}.

## Example Usage

```bash
# run freyja variants to call variants from an aligned SC2 bam file
freyja variants [bamfile] --variants [variant outfile name] --depths [depths outfile name] --ref [reference.fa]

# run freyja demix to identify lineages based on called variants 
freyja demix [variants-file] [depth-file] --output [output-file]
```

Warning: `freyja update` does not work under all conditions. You may need to specify an output directory (`freyja update --outdir /path/to/outdir`) for which your user has write privileges, such as a mounted volume.
