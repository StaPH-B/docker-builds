# mash container

Main tool: [mash](https://github.com/marbl/Mash)
  
Code repository: https://github.com/marbl/Mash

Additional tools:
- none

Basic information on how to use this tool:
- executable: mash
- help: -h
- version: --version
- description: Fast genome and metagenome distance estimation using MinHash

Additional information:

This container includes a custom reference sketch at `/db/cbird-v2.0-lite.msh`<br>
The sketch contains only the species of `Acinetobacter, Burkholderia, Citrobacter, Enterobacter, Escherichia, Klebsiella, Kluyvera, Metapseudomonas, Morganella, Neisseria, Proteus, Providencia, Pseudomonas, Raoultella, Salmonella, Serratia, Streptococcus`<br>
The full list of sketched genomes are [here](https://github.com/Kincekara/cbird_mash_sketch/blob/main/mash_sketch_dataset_v2.0-lite.tsv).
  
Full documentation: https://mash.readthedocs.io/en/latest/

## Example Usage

```bash
# genome vs. genome
mash dist genome1.fna genome2.fna
# multiple genomes vs. genome
mash dist reference.msh genome.fna
# screen against refseq
mash screen refseq.genomes.msh genome.fq > screen.tab
```
