# iVar container

Main tool : [iVar](https://andersen-lab.github.io/ivar/html/manualpage.html)

Additional tools (required):
* [HTSlib](https://github.com/samtools/htslib)
* [samtools](http://www.htslib.org/)
* [bwa](http://bio-bwa.sourceforge.net/)

Also includes the 
* [artic primers](https://github.com/artic-network/artic-ncov2019.git) as they were on 2021-05-06 (ef3f1ce9f66d49ec7caa67e0425e556bd67c53de) <-- update
* A bedfile representing the amplicons (alt primers are ignored) at `/artic-ncov2019/primer_schemes/nCoV-2019/{V1,V2,V3}/nCoV-2019_amplicon.bed`
* A gff file for the reference sequence /reference/GCF_009858895.2_ASM985889v3_genomic.gff.gz

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
