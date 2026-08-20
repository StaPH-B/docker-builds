#!/bin/bash 

set -euo pipefail

FASTA=GCF_000240185.1_ASM24018v2_genomic.fna.gz
FASTA_URL=https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/240/185/GCF_000240185.1_ASM24018v2/$FASTA

gambit --version

wget $FASTA_URL
gambit query $FASTA -o test_output.csv
grep "Klebsiella pneumoniae" test_output.csv
