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

This image does not contain any of the assemblers listed in the wikis or tutorials. All helper scripts should be in path and are located at /usr/local/bin.
  
Full documentation: [https://github.com/rrwick/Autocycler/wiki](https://github.com/rrwick/Autocycler/wiki)

## Official Steps
* Step 1: [Autocycler subsample](https://github.com/rrwick/Autocycler/wiki/Autocycler-subsample)
  * "Creates multiple read subsets from a single long-read dataset, minimising overlap to ensure each subset is as independent as possible."
* Step 2: [Generating input assemblies](https://github.com/rrwick/Autocycler/wiki/Generating-input-assemblies)
  * "Each of the read subsets made by Autocycler subsample can now be assembled, producing multiple alternative assemblies of the same genome."
* Step 3: [Autocycler compress](https://github.com/rrwick/Autocycler/wiki/Autocycler-compress)
  * "The autocycler compress command uses your input assemblies to build a compacted De Bruijn graph (a.k.a. a unitig graph)."
* Step 4: [Autocycler cluster](https://github.com/rrwick/Autocycler/wiki/Autocycler-cluster)
  * "The autocycler cluster command groups input contigs into clusters. A cluster is a group of contigs which represent the same genomic sequence. It also decides which of these clusters should be included in the final assembly (QC-pass) and which should not (QC-fail)."
* Step 5: [Autocycler trim](https://github.com/rrwick/Autocycler/wiki/Autocycler-trim)
  * "Long-read contigs sometimes contain excess sequence which needs to be trimmed off." 
  * "This step is performed on a per-cluster basis. For each contig, Autocycler looks for two types of excess sequence: start-end circular overlap and hairpin overlap. Contigs are trimmed as necessary. After trimming, Autocycler discards any contigs with outlier lengths, so the remaining contigs in the cluster will all be in close agreement with each other."
* Step 6: [Autocycler resolve](https://github.com/rrwick/Autocycler/wiki/Autocycler-resolve) \
"Aims to resolve repeats and ambiguities in the cluster by following these steps:

  * Identifying anchors: unitigs which occur exactly once in each of the cluster's contigs.
  * Creating bridges: connections between anchors that follow the most supported path.
  * Applying bridges: first unique bridges (those with no conflicts) and then the most supported conflicting bridges.
  * Merging linear sequences into 'consentigs'."

* Step 7: [Autocycler combine ](https://github.com/rrwick/Autocycler/wiki/Autocycler-combine)
  * "This is the final step in an Autocycler assembly, where the resolved sequences for each cluster are combined into a single assembly."

## Quick Start step with helper script.

```bash
autocycler_full.sh reads.fastq.gz 16 4
```

## Fully automated assembly

```bash
reads=ont.fastq.gz  # your read set goes here
threads=16  # set as appropriate for your system (no more than 128)
genome_size=$(autocycler helper genome_size --reads "$reads" --threads "$threads")  # can set this manually if you know the value

# Step 1: subsample the long-read set into multiple files
autocycler subsample --reads "$reads" --out_dir subsampled_reads --genome_size "$genome_size"

# Step 2: assemble each subsampled file
mkdir assemblies
for assembler in canu flye metamdbg miniasm necat nextdenovo plassembler raven; do
    for i in 01 02 03 04; do
        autocycler helper "$assembler" --reads subsampled_reads/sample_"$i".fastq --out_prefix assemblies/"$assembler"_"$i" --threads "$threads" --genome_size "$genome_size"
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

## Information about manually curating your own assembly

According to the author, Ryan Wick, certain steps in the aforementioned fully automated assembly can be [manually curated](https://github.com/rrwick/Autocycler/wiki/Manually-curated-assembly).

* After Steps 1 & 2, you can curate input assemblies.
  * See the [Generating input assemblies](https://github.com/rrwick/Autocycler/wiki/Generating-input-assemblies) page for more details.
  * See the [Influencing Autocycler via contig headers](https://github.com/rrwick/Autocycler/wiki/Influencing-Autocycler-via-contig-headers) page for more details.
* After Steps 3 & 4, you can curate your clusters.
  * See the [Autocyler cluster](https://github.com/rrwick/Autocycler/wiki/Autocycler-cluster) page for more details.
* After Steps 5 & 6, you can examine dot plots and the autocycler bridging.
  * See the [Autocycler dotplot](https://github.com/rrwick/Autocycler/wiki/Autocycler-dotplot) page for more information.
  * "In particular, it can be helpful to examine each cluster's 4_merged.gfa file to see if there is structural heterogeneity or conflicts between assemblies."
* A manual step of removing any extraneous sequences can be done after Step 7.
  * See [Bandage](https://github.com/rrwick/Bandage), a tool by Ryan Wick.
  * [Autocycler clean](https://github.com/rrwick/Autocycler/wiki/Autocycler-clean) can be used to "remove unwanted tigs to allow for a fully resolved assembly."
