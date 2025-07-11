# SISTR container

Main tool: [sistr](https://github.com/phac-nml/sistr_cmd)
  
Code repository: https://github.com/phac-nml/sistr_cmd

Additional tools:
- blast : 2.12.0
- mafft : v7.490
- mash : 2.3
- pandas : 2.2.3
- numpy : 1.26.4

Basic information on how to use this tool:
- executable: `sistr`
- help: `-h`, `--help`
- version: `-V`, `--version`
- description: (Salmonella In Silico Typing Resource) Command-line Tool

Full documentation: https://github.com/phac-nml/sistr_cmd

## Example Usage

```bash
sistr --qc -vv --alleles-output allele-results.json --novel-alleles novel-alleles.fasta --cgmlst-profiles cgmlst-profiles.csv -f tab -o sistr-output.tab genome.fasta
```

