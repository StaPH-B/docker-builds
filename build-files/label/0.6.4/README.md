# LABEL container

Main tool: [LABEL](https://wonder.cdc.gov/amd/flu/label/)
  
Code repository: https://wonder.cdc.gov/amd/flu/label/

Additional tools:
- mafft: v7.490 

Note: muscle and fasttree are downloaded with LABEL

Basic information on how to use this tool:
- executable: label
- help: -h
- version: NA
- description: |
    > LABEL was designed for the rapid annotation of influenza (or other virus) clades using profile Hidden Markov models and support vector machines. In particular, LABEL comes with modules to annotate clades for influenza A(H5N1) hemagluttinin gene segments as described by the WHO/FAO/OIE H5N1 nomenclature working group.
  
Full documentation: link to documentation or wiki

## Example Usage

```bash
LABEL /flu-amd/test.fa test\_proj H9v2011
```
