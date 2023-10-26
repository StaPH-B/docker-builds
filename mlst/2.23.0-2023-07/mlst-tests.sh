#!/bin/bash
# test commands stolen shamelessly from https://github.com/tseemann/mlst/blob/master/.travis.yml

# change into mlst root dir where it's installed in the docker image, e.g. /mlst-2.22.0
cd /mlst-*

# all below commands should exit code 0
set -euxo pipefail 

mlst --check
mlst --version
mlst --help
! mlst --doesnotexist
! mlst -q /etc
! mlst -q /etc/shadow
mlst --list | grep saureus
mlst --longlist | grep saureus
mlst -q test/example.fna.gz | grep -w 184
mlst -q test/example.gbk.gz | grep -w 184
mlst -q test/novel.fasta.bz2 | grep -w spneumoniae
gzip -d -c test/example.fna.gz | mlst -q /dev/stdin | grep -w 184
gzip -d -c test/example.gbk.gz | mlst -q /dev/stdin | grep -w 184
mlst -q --legacy --scheme sepidermidis test/example.fna.gz test/example.gbk.gz
mlst -q --csv test/example.fna.gz | grep ',184,'
mlst -q test/example.gbk.gz --json out.json && grep 'sequence_type' out.json
! mlst -q --label double_trouble test/example.gbk.gz test/example.fna.gz
mlst -q --label GDAYMATE test/example.fna.gz | grep GDAYMATE
mlst -q --novel novel.fa test/novel.fasta.bz2 && grep 'recP' novel.fa
scripts/mlst-show_seqs -s efaecium -t 111
