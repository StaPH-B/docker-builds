# Trimmomatic container

Main tool : [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)

Full documentation: http://www.usadellab.org/cms/?page=trimmomatic

> A flexible read trimming tool for Illumina NGS data

# Example Usage

From http://www.usadellab.org/cms/?page=trimmomatic

```
# Paired end
java -jar trimmomatic-0.39.jar PE input_forward.fq.gz input_reverse.fq.gz output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz ILLUMINACLIP:TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36
```
