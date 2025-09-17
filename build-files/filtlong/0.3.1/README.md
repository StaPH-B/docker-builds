# filtlong container

Main tool : [filtlong](https://github.com/rrwick/Filtlong)

Full documentation: [https://github.com/rrwick/Filtlong](https://github.com/rrwick/Filtlong)

Filtlong filters long-read fastq files by quality & read lengths.

## Example Usage

```bash
filtlong --min_length 1000 --keep_percent 90 --target_bases 500000000 input.fastq.gz | gzip > output.fastq.gz
```
