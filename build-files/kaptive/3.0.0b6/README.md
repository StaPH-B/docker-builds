# Kaptive Container

Main tool: [Kaptive](https://github.com/klebgenomics/Kaptive)

Additional tools:

- minimap2 2.28
- python 3.10.12
- biopython 1.84
- matplotlib 3.9.2
- dna-features-viewer 3.1.3
- numpy 2.1.3

## Kaptive databases

There are few databases included in this docker image:

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
kaptive.py assembly /kaptive/reference_database/Acinetobacter_baumannii_k_locus_primary_reference.gbk assembly.fasta -o outfile.txt
# O locus, A. baumannii
kaptive.py assembly /kaptive/reference_database/Acinetobacter_baumannii_OC_locus_primary_reference.gbk assembly.fasta -o outfile.txt

# K locus, K. pneumoniae
kaptive.py assembly /kaptive/reference_database/Klebsiella_k_locus_primary_reference.gbk assembly.fasta -o outfile.txt
# O locus, K. pneumoniae
kaptive.py assembly /kaptive/reference_database/Klebsiella_o_locus_primary_reference.gbk assembly.fasta -o outfile.txt

# K locus, V. parahaemolyticus
kaptive.py assembly /kaptive/reference_database/VibrioPara_Kaptivedb_K.gbk assembly.fasta -o outfile.txt
# O locus, V. parahaemolyticus
kaptive.py assembly /kaptive/reference_database/VibrioPara_Kaptivedb_O.gbk assembly.fasta -o outfile.txt
```
