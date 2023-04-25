# iVar container

Main tool : [iVar](https://andersen-lab.github.io/ivar/html/manualpage.html)

> iVar is a computational package that contains functions broadly useful for viral amplicon-based sequencing

Additional tools (required):

* [HTSlib](https://github.com/samtools/htslib) 1.17
* [samtools](http://www.htslib.org/) 1.17
* [bedtools](https://bedtools.readthedocs.io/en/latest/) 2.30.0
* python 3.10.6

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
