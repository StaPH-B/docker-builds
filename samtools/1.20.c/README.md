# samtools container

Main tool: [samtools](https://www.htslib.org/)

Code repository: https://github.com/samtools/samtools

Additional tools:

* perl 5.34.0

Basic information on how to use this tool:
- executable: samtools
- help: --help
- version: --version
- description: Utilities for the Sequence Alignment/Map (SAM) format

Additional information:

This container includes samtools v1.20 compiled with **libdeflate** for a better cloud performance.

Full documentation: https://www.htslib.org/doc/samtools.html

## Example Usage

```bash
samtools ampliconclip -b bed.file input.bam

samtools sort -T /tmp/aln.sorted -o aln.sorted.bam aln.bam
```

