# Samclip container

Main tool: [samclip](https://github.com/tseemann/samclip)

Basic information on how to use this tool:
- executable: ./samclip
- help: -h, --help
- version: -V, --version
- description: Filter SAM file for soft and hard clipped alignments

## Example Usage

Basic command to clip ends of reads
```bash
samclip --ref ref.fa < in.sam > out.sam
```

Integrate samclip with other tools like bwa and samtools
```bash
bwa mem ref.fa R1.fq R2.fq | samclip --ref ref.fa | samtools sort > out.bam 
```

