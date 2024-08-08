# htslib container

Main tool:

* [https://www.htslib.org/](https://www.htslib.org/)
* [GitHub](https://github.com/samtools/htslib)

Additional tools:

* perl 5.34.0

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

Better documentation can be found at [https://www.htslib.org/doc/samtools.html](https://www.htslib.org/doc/samtools.html)
