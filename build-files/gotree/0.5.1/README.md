# gotree container

Main tool: [gotree](https://github.com/evolbioinfo/gotree)

Code repository: [https://github.com/evolbioinfo/gotree](https://github.com/evolbioinfo/gotree)

Basic information on how to use this tool:
- executable: `gotree`
- help: `--help`
- version: `version`
- description: A comprehensive set of command-line tools for manipulating, modifying, and computing statistics on phylogenetic trees (Newick, Nexus, PhyloXML).

Full documentation: [https://github.com/evolbioinfo/gotree/wiki](https://github.com/evolbioinfo/gotree/wiki)

## Example Usage

```bash
# Calculate basic statistics for a tree file
gotree stats --input input_tree.nwk

# Reroot a tree at the midpoint
gotree reroot midpoint --input input_tree.nwk --output rooted_tree.nwk

# Generate a random tree
gotree generate random --tips-count 10 --seed 42
```