# sistr container

Main tool : [sistr](https://github.com/phac-nml/sistr_cmd)

Additional tools:
- ncbi-blast
- mafft
- mash

Full documentation: https://github.com/phac-nml/sistr_cmd

> Salmonella In Silico Typing Resource (SISTR) commandline tool

# Example Usage

From github
```
sistr --qc -vv --alleles-output allele-results.json --novel-alleles novel-alleles.fasta --cgmlst-profiles cgmlst-profiles.csv -f tab -o sistr-output.tab LT2.fasta
```
