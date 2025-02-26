#!/bin/bash

# Download test data
wget -nv https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/rdp/2.14/16S_rRNA_gene.Burkholderia_pseudomallei.2002721184.AY305776.1.fasta -O 16S_test.fa
wget -nv https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/rdp/2.14/18S_rRNA_gene.Homo_sapiens.T2T-CHM13v2.0.Chromosome13.fasta -O 18S_test.fa

# Get taxonomic assignments for your data
classifier classify -o taxa_16S_test.txt 16S_test.fa
classifier classify -o taxa_18S_test.txt 18S_test.fa

# run checksum on files
sha256sum 16S_test.fa > 16S_checksum.txt
sha256sum 18S_test.fa > 18S_checksum.txt




