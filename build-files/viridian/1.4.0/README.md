# Viridian container

Main tool: [Viridian](https://github.com/iqbal-lab-org/viridian)
  
Code repository: [Viridian](https://github.com/iqbal-lab-org/viridian)

Additional tools:
- samtools: 1.21
- bcftools: 1.21
- htslib: 1.21
- ENA: 1.7.1
- ngmerge: 0.3
- vt: 0.577721
- racon: 1.5.0
- mummer: 4.0.1
- read-it-and-keep: 0.3.0
- cylon: commit hash 9402ba5e96ba52d5ade0deb2268d680d8726ad48
- varifier: commit hash 940d4503671f5dd09ce51116be6e77c85d50ada5
- minimap2: 2.28

Basic information on how to use this tool:
- executable: viridian
- help: --help
- version: --version
- description: Ultra-careful amplicon-aware viral assembly for tiled amplicon schemes.
  
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
