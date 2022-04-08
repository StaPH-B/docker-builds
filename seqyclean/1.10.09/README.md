# seqyclean container

Main tool : [seqyclean](https://github.com/ibest/seqyclean)

Full documentation: https://github.com/ibest/seqyclean

Seqyclean "cleans" NGS sequencing data.
A file containing Illumina adapters and PhiX is located at `/Adapters_plus_PhiX_174.fasta`.

# Example Usage

```
seqyclean -minlen 25 -qual -c /Adapters_plus_PhiX_174.fasta -1 sample_R1.fastq.gz -2 sample_R2.fastq.gz -o sample_clean -gz
```
