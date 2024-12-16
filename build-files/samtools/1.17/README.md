# samtools container

Main tool:

* [https://www.htslib.org/](https://www.htslib.org/)
* [GitHub](https://github.com/samtools/samtools)

Additional tools:

* python 3.8.10
* perl 5.30.0

## Example Usage

```bash
samtools ampliconclip -b bed.file input.bam

samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam
```

Better documentation can be found at [https://www.htslib.org/doc/samtools.html](https://www.htslib.org/doc/samtools.html)