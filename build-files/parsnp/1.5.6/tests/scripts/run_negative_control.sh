#!/bin/bash
# This script pulls real data and runs parsnp on it.
# It should exclude one Salmonella enterica genome for being too unrelated to the Escherichia coli reference genome.

mkdir -p neg_control/input_dir
mkdir -p neg_control/reference
cd neg_control/input_dir
wget \
    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/703/365/GCA_000703365.1_Ec2011C-3609/GCA_000703365.1_Ec2011C-3609_genomic.fna.gz \
    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/766/575/GCA_016766575.1_PDT000040717.5/GCA_016766575.1_PDT000040717.5_genomic.fna.gz \
    https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/748/565/GCA_000748565.2_ASM74856v2/GCA_000748565.2_ASM74856v2_genomic.fna.gz
gunzip ./*.gz
mv GCA_000703365.1_Ec2011C-3609_genomic.fna ../reference/
cd ../

OUTGROUP_STRAIN="GCA_000703365.1_Ec2011C-3609_genomic.fna"

# Run using FastTree without -c
FILTER_OUTDIR=outdir_parsnp_filter
parsnp \
-d input_dir \
-o  $FILTER_OUTDIR \
--use-fasttree \
-v \
-r reference/$OUTGROUP_STRAIN



