# krocus container

Main tool: [krocus](https://github.com/andrewjpage/krocus)
  
Code repository: https://github.com/andrewjpage/krocus

Basic information on how to use this tool:

- executable: `krocus`
- help: `krocus --help`
- version: `krocus --version`
- description: MLST typing from uncorrected long reads

Additional dependencies:

- python 3.10.6
- biopython 1.79
- pyfastaq 3.17.0

This container does not contain any of the mlst schemes. They must be downloaded prior to running the tool.
  
Full documentation: https://github.com/andrewjpage/krocus

## Example Usage

```bash
krocus_database_downloader -s "Species" -o allele_directory

krocus allele_directory input.fastq
```
