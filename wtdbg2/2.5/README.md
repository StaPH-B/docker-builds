# Wtdbg2 container

Main tool : [Wtdbg2](https://github.com/ruanjue/wtdbg2)

Full documentation: https://github.com/ruanjue/wtdbg2

> Wtdbg2 is a de novo sequence assembler for long noisy reads produced by PacBio or Oxford Nanopore Technologies (ONT).

# Example Usage

From github page
```
#quick start with wtdbg2.pl
./wtdbg2.pl -t 16 -x rs -g 4.6m -o dbg reads.fa.gz

# Step by step commandlines
# assemble long reads
./wtdbg2 -x rs -g 4.6m -i reads.fa.gz -t 16 -fo dbg

# derive consensus
./wtpoa-cns -t 16 -i dbg.ctg.lay.gz -fo dbg.raw.fa

# polish consensus, not necessary if you want to polish the assemblies using other tools
minimap2 -t16 -ax map-pb -r2k dbg.raw.fa reads.fa.gz | samtools sort -@4 >dbg.bam
samtools view -F0x900 dbg.bam | ./wtpoa-cns -t 16 -d dbg.raw.fa -i - -fo dbg.cns.fa

# Addtional polishment using short reads
bwa index dbg.cns.fa
bwa mem -t 16 dbg.cns.fa sr.1.fa sr.2.fa | samtools sort -O SAM | ./wtpoa-cns -t 16 -x sam-sr -d dbg.cns.fa -i - -fo dbg.srp.fa
```
