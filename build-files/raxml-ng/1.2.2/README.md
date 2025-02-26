# RAxML-NG container

Main tool: [raxml-ng](https://github.com/amkozlov/raxml-ng)
  
Code repository: https://github.com/amkozlov/raxml-ng

Basic information on how to use this tool:
- executable: raxml-ng
- help: --help
- version: --version
- description: RAxML-NG is a phylogenetic tree inference tool which uses maximum-likelihood (ML) optimality criterion.

Full documentation: https://github.com/amkozlov/raxml-ng/wiki

## Example Usage

```bash
# Perform tree inference on DNA alignment
raxml-ng --msa testDNA.fa --model GTR+G

# Perform an all-in-one analysis 
raxml-ng --all --msa testAA.fa --model LG+G8+F --tree pars{10} --bs-trees 200

# Optimize branch lengths and free model parameters on a fixed topology
raxml-ng --evaluate --msa testAA.fa --model partitions.txt --tree test.tree --brlen scaled
```


