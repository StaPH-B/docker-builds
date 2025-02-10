# GenoFLU container

Main tool: [GenoFLU](https://github.com/USDA-VS/GenoFLU)

Code repository: [https://github.com/USDA-VS/GenoFLU](https://github.com/USDA-VS/GenoFLU)

Additional tools:

- biopython 1.85
- ncbi-blast 2.16.0
- numpy 2.0.2
- pandas 2.2.3
- python 3.9.21

Basic information on how to use this tool:

- executable: `genoflu.py`
- help: `--help`
- version: `--version`
- description: "GenoFLU determines the genotype of a segmented flu sample by BLASTing a multi-segment FASTA against the BLAST database"

Additional information:

Full documentation: [https://github.com/USDA-VS/GenoFLU](https://github.com/USDA-VS/GenoFLU)

## Example Usage

```bash
genoflu.py -f input.fasta
```
