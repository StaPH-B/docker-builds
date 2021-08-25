# shigatyper container

Main tool : [shigatyper](https://github.com/CFSAN-Biostatistics/shigatyper)

Additional tools:
- [bcftools](http://samtools.github.io/bcftools/bcftools.html) v.1.9
- [samtools](http://www.htslib.org/) v.1.9
- [minimap2](https://github.com/lh3/minimap2) v.2.16
- [pandas](https://pandas.pydata.org/) v.0.24.2 

> ShigaTyper is a quick and easy tool designed to determine Shigella serotype using Illumina paired end reads with low computation requirement.

A full list of options can be found at [https://github.com/CFSAN-Biostatistics/shigatyper](https://github.com/CFSAN-Biostatistics/shigatyper)

# Example Usage

```
shigatyper --name sample_hits sample_R1.fastq.gz sample_R2.fastq.gz > sample_serotype.txt
```

This results in two files : 
```
$ head sample_hits.csv
,Hit,Number of reads,Length Covered,reference length,% covered,Number of variants,% accuracy
0,ipaH_c,1421,779,780,99.9,3,99.6
1,EclacY,160,270,1254,21.5,1,99.6
2,cadA,759,1886,2143,88.0,19,99.0
3,Ss_methylase,662,1830,1833,99.8,1,99.9

$ head sample_serotype.txt
sample	prediction	ipaB
test	Shigella sonnei form II	-
```
