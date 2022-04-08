# bcftools container

Main tool : [bcftools](https://www.htslib.org/)

Full documentation: https://www.htslib.org/doc/bcftools.html

> BCFtools is a set of utilities that manipulate variant calls in the Variant Call Format (VCF) and its binary counterpart BCF. All commands work transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed.

# Example Usage

```
bcftools mpileup -A -d 200 -B -Q 0 -f {reference_genome} {bam} | bcftools call -mv -Ov -o bcftools_variants/{sample}.vcf
```
