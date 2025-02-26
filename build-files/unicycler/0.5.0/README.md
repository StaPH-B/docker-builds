# Unicycler container

Main tools:
- [Unicycler](https://github.com/rrwick/Unicycler)

Other tools:
- [spades](https://github.com/ablab/spades)
- [racon](https://github.com/isovic/racon)

Unicycler is a hybrid assembler that takes reads assembled with spades and ties them together with long reads.

# Example Usage

```
unicycler -1 short_reads_1.fastq.gz -2 short_reads_2.fastq.gz -l long_reads.fastq.gz -o output_dir
```

Better documentation can be found at [https://github.com/rrwick/Unicycler](https://github.com/rrwick/Unicycler)
