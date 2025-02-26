#!/usr/bin/env bash

# test for POLCA
wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz
wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz
wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa
polca.sh -a SRR13957123.consensus.fa -r 'SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz'
