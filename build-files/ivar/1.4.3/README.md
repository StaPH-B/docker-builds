# iVar container

Main tool : [iVar](https://andersen-lab.github.io/ivar/html/manualpage.html)

> iVar is a computational package that contains functions broadly useful for viral amplicon-based sequencing

Additional tools (required):

* [HTSlib](https://github.com/samtools/htslib) 1.20
* [samtools](http://www.htslib.org/) 1.20

## Example Usage

```bash
ivar trim -e -i {bam} -b {primer bed} -p {sample}.primertrim
```

```bash
samtools mpileup -A -d 8000 -B -Q 0 --reference {reference.fasta} {bam} | \
      ivar variants -p {sample}.variants -q 20 -t 0.6 -r {reference.fasta} -g {reference.gff}
```

```bash
samtools mpileup -A -d 8000 -B -Q 0 --reference {reference.fasta} {bam} | \
      ivar consensus -t 0.6 -p {sample}.consensus -n N
```

Starting with iVar version 1.4.1, the output of an aligner such as minimap2 and bwa (both included) can be piped into ivar trim directly
```bash
# index reference
bwa index reference.fasta

# run bwa and pipe into ivar (single line is split with \ for clarity)
bwa mem reference.fasta read_1.fastq.gz read_2.fastq.gz | \
  ivar trim -b primer.bed -x 3 -m 30 | \
  samtools sort | \
  samtools mpileup -aa -A -Q 0 -B -d 2000 - | \
  ivar consensus -p output_prefix -m 10 -n N -t 0.5
```
