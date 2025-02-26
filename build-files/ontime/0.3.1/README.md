# ontime container

Main tool: [ONTime](https://github.com/mbhall88/ontime/tree/main)
  
Code repository: https://github.com/mbhall88/ontime

Basic information on how to use this tool:
- executable: ontime
- help: --help
- version: --version
- description: Extracts nanopore reads based on when in the run reads were generated.
  
Full documentation: https://github.com/mbhall88/ontime/tree/main

WARNING : the nanopore fastq file MUST still have the time stamp on the reads in the fastq fime, so this tool is **NOT** expected to run on reads downloaded from public repositories.

## Example Usage

```bash
# reads from the first five hours
ontime --to 5h in.fq
# reads after the first 24 hours
ontime --from 24h in.fq
# Check what the earliest and latest start times in the fastq are
ontime --show in.fq
```
