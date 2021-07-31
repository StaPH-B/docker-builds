# iVar container

Main tool : [iVar](https://andersen-lab.github.io/ivar/html/manualpage.html)

Additional tools (required):
* [HTSlib](https://github.com/samtools/htslib)
* [samtools](http://www.htslib.org/)

# Example Usage

```
ivar trim -e -i {bam} -b {primer bed} -p {sample}.primertrim
```
```
samtools mpileup -A -d 8000 -B -Q 0 --reference {reference.fasta} {bam} | \
      ivar variants -p {sample}.variants -q 20 -t 0.6 -r {reference.fasta} -g {reference.gff}
```
```
samtools mpileup -A -d 8000 -B -Q 0 --reference {reference.fasta} {bam} | \
      ivar consensus -t 0.6 -p {sample}.consensus -n N
```
