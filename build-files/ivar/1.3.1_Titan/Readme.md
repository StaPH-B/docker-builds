# iVar container

Main tool : [iVar](https://andersen-lab.github.io/ivar/html/manualpage.html)

Additional tools (required):
* [HTSlib](https://github.com/samtools/htslib)
* [samtools](http://www.htslib.org/)
* [bwa](http://bio-bwa.sourceforge.net/)
* [ivar_variants_to_vcf.py](https://github.com/nf-core/viralrecon/blob/master/bin/ivar_variants_to_vcf.py)

Also includes the 
* [artic primers](https://github.com/artic-network/artic-ncov2019.git) as they were on 2021-05-06 (7e359dae37d894b40ae7e35c3582f14244ef4d36)
* A primer bedfile `/artic-ncov2019/primer_schemes/nCoV-2019/{V1,V2,V3}/nCoV-2019.primer.bed`
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
```
ivar_variants_to_vcf.py ivar-variants.tsv ivar-variants.vcf
```
