#!/bin/bash

# Download test data
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa -O burk_wgs_pos_ctrl.fa
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_16S.fa -O burk_16S_neg_ctrl.fa

# Get taxonomic assignments for your data
checkm2 predict --threads 4 \
    --input burk_wgs_pos_ctrl.fa \
    burk_16S_neg_ctrl.fa \
    --output-directory tests_output/ 

# run checksum on files
sha256sum burk_wgs_pos_ctrl.fa > burk_wgs_checksum.txt
sha256sum burk_16S_neg_ctrl.fa > burk_16S_checksum.txt
sha256sum tests_output/quality_report.tsv > quality_report_checksum.txt
