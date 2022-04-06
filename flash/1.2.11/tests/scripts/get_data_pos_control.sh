#!/bin/bash
# This script downloads read files from NCBI for SRR5481494 (https://www.ncbi.nlm.nih.gov/sra/SRR5481494).

DATADIR=/data
mkdir -p $DATADIR

# Download raw reads from ENA FTP site
wget -nv ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR548/004/SRR5481494/SRR5481494_1.fastq.gz -O $DATADIR/R1.fastq.gz
wget -nv ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR548/004/SRR5481494/SRR5481494_2.fastq.gz -O $DATADIR/R2.fastq.gz
