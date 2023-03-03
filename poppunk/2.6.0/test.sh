#!/bin/bash
set -euxo pipefail

# Download 100 S. Pneumo assemblies from GPS Public Data on ENA
mkdir assemblies
while read link; do
  wget -q -P assemblies $link;
done < ftps.txt

# Generate r-file for creating PopPUNK database
for FILE in assemblies/*; do
    printf $(basename -s .contigs.fa.gz $FILE)'\t'$FILE'\n' >> rfile.txt;
done

# Build PopPUNK database from the assemblies
poppunk --create-db --output database --r-files rfile.txt --threads $(nproc)
poppunk --fit-model bgmm --ref-db database

# Assign clusters on the same assemblies using the built database
# the sample names are modified as PopPUNK reject samples with names that are already in the database
sed 's/^/prefix_/' rfile.txt > qfile.txt
poppunk_assign --db database --query qfile.txt --output output --threads $(nproc)

# Compare the database clusters and assigned clusters of the assemblies
sed 's/^prefix_//' output/output_clusters.csv | awk 'NR == 1; NR > 1 { print $0 | "sort" }' > assigned.csv
awk 'NR == 1; NR > 1 { print $0 | "sort" }' database/database_clusters.csv > database.csv
cmp assigned.csv database.csv