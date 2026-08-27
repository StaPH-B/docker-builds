# wtdbg2 container

Main tool: [wtdbg2](https://github.com/ruanjue/wtdbg2)
  
Code repository: https://github.com/ruanjue/wtdbg2

Additional tools:
- minimap2: 2.26-r1175
- samtools: 1.19.2
- bwa: 0.7.17-r1188

Basic information on how to use this tool:
- executable: `wtdbg2`, `wtpoa-cns`
- help: `-h`, `--help`
- version: `-V`
- description: Wtdbg2 is a de novo sequence assembler for long noisy reads produced by PacBio or Oxford Nanopore Technologies (ONT).

Additional information:

Ruan, J. and Li, H. (2019) Fast and accurate long-read assembly with wtdbg2. Nat Methods doi:10.1038/s41592-019-0669-3
  
Full documentation: https://github.com/ruanjue/wtdbg2

## Example Usage

```bash
# quick start with wtdbg2.pl
wtdbg2.pl -t 16 -x rs -g 4.6m -o dbg reads.fa.gz

# Step by step commandlines
# assemble long reads
wtdbg2 -x rs -g 4.6m -i reads.fa.gz -t 16 -fo dbg

# derive consensus
wtpoa-cns -t 16 -i dbg.ctg.lay.gz -fo dbg.raw.fa

# polish consensus (not necessary if you want to polish the assemblies using other tools)
minimap2 -t16 -ax map-pb -r2k dbg.raw.fa reads.fa.gz | samtools sort -@4 > dbg.bam
samtools view -F0x900 dbg.bam | wtpoa-cns -t 16 -d dbg.raw.fa -i - -fo dbg.cns.fa

# Addtional polishing with short reads
bwa index dbg.cns.fa
bwa mem -t 16 dbg.cns.fa sr.1.fa sr.2.fa | samtools sort -O SAM | wtpoa-cns -t 16 -x sam-sr -d dbg.cns.fa -i - -fo dbg.srp.fa

```
