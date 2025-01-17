# NCBI table2asn

Main tool : [table2asn](https://www.ncbi.nlm.nih.gov/genbank/table2asn/)

Full documentation: [README](https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/DOCUMENTATION/table2asn_readme.txt)

> table2asn is a command-line program that creates sequence records for submission to GenBank

## Example Usage

```bash
# Single non-genome submission: a particular .fsa file, and only 1 sequence in the .fsa file and the source information is in the definition line of the .fsa file:
table2asn -t template.sbt -i x.fsa -V v

# Batch non-genome submission: a directory that contains .fsa files, and multiple sequences per file, and the source information is in the definition line of the .fsa files:
table2asn -t template.sbt -indir path_to_files -a s -V v

# Genome submission: a directory that contains multiple .fsa files of a single genome, and one or more sequences per file and the source information is in the definition line of the .fsa files:
table2asn -t template.sbt -indir path_to_files -M n -Z

# Genome submission for the most common gapped situation (= runs of 10 or more Ns represent a gap, and there are no gaps of completely unknown size, and the evidence for linkage across the gaps is "paired-ends"), and the source information is in the definition line of the .fsa files:
table2asn -t template -indir path_to_files -M n -Z -gaps-min 10 -l paired-ends
```
