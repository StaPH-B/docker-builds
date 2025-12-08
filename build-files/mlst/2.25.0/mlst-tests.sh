#!/bin/bash
# test commands stolen shamelessly from https://github.com/tseemann/mlst/blob/master/.travis.yml
# updated upon v2.25.0 release since tests were also updated in this version. See https://github.com/tseemann/mlst/compare/v2.23.0...v2.25.0

# change into mlst root dir where it's installed in the docker image, e.g. /mlst-2.22.0
cd /mlst-*

# all below commands should exit code 0
set -euxo pipefail 

# Test mlst --check
mlst --check
# Test mlst --version
mlst --version
# Test mlst --help
mlst --help
# Test invalid option
! mlst --doesnotexist
# Test invalid directory /etc
! mlst -q /etc
# Test invalid file /etc/shadow
! mlst -q /etc/shadow
# Test list scheme (saureus)
mlst --list | grep saureus
# Test longlist scheme (saureus)
mlst --longlist | grep saureus
# Test example.fna.gz
mlst -q test/example.fna.gz | grep -w 184
# Test example.gbk.gz
mlst -q test/example.gbk.gz | grep -w 184
# Test novel.fasta.bz2
mlst -q test/novel.fasta.bz2 | grep -w leptospira_2
# Test stdin with fna.gz
gzip -d -c test/example.fna.gz | mlst -q /dev/stdin | grep -w 184
# Test stdin with gbk.gz
gzip -d -c test/example.gbk.gz | mlst -q /dev/stdin | grep -w 184
# Test legacy scheme
mlst -q --legacy --scheme sepidermidis test/example.fna.gz test/example.gbk.gz
# Test CSV output
mlst -q --csv test/example.fna.gz | grep ',184,'
# Test JSON output
mlst -q test/example.gbk.gz --json out.json && grep 'sequence_type' out.json
# Test duplicate label (should fail)
! mlst -q --label double_trouble test/example.gbk.gz test/example.fna.gz
# Test custom label
mlst -q --label GDAYMATE test/example.fna.gz | grep GDAYMATE
# test novel alleles
mlst -q --novel novel.fa test/novel.fasta.bz2 && grep 'mreA' novel.fa
# test issue 146 bug
mlst -q test/issue146.fa | grep -F 'purE(25)'
# Test mlst-show_seqs
scripts/mlst-show_seqs -s efaecium -t 111
