# SeqSero2 docker image

> SeqSero2: Salmonella enterica serotype prediction from genome sequencing data

Main tool : [SeqSero2](https://github.com/denglab/SeqSero2)

Additional tools:

- spades 3.15.5
- ncbi-blast+ 2.6.0
- python 2.7.17
- python3 3.6.9
- biopython 1.73
- samtools 1.8
- bedtools 2.26.0
- SalmID 0.11
- bwa 0.7.17-r1188
- sra-toolkit 2.8.2

## Example Usage

```bash
# paired end Illumina reads as input for allele mode
$ SeqSero2_package.py \
      -i SRR6082043_1.fastq.gz SRR6082043_2.fastq.gz \
      -t 2 \
      -m a \
      -d SRR6082043-seqsero2-reads-allele-mode \
      -n SRR6082043 \
      -p 2
[bam_sort_core] merging from 0 files and 2 in-memory blocks...
building database...
mapping...
check samtools version: 1.9
assembling...
blasting... 

Sample name:    SRR6082043
Output directory:       /test/SRR6082043-seqsero2-reads-allele-mode
Input files:    /test/SRR6082043_1.fastq.gz     /test/SRR6082043_2.fastq.gz
O antigen prediction:   7
H1 antigen prediction(fliC):    r
H2 antigen prediction(fljB):    1,5
Predicted identification:       Salmonella enterica subspecies enterica (subspecies I)
Predicted antigenic profile:    7:r:1,5
Predicted serotype:     Infantis
Note:

# genome assembly FASTA as input for kmer mode
$ SeqSero2_package.py \
      -i GCA_007765495.1.genomic.fna \
      -t 4 \
      -m k \
      -d GCA_007765495.1-seqsero2-assembly-kmer-mode \
      -n GCA_007765495.1 \
      -p 2
Sample name:    GCA_007765495.1
Output directory:       /test/GCA_007765495.1-seqsero2-assembly-kmer-mode
Input files:    GCA_007765495.1.genomic.fna
O antigen prediction:   7
H1 antigen prediction(fliC):    r
H2 antigen prediction(fljB):    1,5
Predicted identification:       Salmonella enterica subspecies enterica (subspecies I)
Predicted antigenic profile:    7:r:1,5
Predicted serotype:     Infantis
Note:
```
