# Shigatyper 2.0.4 container

Main tool : [shigatyper](https://github.com/CFSAN-Biostatistics/shigatyper)

Additional tools:

- samtools 1.9
- bcftools 1.9
- minimap2 2.24
- python 3.10.6

## Known Version Issue

The 2.0.4 release of Shigatyper reports the incorrect version `2.0.3` when running `shigatyper --version`. This is [a known issue](https://github.com/CFSAN-Biostatistics/shigatyper/pull/16) and should be addressed in the next version release. Users should not rely upon the command for correctly reporting the version, but rather the docker image tag `2.0.4` for tracking the correct version.

## Example Usage

```{bash}
# Paired-end reads
shigatyper.py --R1 SRX5006488_R1.fastq.gz --R2 SRX5006488_R2.fastq.gz
sample  prediction      ipaB
SRX5006488      Shigella boydii serotype 12     +

# Single-end reads
shigatyper.py --SE SRX5006488.fastq.gz
sample  prediction      ipaB
SRX5006488-se   Shigella boydii serotype 12     +

# Oxford Nanopore reads
shigatyper.py --SE SRX7050861.fastq.gz --ont
sample  prediction      ipaB
SRX7050861-ont  Shigella dysenteriae serotype 3 +
```

Better documentation can be found at [https://github.com/CFSAN-Biostatistics/shigatyper](https://github.com/CFSAN-Biostatistics/shigatyper)
