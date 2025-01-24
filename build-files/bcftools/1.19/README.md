# bcftools container

Main tool:

* [https://www.htslib.org/](https://www.htslib.org/)
* [GitHub](https://github.com/samtools/bcftools)

Additional tools:

* perl 5.34.0

## Example Usage

```bash
bcftools mpileup -A -d 200 -B -Q 0 -f {reference_genome} {bam} | bcftools call -mv -Ov -o bcftools_variants/{sample}.vcf
```

Better documentation can be found at [https://www.htslib.org/doc/bcftools.html](https://www.htslib.org/doc/bcftools.html)
