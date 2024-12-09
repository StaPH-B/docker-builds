# fasten container

Main tool: [fasten](https://github.com/lskatz/fasten/tree/master)
  
Code repository: https://github.com/lskatz/fasten

Basic information on how to use this tool:
- executable: fasten* (executables are found in `/usr/local/bin`)
- help: --help
- version: NA
- description: |
    > A powerful manipulation suite for interleaved fastq files. Executables can read/write to stdin and stdout, and they are compatible with the interleaved fastq format. This makes it much easier to perform streaming operations using unix pipes.

There are several commands associated with fasten:
|script             |Description|
|-------------------|-----------|
|[`fasten_clean`](https://lskatz.github.io/fasten/fasten_clean)     | Trims and cleans a fastq file.|
|[`fasten_convert`](https://lskatz.github.io/fasten/fasten_convert)   | Converts between different sequence formats like fastq, sam, fasta.|
|[`fasten_straighten`](https://lskatz.github.io/fasten/fasten_straighten)| Convert any fastq file to a standard four-line-per-entry format.|
|[`fasten_metrics`](https://lskatz.github.io/fasten/fasten_metrics)   | Prints basic read metrics.|
|[`fasten_pe`](https://lskatz.github.io/fasten/fasten_pe)        | Determines paired-endedness based on read IDs.|
|[`fasten_randomize`](https://lskatz.github.io/fasten/fasten_randomize) | Randomizes reads from input |
|[`fasten_combine`](https://lskatz.github.io/fasten/fasten_combine)   | Combines identical reads and updates quality scores.|
|[`fasten_kmer`](https://lskatz.github.io/fasten/fasten_kmer)      | Kmer counting.|
|[`fasten_normalize`](https://lskatz.github.io/fasten/fasten_normalize)      | Normalize read depth by using kmer counting.|
|[`fasten_sample`](https://lskatz.github.io/fasten/fasten_sample)    | Downsamples reads.|
|[`fasten_shuffle`](https://lskatz.github.io/fasten/fasten_shuffle)   | Shuffles or deshuffles paired end reads.|
|[`fasten_validate`](https://lskatz.github.io/fasten/fasten_validate)  | Validates your reads (deprecated in favor of `fasten_inspect` and `fasten_repair`|
|[`fasten_inspect`](https://lskatz.github.io/fasten/fasten_inspect)  | adds information to read IDs such as seqlength |
|[`fasten_repair`](https://lskatz.github.io/fasten/fasten_repair)  | Repairs corrupted reads |
|[`fasten_quality_filter`](https://lskatz.github.io/fasten/fasten_quality_filter) | Transforms nucleotides to "N" if the quality is low | |
|[`fasten_trim`](https://lskatz.github.io/fasten/fasten_trim)      | Blunt-end trims reads | |
|[`fasten_replace`](https://lskatz.github.io/fasten/fasten_replace)   | Find and replace using regex | |
|[`fasten_mutate`](https://lskatz.github.io/fasten/fasten_mutate)    | introduce random mutations | |
|[`fasten_regex`](https://lskatz.github.io/fasten/fasten_regex)     | Filter for reads using regex | |
|[`fasten_progress`](https://lskatz.github.io/fasten/fasten_progress)  | Add progress to any place in the pipeline | |
|[`fasten_sort`](https://lskatz.github.io/fasten/fasten_sort)  | Sort fastq entries | |

Full documentation: https://github.com/lskatz/fasten

## Example Usage

```bash
cat testdata/R1.fastq testdata/R2.fastq | fasten_shuffle | fasten_metrics > fasten_metrics.txt
zcat testdata/R1.fastq testdata/R2.fastq | fasten_shuffle | fasten_clean --paired-end --min-length 2 | gzip -c > cleaned.shuffled.fastq.gz
```
