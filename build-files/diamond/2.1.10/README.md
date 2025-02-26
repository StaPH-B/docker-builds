# diamond container

Main tool: [diamond](https://github.com/bbuchfink/diamond)
  
Code repository: https://github.com/bbuchfink/diamond

Additional tools:
- ncbi-blast+ : 2.12.0

Basic information on how to use this tool:
- executable: diamond
- help: help
- version: version
- description: DIAMOND is a sequence aligner for protein and translated DNA searches, designed for high performance analysis of big sequence data. The key features are:

  - Pairwise alignment of proteins and translated DNA at 100x-10,000x speed of BLAST.
  - Protein clustering of up to tens of billions of proteins
  - Frameshift alignments for long read analysis.
  - Low resource requirements and suitable for running on standard desktops or laptops.
  - Various output formats, including BLAST pairwise, tabular and XML, as well as taxonomic classification.

Full documentation: https://github.com/bbuchfink/diamond/wiki

## Example Usage

```bash
# Protein alignment
diamond makedb --in proteins.fa -d db
diamond blastp -q query.fa -d db -o out.tsv --very-sensitive
# Protein clustering
diamond cluster -d proteins.fa -o clusters.tsv --approx-id 40 -M 12G --header
```