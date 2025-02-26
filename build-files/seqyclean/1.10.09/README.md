# seqyclean container

Main tool : [seqyclean](https://github.com/ibest/seqyclean)

Seqyclean "cleans" NGS sequencing data. A file containing Illumina adapaters and PhiX is located at `/Adapters_plus_PhiX_174.fasta`.

# Example Usage

```
seqyclean -minlen 25 -qual -c /Adapters_plus_PhiX_174.fasta -1 {reads.R1.fastq.gz} -2 {reads.R2.fastq.gz} -o Sequencing_reads/QCed/{sample}_clean
```
