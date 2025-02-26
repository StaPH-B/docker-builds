# BBTools container

Main tool: [BBTools](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/)
  
Code repository: https://sourceforge.net/projects/bbmap/

Additional tools:
- samtools: 1.21
- htslib: 1.21
- sambamba: 1.0.1

Basic information on how to use this tool:
- executable: *.sh
- help: Program descriptions and options are shown when running the shell scripts with no parameters.
- version: --version
- description: 
>BBTools is a suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data. BBTools can handle common sequencing file formats such as fastq, fasta, sam, scarf, fasta+qual, compressed or raw, with autodetection of quality encoding and interleaving.

Additional information:
| Script                  | Purpose                                                                          | Comment                                                                |
|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| bbcms.sh                | Performs error correction using a Count-Min Sketch                               | Intended for metagenome assembly assembly                              |
| bbcountunique.sh        | Counts unique kmers in reads                                                     |                                                                        |
| bbduk.sh                | Trims, filters or masks reads using kmers                                        |                                                                        |
| bbmap.sh                | Splice-aware aligner for short reads                                             |                                                                        |
| bbmapskimmer.sh         | BBMap version designed for high levels of multimapping                           |                                                                        |
| bbmask.sh               | Masks references based on various things, such as sequence complexity            |                                                                        |
| bbmerge.sh              | Merges overlapping paired reads                                                  |                                                                        |
| bbmerge-auto.sh         | Same as bbmerge, but tries to allocate all memory on the node                    | Use this version for kmer operations like extend                       |
| bbnorm.sh               | Normalizes reads based on coverage                                               | Mainly for use prior to single-cell assembly                           |
| bbsplit.sh              | BBMap version that maps to multiple references simultaneously                    | Intended for decontamination; similar to Seal                          |
| bbversion.sh            | Prints the version of BBTools                                                    |                                                                        |
| bbwrap.sh               | Wraps BBMap to process many files using same reference                           | Saves time by loading the index only once                              |
| calctruequality.sh      | Allows recalibration of quality scores from mapped reads                         | This generates the correction matrix; BBDuk does the recalibration     |
| callgenes.sh            | Fast prokaryotic gene caller                                                     | Integrated into BBSketch                                               |
| callvariants.sh         | Fast variant caller                                                              |                                                                        |
| callvariants2.sh        | Same as callvariants.sh with the "multisample" flag                              |                                                                        |
| clumpify.sh             | Shrinks compressed fastq files, and can remove duplicate reads                   | Also supports error correction                                         |
| comparesketch.sh        | Compares sketches locally, without using a sketch server                         |                                                                        |
| crossblock.sh           | Alias for decontaminate.sh                                                       |                                                                        |
| cutgff.sh               | Cuts out features defined by gff file                                            | E.g, generates one fasta entry per gene from a gff and an assembly     |
| cutprimers.sh           | Cuts out subregions of ribosomes                                                 | Mainly for 16S analysis                                                |
| decontaminate.sh        | Pool-level decontamination for single-cell MDA-amplified genomes                 |                                                                        |
| dedupe.sh               | Removes duplicate and fully-contained sequences                                  | Can also be used to cluster 16S sequences                              |
| dedupe2.sh              | Version of dedupe that supports more hash keys for greater sensitivity           |                                                                        |
| dedupebymapping.sh      | Deduplicates reads based on mapping coordinates                                  |                                                                        |
| demuxbyname.sh          | Demultiplexes based on sequences headers                                         |                                                                        |
| filterbyname.sh         | Filters based on sequence headers                                                |                                                                        |
| filterbytaxa.sh         | Filters sequences based on taxonomic classification                              | Used with NCBI datasets                                                |
| filterbytile.sh         | Removes reads that are in low quality areas on flowcell                          |                                                                        |
| filterqc.sh             | Part of JGI's fastq filtering pipeline                                           |                                                                        |
| filtersam.sh            | Filters sam files to remove reads with multiple unsupported mismatches           | Designed for NovaSeq                                                   |
| gitable.sh              | Used to process NCBI taxonomy data                                               |                                                                        |
| khist.sh                | Alias for bbnorm.sh with flags for making a kmer frequency histogram             |                                                                        |
| kmercountexact.sh       | Counts kmers and produces a histogram                                            | Uses more memory than BBNorm but allows exact counts                   |
| kmercountmulti.sh       | Cardinality estimation over multiple kmer lengths                                | Uses LogLog; does not produce a histogram                              |
| mapPacBio.sh            | BBMap version designed for PacBio or Nanopore reads                              | Reads longer than 5kbp get broken into 5kbp shreds                     |
| mergesketch.sh          | Allows multiple sketches to be combined                                          |                                                                        |
| msa.sh                  | Alignment tool                                                                   | Used with cutprimers.sh to cut subsections out of 16s                  |
| mutate.sh               | Generates synthetic genomes by randomly mutating the input                       |                                                                        |
| muxbyname.sh            | Multiplex multiple files, renaming sequences based on input file name            | Opposite of demuxbyname.sh                                             |
| partition.sh            | Splits a sequence file into multiple files                                       |                                                                        |
| pileup.sh               | Calculates coverage from sam files                                               |                                                                        |
| plotflowcell.sh         | Produces statistics about flowcell positions                                     |                                                                        |
| processhi-c.sh          | Custom trimming for hi-C reads                                                   | In development                                                         |
| randomreads.sh          | Generates synthetic data from real genome reference                              | Highly customizable                                                    |
| readqc.sh               | Short read quality report                                                        | Alternative to fastqc                                                  |
| reformat.sh             | Converts sequence files to another format                                        | Has many additional options, includes subsampling                      |
| rename.sh               | Renames sequences in various ways, such as adding a prefix                       |                                                                        |
| repair.sh               | Fixes broken pairing in fastq files                                              |                                                                        |
| representative.sh       | Makes a smaller subset of a reference dataset by eliminating redundancy          | Designed for use with BBSketch output                                  |
| rqcfilter2.sh           | Filtering pipeline used at JGI                                                   | portal.nersc.gov/dna/microbial/assembly/bushnell/RQCFilterData.tar     |
| seal.sh                 | Counts kmer matches between query and reference sequences                        |                                                                        |
| sendsketch.sh           | Fast taxonomic classifier using webservers at JGI                                |                                                                        |
| shred.sh                | Breaks sequences into shorter, fixed-length pieces                               |                                                                        |
| shuffle.sh              | Randomly reorders input file                                                     | Crashes if input doesn't fit in memory                                 |
| shuffle2.sh             | Randomly reorders input file                                                     | Supports larger files, but output might be less random                 |
| sketch.sh               | Makes reference sketches on a per-TaxID basis                                    |                                                                        |
| sketchblacklist.sh      | Makes sketch blacklists of common kmers                                          |                                                                        |
| sortbyname.sh           | Sorts sequences by name, length, quality, taxa, and other things                 |                                                                        |
| summarizequast.sh       | Generates box plots for multiple quast reports                                   |                                                                        |
| tadpipe.sh              | Preprocessing and assembly pipeline using tadpole                                |                                                                        |
| tadpole.sh              | Fast short read assembler                                                        |                                                                        |
| tadwrapper.sh           | Runs Tadpole with multiple kmer lengths to select the best assembly              |                                                                        |
| taxserver.sh            | Starts taxonomy and sketch servers                                               |                                                                        |
| testformat.sh           | Determines if file is fasta, fastq, interleaved, etc. by reading first few lines |                                                                        |
| testformat2.sh          | Generates extensive statistics by reading the full file                          |                                                                        |
| translate6frames.sh     | Translates nucleotide sequence into amino acid sequence in all frames            |                                                                        |
| vcf2gff.sh              | Converts vcf format to gff format                                                |                                                                        |
  
Full documentation: https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/

## Example Usage

(adapted from `/opt/bbmap/pipelines/covid/processCorona.sh`)

Interleave a pair of FASTQ files for downstream processing:

```text
reformat.sh \
    in1=${SAMPLE}_R1.fastq.gz \
    in2=${SAMPLE}_R2.fastq.gz \
    out=${SAMPLE}.fastq.gz
```
Split into SARS-CoV-2 and non-SARS-CoV-2 reads:

```text
bbduk.sh ow -Xmx1g \
    in=${SAMPLE}.fq.gz \
    ref=REFERENCE.fasta \
    outm=${SAMPLE}_viral.fq.gz \
    outu=${SAMPLE}_nonviral.fq.gz \
    k=25
```
