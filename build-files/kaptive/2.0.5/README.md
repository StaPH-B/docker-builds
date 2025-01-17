# Kaptive

Main tool: [Kaptive](https://github.com/katholt/Kaptive)

Additionall tools:

- ncbi-blast+ 2.3.0
- python 3.8.10
- biopython 1.81

## Example Usage

```bash
# K locus, A. baumannii
kaptive.py -a assembly.fasta -k /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk
# O locus, A. baumannii
kaptive.py -a assembly.fasta -k /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk

# K locus, K. pneumoniae
kaptive.py -a assembly.fasta -k /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk
# O locus, K. pneumoniae
kaptive.py -a assembly.fasta -k /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk
```

