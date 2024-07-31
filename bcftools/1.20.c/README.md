# bcftools container

Main tool:

* [bcftools](https://github.com/samtools/bcftools)

## Example Usage

```bash
bcftools mpileup -A -d 200 -B -Q 0 -f {reference_genome} {bam} | bcftools call -mv -Ov -o bcftools_variants/{sample}.vcf
```

Better documentation can be found at [https://www.htslib.org/doc/bcftools.html](https://www.htslib.org/doc/bcftools.html)
