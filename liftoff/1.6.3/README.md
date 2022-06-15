# Liftoff Container
Main tool: [Liftoff](https://github.com/agshumate/Liftoff)

Liftoff is a tool that accurately maps annotations in GFF or GTF between assemblies of the same, or closely-related species.

# Example Usage
```{bash}
liftoff -g GCA_000146045.2_R64_genomic.gff.gz -o GCA_000146045.2_R64_to_GCA_000146045.2_advanced.gff3 -u unmapped_features_GCA_000146045.2_R64_advanced.txt -dir sandbox -chroms chroms.txt -unplaced unplaced.txt -copies GCA_000146045.2_R64_genomic.fna.gz
```

Better documentation can be found at [Liftoff](https://github.com/agshumate/Liftoff)
