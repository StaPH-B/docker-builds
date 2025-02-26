# phyTreeViz container

Main tool: [phyTreeViz](https://github.com/moshi4/phyTreeViz)
  
Code repository: https://github.com/moshi4/phyTreeViz

Basic information on how to use this tool:
- executable: phytreeviz
- help: --help
- version: --version
- description: Visualizing phylogenetic trees

Additional information:

> phyTreeViz is a simple and minimal phylogenetic tree visualization python package implemented based on matplotlib. This package was developed to enhance phylogenetic tree visualization functionality of BioPython.

This is contains a python library as well as a command line executable.
  
Full documentation: 
- CLI Docs : https://moshi4.github.io/phyTreeViz/cli-docs/phytreeviz/
- API Docs : https://moshi4.github.io/phyTreeViz/api-docs/treeviz/

## Example Usage

CLI example
```bash
phytreeviz -i input.nwk -o output.png 
```

API example
```python
from phytreeviz import TreeViz, load_example_tree_file

tree_file = load_example_tree_file("small_example.nwk")

tv = TreeViz(tree_file)
tv.show_branch_length(color="red")
tv.show_confidence(color="blue")
tv.show_scale_bar()

tv.savefig("api_example01.png", dpi=300)
```
