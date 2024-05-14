# Kaptive

Main tool: [Kaptive](https://github.com/klebgenomics/Kaptive)

Additional tools:

- minimap2: 2.27

## Kaptive databases

There are few databases included in this docker image for Kaptive v2.0.8:

- Klebsiella pneumoniae species complex
  - included w/ Kaptive
- Acinetobacter baumannii
  - included w/ Kaptive

The databases (Genbank/GBK files) are located as follows in the container filesystem:

```bash
# Klebsiella pneumoniae species complex
/kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk
/kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk

# Acinetobacter baumannii
/kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk
/kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk

```

Example commands for each of these databases can be found below.

## Example Usage

```bash
# basic usage
kaptive assembly reference.gbk assembly.fasta

# K locus, A. baumannii
kaptive assembly /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk assembly.fasta
# O locus, A. baumannii
kaptive assembly /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk assembly.fasta

# K locus, K. pneumoniae
kaptive assembly /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk assembly.fasta
# O locus, K. pneumoniae
kaptive assembly /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk assembly.fasta

# K locus, V. parahaemolyticus
kaptive assembly /kaptive/reference_database/VibrioPara_Kaptivedb_K.gbk assembly.fasta
# O locus, V. parahaemolyticus
kaptive assembly /kaptive/reference_database/VibrioPara_Kaptivedb_O.gbk assembly.fasta
```