
# artic-tools container

Main tool: [artic-tools](https://github.com/will-rowe/artic-tools)
  
Code repository: https://github.com/will-rowe/artic-tools

Basic information on how to use this tool:
- executable: artic-tools
- help: `-h`, `--help`
- version: `-v`, `--version`
- description: |
> We've been working on artic-tools as a complimentary set of utilities for helping with amplicon sequencing workflows and plan to incorporate them into the ARTIC pipeline.

Additional information and Full Documentation: https://artic-tools.readthedocs.io/en/latest/

## Example Usage

align_trim
```bash
artic-tools align_trim -b in.bam primerscheme.bed > out.bam 2> out.log
```

get_scheme
```bash
artic-tools artic-tools get_scheme nipah
```

validate_scheme
```bash
artic-tools artic-tools validate_scheme primerscheme.bed
```

check_vcf
```bash
artic-tools check_vcf -o summary.txt --vcfOut variants_passed.txt CVR1.merged.vcf.gz SCoV2.scheme.v3.bed
```
