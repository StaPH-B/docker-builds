# autocycler container

Main tool: [autocycler](https://github.com/rrwick/Autocycler/)
  
Code repository: https://github.com/rrwick/Autocycler/

<details>

<summary>Additional tools installed via micromamba:</summary>

```
TBA
```

</details>

Basic information on how to use this tool:
- executable: autocycler
- help: --help
- version: --version
- description: |

> Autocycler is a tool for generating consensus long-read assemblies for bacterial genomes.

Additional information:

This image contains all additional tools listed in the environmental.yml file.
  
Full documentation: [https://github.com/rrwick/Autocycler/wiki](https://github.com/rrwick/Autocycler/wiki)

## Example Usage

```bash
reads=ont.fastq.gz  # your read set goes here
threads=16  # set as appropriate for your system
genome_size=$(genome_size_raven.sh "$reads" "$threads")  # can set this manually if you know the value

# Step 1: subsample the long-read set into multiple files
autocycler subsample --reads "$reads" --out_dir subsampled_reads --genome_size "$genome_size"

# Step 2: assemble each subsampled file
mkdir assemblies
for assembler in canu flye miniasm necat nextdenovo raven; do
    for i in 01 02 03 04; do
        "$assembler".sh subsampled_reads/sample_"$i".fastq assemblies/"$assembler"_"$i" "$threads" "$genome_size"
    done
done

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
