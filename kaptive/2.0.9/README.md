# Kaptive

Main tool: [Kaptive](https://github.com/klebgenomics/Kaptive)

Additional tools:

- ncbi-blast+ 2.3.0
- python 3.8.10
- biopython 1.81

## Kaptive databases

There are few databases included in this docker image for Kaptive v2.0.8:

- Klebsiella pneumoniae species complex
  - included w/ Kaptive
- Acinetobacter baumannii
  - included w/ Kaptive
- Vibrio parahaemolyticus
  - Located in separate GitHub repo: https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping
  - Publication: https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.001007

The databases (Genbank/GBK files) are located as follows in the container filesystem:

```bash
# Klebsiella pneumoniae species complex
/kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk
/kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk

# Acinetobacter baumannii
/kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk
/kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk

# Vibrio parahaeolyticus
/kaptive/reference_database/VibrioPara_Kaptivedb_K.gbk
/kaptive/reference_database/VibrioPara_Kaptivedb_O.gbk
```

Example commands for each of these databases can be found below.

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

# K locus, V. parahaemolyticus
kaptive.py -a assembly.fasta -k /kaptive/reference_database/VibrioPara_Kaptivedb_K.gbk
# O locus, V. parahaemolyticus
kaptive.py -a assembly.fasta -k /kaptive/reference_database/VibrioPara_Kaptivedb_O.gbk
```