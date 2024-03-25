#!/bin/bash -euo pipefail
echo "${PWD}"
for entry in "${PWD}"/*
do
  echo "$entry"
done

gunzip -f LIY15561A65_2022_1744_NE.assembly.gfa.gz
cat LIY15561A65_2022_1744_NE.assembly.gfa | awk 'BEGIN { FS="\t" } /^S/{ if( length($3) >= 1) print ">Contig"$2"_len"substr($4,6)"_cov"substr($5,6,5)"\n"$3}' | fold > LIY15561A65_2022_1744_NE.contigs.fasta

python mpxv-AssemblyGraph_gfaPy.py \
    -i LIY15561A65_2022_1744_NE.assembly.gfa \
    -r "/scicomp/home-pure/ick4/01.scripts/polkapox/assets/MPXV-UK_P2.noN_39086_40204.fasta" \
    -o .

