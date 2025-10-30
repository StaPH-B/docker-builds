# pod5 container

Main tool: [pod5](https://github.com/nanoporetech/pod5-file-format)
  
Code repository: [https://github.com/nanoporetech/pod5-file-format](https://github.com/nanoporetech/pod5-file-format)

Additional tools:
- python 3.9.17

Basic information on how to use this tool:

- executable: `pod5`
- help: `--help`
- version: `--version`
- description: "The pod5 package provides the following tools for inspecting and manipulating POD5 files as well as converting between .pod5 and .fast5 file formats."

Additional information:
  
Full documentation: [https://pod5-file-format.readthedocs.io/en/latest/index.html](https://pod5-file-format.readthedocs.io/en/latest/index.html)

## Example Usage

```bash
# split pod5 files into channel-specific pod5 files for parallelization of dorado basecalling
pod5 view . --include "read_id, channel" --output summary.tsv && \
pod5 subset . --summary summary.tsv --columns channel
```
