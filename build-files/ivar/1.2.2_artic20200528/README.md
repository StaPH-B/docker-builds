# iVar container

Main tool : [iVar](https://andersen-lab.github.io/ivar/html/manualpage.html)

Additional tools:
* [seqtk](https://github.com/lh3/seqtk)
* [Minimap2](https://github.com/lh3/minimap2)
* [HTSlib](https://github.com/samtools/htslib)
* [samtools](http://www.htslib.org/)
* [bwa](http://bio-bwa.sourceforge.net/)
* [snakemake](https://snakemake.readthedocs.io/en/stable/index.html)

Also includes the 
* [artic primers](https://github.com/artic-network/artic-ncov2019.git) as they were on 2020-05-28 (ef3f1ce9f66d49ec7caa67e0425e556bd67c53de)
* A bedfile representing the amplicons (alt primers are ignored) at `/artic-ncov2019/primer_schemes/nCoV-2019/{V1,V2,V3}/nCoV-2019_amplicon.bed`
* A gff file for the reference sequence /reference/GCF_009858895.2_ASM985889v3_genomic.gff.gz

# Example Usage

```
ivar trim -e -i {bam} -b /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.bed -p {sample}.primertrim
```
```
samtools mpileup -A -d 600000 -B -Q 0 --reference /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta {bam} | \
      ivar variants -p {sample}.variants -q 20 -t 0.6 -r /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta -g /reference/GCF_009858895.2_ASM985889v3_genomic.gff
```
```
samtools mpileup -A -d 6000000 -B -Q 0 --reference /artic-ncov2019/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta {bam} | \
      ivar consensus -t 0.6 -p {sample}.consensus -n N
```
