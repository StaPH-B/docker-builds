#/usr/bin/bash

shigatyper -h
shigatyper --version

wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz && \
tar -vxzf sratoolkit.tar.gz && \
rm sratoolkit.tar.gz

PATH="$PATH:/data/sratoolkit.2.9.2-ubuntu64/bin"

fasterq-dump SRR8186675
fasterq-dump SRR7738178

shigatyper --R1 SRR8186675_1.fastq --R2 SRR8186675_2.fastq --name SRR8186675
shigatyper --R1 SRR7738178_1.fastq --R2 SRR7738178_2.fastq --name SRR7738178
