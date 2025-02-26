# SNVPhyl-Tools Container

## Documentation and Overview

Main Tool: SNVPhyl-tools for use with the SNVPhyl pipeline

Full documentation: https://github.com/phac-nml/snvphyl-tools

SNVPhyl-Tools are used in the [SNVPhyl Whole Genome SNV Phylogenomics Pipeline](https://snvphyl.readthedocs.io/en/latest/). You can read the [SNVPhyl pipeline paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5628696/) for more information. 

"The SNVPhyl (__S__ingle __N__ucleotide __V__ariant __PHYL__ogenomics) pipeline is a pipeline for identifying Single Nucleotide Variants (SNV) within a collection of microbial genomes and constructing a phylogenetic tree. Input is provided in the form of a collection of whole genome sequence reads as well as an assembled reference genome. The output for the pipeline consists of a whole genome phylogenetic tree constructed from the detected SNVs, as well as a list of all detected SNVs and other information." 

The [original pipeline](https://github.com/phac-nml/snvphyl-galaxy) is implemented using the Galaxy bioinformatics analysis platform, but this container can be used in conjunction with a [nextflow workflow](https://github.com/DHQP/SNVPhyl_Nextflow) to run SNVPhyl on a HPC or locally off of Galaxy. 

This tool kit contains the following scripts that are written in perl:
- consolidate_vcfs.pl
- core-only.pl
- extract_snvs_metaalign.pl
- filter-positions.pl
- filter-stats.pl
- filterVcf.pl
- filter_unique_basepairs.pl
- find-positions-used.pl
- find-repeats.pl
- positions2phyloviz.pl
- positions2snv_alignment.pl
- positions2snv_invariant_alignment.pl
- rearrange_snv_matrix.pl
- ref_stats.pl
- reporter.pl
- snv_matrix.pl
- tsvToVcf.pl
- vcf2snv_alignment.pl
- verify_excess_coverage.pl
- verify_low_depth.pl
- verify_mapping_quality.pl

To get details on each tool type the tool name into your terminal:

```
me@my_pc: find-repeats.pl
```
outputs:
```
error: no input file defined
Usage: find-repeats.pl [reference.fasta] --min-length [length] --min-pid [pid]
Parameters:
        [reference.fasta]:  A fasta reference file to search for repeats.
Options:
        -l|--min-length: Minimum length of repeat region (150).
        -p|--min-pid: Minimum PID of repeat region (90).
        -k|--keep-temp: Keep around temporary nucmer/coords files (no).
```
