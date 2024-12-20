# Integron Finder container

Main tool: [Integron Finder](https://integronfinder.readthedocs.io/en/latest/)
  
Code repository: https://github.com/gem-pasteur/Integron_Finder

Additional tools:
 - Python 3.10.12
 - numpy 2.1.1
 - pandas 2.2.3
 - matplolib 3.9.2
 - biopython 1.84
 - Prodigal V2.6.3
 - INFERNAL 1.1.4
 - HMMER 3.3.2

Basic information on how to use this tool:
- executable: integron_finder
- help: --help
- version: --version
- description: Finds integrons in DNA sequences
 
Full documentation: https://integronfinder.readthedocs.io/en/latest/

## Example Usage

```bash
integron_finder --local-max --circ --keep-tmp genome.fna
```
