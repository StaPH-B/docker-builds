# Minimap2 container

Main tool : [Minimap2](https://github.com/lh3/minimap2)

Full documentation: https://github.com/lh3/minimap2

> Minimap2 is a versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database.

# Example Usage

```
minimap2 -K 20M \
  -ax sr -t !{task.cpus} \
  -o aligned/!{sample}.sam \
  !{reference_genome} !{reads}
```
