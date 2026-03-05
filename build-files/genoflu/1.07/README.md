# GenoFLU container

Main tool: [GenoFLU](https://github.com/USDA-VS/GenoFLU)

Code repository: [https://github.com/USDA-VS/GenoFLU](https://github.com/USDA-VS/GenoFLU)

Additional tools:

- biopython 1.86
- ncbi-blast 2.17.0
- numpy 2.4.2
- pandas 3.0.1
- python 3.14.3

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
