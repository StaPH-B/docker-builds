# Merqury container

Main tool: [merqury](https://github.com/marbl/merqury)
  
Code repository: https://github.com/marbl/merqury

Additional tools:
- meryl: 1.4.1
- samtools: 1.19.2
- bedtools: 2.31.1

Basic information on how to use this tool:
- executable: `merqury.sh`
- help: 
- version:
- description: reference-free quality, completeness, and phasing assessment for genome assemblies

Additional information:

Rhie, A., Walenz, B.P., Koren, S. et al. Merqury: reference-free quality, completeness, and phasing assessment for genome assemblies. Genome Biol 21, 245 (2020). https://doi.org/10.1186/s13059-020-02134-9
  
Full documentation: https://github.com/marbl/merqury/wiki

## Example Usage

```bash
# required: < > , optional: [ ]
merqury.sh [-c] <read-db.meryl> [<mat.meryl> <pat.meryl>] <asm1.fasta> [asm2.fasta] <out>
```
