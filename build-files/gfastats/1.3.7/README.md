# gfastats container

Main tool : [gfastats](https://github.com/vgl-hub/gfastats)

Full documentation: [https://github.com/vgl-hub/gfastats](https://github.com/vgl-hub/gfastats)

> The swiss army knife for genome assembly.
> gfastats is a single fast and exhaustive tool for summary statistics and simultaneous *fa* (fasta, fastq, gfa [.gz]) genome assembly file manipulation. gfastats also allows seamless fasta<>fastq<>gfa[.gz] conversion.

## Example Usage

```bash
# from readme
gfastats input.[fasta|fastq|gfa][.gz] [expected genome size] [header[:start-end]]

# sample usage
gfastats  input.gfa --threads 4 --tabular --seq-report
```