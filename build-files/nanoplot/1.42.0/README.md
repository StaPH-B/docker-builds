# NanoPlot container

Main tool : [NanoPlot](https://github.com/wdecoster/NanoPlot)

Full documentation: [https://github.com/wdecoster/NanoPlot](https://github.com/wdecoster/NanoPlot)

Plotting tool for long read sequencing data and alignments.

## Example Usage

```bash
# pass in the sequencing_summary.txt file produced by Guppy/Dorado basecaller
NanoPlot --summary sequencing_summary.txt --N50 --loglength -t 4 -o nanoplot-out
```
