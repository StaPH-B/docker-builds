# racon container

Main tool : [racon](https://github.com/lbcb-sci/racon)

Consensus module for raw de novo DNA assembly of long uncorrected reads.

Can be used for polishing de novo assemblies as well as for polishing long reads.

# Example Usage

```
racon --match 8 --mismatch -6 --gap -8 --window-length 500 --threads {threads} {input.reads} {input.alignment} {input.assembly}
```
