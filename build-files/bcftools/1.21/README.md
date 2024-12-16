# bcftools container

Main tool: [bcftools](https://github.com/samtools/bcftools)

Code repository: https://github.com/samtools/bcftools

Basic information on how to use this tool:
- executable: bcftools
- help: --help
- version: --version
- description: BCFtools is a program for variant calling and manipulating files in the Variant Call Format (VCF) and its binary counterpart BCF. 

Additional information:

This container includes bcftools v1.21 compiled with **libdeflate** for a better cloud performance. Also, "polysomy" and plugins are enabled in this image.
  
Full documentation: https://samtools.github.io/bcftools/howtos/index.html

## Example Usage

```bash
bcftools mpileup -A -d 200 -B -Q 0 -f {reference_genome} {bam} | bcftools call -mv -Ov -o bcftools_variants/{sample}.vcf
```


