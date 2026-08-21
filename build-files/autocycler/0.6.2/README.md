# autocycler container

Main tool: [autocycler](https://github.com/rrwick/Autocycler/)
  
Code repository: https://github.com/rrwick/Autocycler/

Basic information on how to use this tool:
- executable: autocycler
- help: --help
- version: --version
- description: |
> Autocycler is a tool for generating consensus long-read assemblies for bacterial genomes.

Additional information:

This image does not contain any of the assemblers listed in the wikis or tutorials. All helper scripts should be in path and are located at /usr/local/bin.
  
Full documentation: [https://github.com/rrwick/Autocycler/wiki](https://github.com/rrwick/Autocycler/wiki)

## Example Usage

```bash
reads=ont.fastq.gz  # your read set goes here
threads=16  # set as appropriate for your system
genome_size=$(genome_size_raven.sh "$reads" "$threads")  # can set this manually if you know the value

# Step 1: subsample the long-read set into multiple files
autocycler subsample --reads "$reads" --out_dir subsampled_reads --genome_size "$genome_size"

# Step 2: assemble each subsampled fastq file using different container

# Optional step: remove the subsampled reads to save space
rm subsampled_reads/*.fastq

# Step 3: compress the input assemblies into a unitig graph
autocycler compress -i assemblies -a autocycler_out

# Step 4: cluster the input contigs into putative genomic sequences
autocycler cluster -a autocycler_out

# Steps 5 and 6: trim and resolve each QC-pass cluster
for c in autocycler_out/clustering/qc_pass/cluster_*; do
    autocycler trim -c "$c"
    autocycler resolve -c "$c"
done

# Step 7: combine resolved clusters into a final assembly
autocycler combine -a autocycler_out -i autocycler_out/clustering/qc_pass/cluster_*/5_final.gfa
```