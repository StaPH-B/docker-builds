# UShER container

Main tool: [UShER](https://usher-wiki.readthedocs.io/en/latest/)
  
Code repository: https://github.com/yatisht/usher

Basic information on how to use this tool:
- executable: usher
- help: --help
- version: NA
- description: |
> UShER is a program for rapid, accurate placement of samples to existing phylogenies. 
  
Full documentation: https://usher-wiki.readthedocs.io/en/latest/

Also contains (same version):
- matUtils
- matOptimize
- ripples

## Example Usage

```bash
# create mutation annotated tree object
usher --tree global_phylo.nh --vcf global_samples.vcf --collapse-tree --save-mutation-annotated-tree global_phylo.pb

# place samples onto tree
usher --vcf new_samples.vcf --load-mutation-annotated-tree global_phylo.pb --write-uncondensed-final-tree
```
