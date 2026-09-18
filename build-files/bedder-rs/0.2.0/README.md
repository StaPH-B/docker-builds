# bedder-rs container
Main tool: [bedder-rs](https://github.com/quinlan-lab/bedder-rs)
  
Code repository: https://github.com/quinlan-lab/bedder-rs

Basic information on how to use this tool:
- executable: bedder
- help: `-h`, `--help`
- version: `-V`, `--version`
- description: A rust-based command-line tool for genomic analysis serving as a successor to bedtools.

Additional information:

This program is a successor to BEDTools using rust as its primary backend language. The tool offers flexibility for use cases supported by BEDTools, speed, and extensibility with support for python functions to allow for more information in columns as output. 
  
Full documentation: https://brentp.github.io/bedder-docs/latest/

Python API: https://quinlan-lab.github.io/bedder-rs/main/bedder.html

## Example Usage
#### Reporting a single line for the a interval if it overlaps using whole-wide and none of the b interval
```bash
bedder intersect -a tests/examples/aa.bed -b tests/examples/bb.bed -g tests/examples/fake.fai --a-piece whole-wide --b-piece none
```
#### Find the closest intervals in target.bed for each interval in query.bed:
```bash
bedder closest -a query.bed -b target.bed -g genome.fai -n 1 -c distance
```
#### Default behavior maps BED score (-c 5) with sum:
```bash
bedder map -a tests/examples/map_a.bed -b tests/examples/map_b.bed -g tests/examples/fake.fai
```