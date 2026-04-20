# BandageNG container
Main tool: [BandageNG](https://github.com/asl/BandageNG)

Fork of: [Bandage](https://rrwick.github.io/Bandage/)

Code repository: https://github.com/asl/BandageNG

Basic information on how to use this tool:
- executable: BandageNG
- help: `--help` and `--helpall`
- version: `--version`
- description: A GUI program that allows users to interact with the assembly graphs made by de novo assemblers such as SPAdes, MEGAHIT and others.

Additional information:
This is a fork of Ryan Wick's Bandage; much of the documentation is based off of the original repository's. Currently, this fork has sparse self-documentation, though most of what is specified by Bandage's CLI documentation is equivalent. We highly recommend running `BandageNG --helpall` to explore CLI usage.

It has CLI components and GUI components, however, the current image is configured for CLI usage only. 

This image is based off of a prebuilt binary, however, it has additional libraries corresponding to Qt6 for proper functionality.

Full documentation: https://github.com/rrwick/Bandage/wiki/Command-line
## Example Usage
### Generating an image file of the graph visualization
```bash
BandageNG image test.gfa output.png
```
### Outputting Graph File statistics
```bash
BandageNG info test.gfa --tsv
```