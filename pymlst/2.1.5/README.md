# pyMLST container

Main tool: [pyMLST](link to program)
  
Code repository: https://github.com/bvalot/pyMLST

Additional tools:
- MAFFT : v7.490
- KMA : 1.3.28
- BLAT :  v.35

Basic information on how to use this tool:
- executable: pyMLST
- help: -h
- version: -v
- description: A Python Mlst Local Search Tool.

Additional information:

<Container contains X database at Y>
  
Full documentation: https://pymlst.readthedocs.io/en/latest/

## Example Usage

```bash
## cg/wgMLST
# initialize database
wgMLST import DATABASE
# add interested strain
wgMLST add DATABASE GENOME
# cgMLST distance
wgMLST distance DATABASE

# MLST
claMLST import DATABASE
claMLST search DATABASE GENOME
```
