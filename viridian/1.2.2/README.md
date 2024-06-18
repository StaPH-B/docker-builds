# Viridian container

Main tool: [Viridian](https://github.com/iqbal-lab-org/viridian)

Code repository: [Viridian](https://github.com/iqbal-lab-org/viridian)

Basic Usage: Ultra-careful amplicon-aware viral assembly for tiled amplicon schemes.

Full documentation: [Viridian wiki](https://github.com/iqbal-lab-org/viridian/wiki)

## Example Usage

To run on paired Illumina reads:

```bash
viridian run_one_sample \
  --tech illumina \
  --reads1 reads_1.fastq.gz \
  --reads2 reads_2.fastq.gz \
  --outdir OUT
```

Download reads with accession SRR12345678 and run:
```bash
viridian run_one_sample --run_accession SRR12345678 --outdir OUT
```

The sequencing tech and unpaired/paired is taken from the ENA metadata for each run.
