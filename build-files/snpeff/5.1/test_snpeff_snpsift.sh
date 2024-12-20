#!/bin/bash
# This script is to test that the program SnpEff runs as expected.

# Get annotation vcf file data.
wget -nv https://sourceforge.net/projects/snpeff/files/demo.1kg.vcf -O demo.vcf

# Inspect the first five lines of the demo.vcf file.
echo "*****TAKE A LOOK AT THE FIRST 5 LINES OF THE DEMO.VCF FILE.*****"
grep -v "^#" demo.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g" 

# Download human genome reference hg19.
snpeff download -v hg19

# Annotate the demo.vcf file with the hg19 data.
snpeff hg19 demo.vcf > annotated.vcf
# More SnpEff options and features are available at https://pcingola.github.io/SnpEff/se_introduction/

# Inspect the first five lines of the annotated.vcf file. 
echo "*****TAKE A LOOK AT THE FIRST 5 LINES OF THE ANNOTATED.VCF FILE.*****"
grep -v "^#"  annotated.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g" 

# SnpSift is a toolbox that allows you to filter and manipulate annotated files.
# Using SnpSift, filter out samples in the annotated.vcf file with quality less than 30. 
cat annotated.vcf | snpsift filter "(QUAL>=30)" > filtered.vcf
# More SnpSift options and features are available at https://pcingola.github.io/SnpEff/ss_introduction/

# Inspect the first five lines of the filtered.vcf file.
echo "*****TAKE A LOOK AT THE FIRST 5 LINES OF THE FILTERED.VCF FILE.*****" 
grep -v "^#"  filtered.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g" 

echo "*****TEST IS COMPLETE.*****"


