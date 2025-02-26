# RAxML container

Main tool: [raxmlHPC](https://github.com/stamatak/standard-RAxML)
  
Code repository: https://github.com/stamatak/standard-RAxML

Additional tools:

- raxmlHPC-AVX
- raxmlHPC-HYBRID
- raxmlHPC-HYBRID-AVX
- raxmlHPC-HYBRID-SSE3
- raxmlHPC-MPI
- raxmlHPC-MPI-AVX
- raxmlHPC-MPI-SSE3
- raxmlHPC-PTHREADS
- raxmlHPC-PTHREADS-AVX
- raxmlHPC-PTHREADS-SSE3
- raxmlHPC-SSE3

Basic information on how to use this tool:
- executable: raxmlHPC
- help: -h
- version: -v
- description: A tool for Phylogenetic Analysis and Post-Analysis of Large Phylogenies

Full documentation: https://github.com/stamatak/standard-RAxML/blob/master/manual/NewManual.pdf

## Example Usage

```bash
raxmlHPC -s sequenceFileName -n outputFileName -m substitutionModel
```
