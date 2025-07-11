#!/bin/bash

labid="test"
analysis_date="2025-01-01"
samplename="test"
version="C_BIRD v2.0.0"
genome_length=5679586
phix_ratio="0.00000%"

# catch taxon & find genome size
taxon=$(awk -F '\t' '{print $1}' top_taxon.tsv)
percent=$(awk -F '\t' '{print $2}' top_taxon.tsv)
datasets summary genome taxon "$taxon" --reference > gs.json

# test plain_report.py
plain_report.py \
-d "$analysis_date" \
-i "$labid" \
-o "$taxon" \
-p "$percent" \
-a amrfinder_all.tsv \
-n  \
-l  \
-r  \
-hl1 ""\
-hl2 "" \
-hl3 "" \
-hl4 "" \
-hl5 "" \
-hl6 ""

# test html_report.py
html_report.py \
-s "$samplename" \
-t bracken.filtered.txt \
-st ts_mlst.tsv \
-a amrfinder_all.tsv \
-p plasmid.tsv \
-c "$version" \
-m top_taxon.tsv \
-f ""

# alternative source for expected genome size
jq -r '.reports[0].assembly_stats.total_sequence_length' gs.json > alt_gs.txt

# test est_coverage.py
taxid=$(cat taxid.txt)
est_coverage.py \
total_bases.txt \
"$taxid" \
alt_gs.txt \
"$genome_length"    

# test qc_report.py
qc_report.py \
"$samplename" \
fastp.html \
bracken.filtered.txt \
quast.report.tsv \
checkm2.report.tsv \
"$version" \
"$phix_ratio" \
"COVERAGE" \
"GENOME_RATIO"