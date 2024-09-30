# htslib container

Main tool: [htslib](https://www.htslib.org/)

Code repository: https://github.com/samtools/htslib

Additional tools:

* perl 5.34.0

Basic information on how to use this tool:
- executable: htsfile
- help: --help
- version: --version
- description: The htsfile utility attempts to identify what kind of high-throughput sequencing data files the specified files are, and provides minimal viewing capabilities for some kinds of data file.

Additional information:

This container includes htslib v1.21 compiled with **libdeflate** for a better cloud performance.

Full documentation: https://www.htslib.org/doc/samtools.html

## Example Usage

```bash
# determine file formats for various BAM and SAM files
$ htsfile tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam 
tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam:     BAM version 1 compressed sequence data

$ htsfile ce_tag_padded.sam
ce_tag_padded.sam:      SAM version 1.4 sequence text

# compresses sample.fastq to sample.fastq.gz in BGZF format (blocked GNU Zip Format)
$ bgzip sample.fastq
```
