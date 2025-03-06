# PPanGGOLiN container

Main tool: [PPanGGOLiN](https://github.com/labgem/PPanGGOLiN)
  
Code repository: https://github.com/labgem/PPanGGOLiN

Basic information on how to use this tool:
- executable: ppanggolin
- help: --help
- version: --version
- description: |
> PPanGGOLiN builds pangenomes through a graphical model and a statistical method to partition gene families in persistent, shell and cloud genomes.

Additional information:

PPanGGOLiN only creates the pangenome graphs. It is recommended to use another tool to visualize them. Please read https://github.com/labgem/PPanGGOLiN/wiki for more information.
  
Full documentation: https://github.com/labgem/PPanGGOLiN/wiki

## Example Usage

```bash
ppanggolin annotate --fasta organisms.fasta.list --output output 

# many of the commands manipulate the 'pangenome.h5' file in place
ppanggolin cluster -p pangenome.h5
ppanggolin graph -p pangenome.h5 
ppanggolin partition -p pangenome.h5
ppanggolin draw -p pangenome.h5 --ucurve   

# there are some human-readable files that can be generated as well
ppanggolin write -p pangenome.h5 --stats --output stats
```
