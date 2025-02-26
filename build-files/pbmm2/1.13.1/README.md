# pbmm2 container

Main tool: [pbmm2](https://github.com/PacificBiosciences/pbmm2)
  
Code repository: https://github.com/PacificBiosciences/pbmm2

Basic information on how to use this tool:
- executable: pbmm2
- help: -h, --help
- version: --version
- description: 
>pbmm2 is a SMRT C++ wrapper for minimap2's C API. Its purpose is to support native PacBio in- and output, provide sets of recommended parameters, generate sorted output on-the-fly, and postprocess alignments. 

Full documentation: https://github.com/PacificBiosciences/pbmm2

## Example Usage

```bash
# index
pbmm2 index [options] <ref.fa|xml> <out.mmi>
# align
pbmm2 align [options] <ref.fa|xml|mmi> <in.bam|xml|fa|fq> [out.aligned.bam|xml]
```