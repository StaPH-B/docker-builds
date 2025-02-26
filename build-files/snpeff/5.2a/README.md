# snpeff container
Main tool: [snpeff](https://pcingola.github.io/SnpEff/)

Additional tools:
SNPSift version 5.1

> Genomic variant annotations, and functional effect prediction toolbox.

This Dockerfile has made an attempt to allow uses to use the scripts included with SnpEff. Not all the scripts are tested before deployment, so please [submit an issue](https://github.com/StaPH-B/docker-builds/issues) for any use-cases that aren't working with the corresponding error message.

Command line options: [https://pcingola.github.io/SnpEff/se_commandline/](https://pcingola.github.io/SnpEff/se_commandline/)
# Example Usage
### This example was taken from the test written for this image using human reference genome HG-19 and demo.1kg.vcf.

```{bash}

# To view the list of available SnpEff databases that may be used for annotation.
snpeff databases

# Get annotation vcf file data.
wget -nv https://sourceforge.net/projects/snpeff/files/demo.1kg.vcf -O demo.vcf

# Inspect the first five lines of the demo.vcf file.
grep -v "^#" demo.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g" 

# Using SnpEff, download human genome reference hg19.
snpeff download -v hg19

# Annotate the demo.vcf file with the hg19 data.
snpeff hg19 demo.vcf > annotated.vcf

# Inspect the first five lines of the annotated.vcf file. 
grep -v "^#"  annotated.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g" 

# SnpSift is a toolbox that allows you to filter and manipulate annotated files.
# Using SnpSift, filter out samples in the annotated.vcf file with quality less than 30. 
cat annotated.vcf | snpsift filter "(QUAL>=30)" > filtered.vcf

# Inspect the first five lines of the filtered.vcf file. 
grep -v "^#"  filtered.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g"

```

Additional usage examples are available at [https://pcingola.github.io/SnpEff/examples/](https://pcingola.github.io/SnpEff/examples/)

Additional SnpEff options and features are available at [https://pcingola.github.io/SnpEff/se_introduction/](https://pcingola.github.io/SnpEff/se_introduction/)

Additional SnpSift options and features are available at [https://pcingola.github.io/SnpEff/ss_introduction/](https://pcingola.github.io/SnpEff/ss_introduction/)

SnpEff and SnpSift can perform annotation, primary impact assessment and variants filtering, as well as many other tasks beyond the scope of this protocol. The software developers highly recommend reading their comprehensive documentation available [here](https://pcingola.github.io/SnpEff/adds/VCFannotationformat_v1.0.pdf)
