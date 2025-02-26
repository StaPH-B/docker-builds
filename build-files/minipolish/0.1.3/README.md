# minipolish and miniasm container

Main tool : [minipolish](https://github.com/rrwick/Minipolish) and [miniasm](https://github.com/lh3/miniasm)

Other tools :
- [racon](https://github.com/isovic/racon) 
- [minimap2](https://github.com/lh3/minimap2)

From minipolish's [readme](https://github.com/rrwick/Minipolish):

> Miniasm is a great long-read assembly tool: straight-forward, effective and very fast. However, it does not include a polishing step, so its assemblies have a high error rate – they are essentially made of stitched-together pieces of long reads.
>
> Racon is a great polishing tool that can be used to clean up assembly errors. It's also very fast and well suited for long-read data. However, it operates on FASTA files, not the GFA graphs that miniasm makes.
>
> That's where Minipolish comes in. With a single command, it will use Racon to polish up a miniasm assembly, while keeping the assembly in graph form.

# Example Usage

```
miniasm_and_minipolish.sh input.fastq $threads > output.gfa
```
