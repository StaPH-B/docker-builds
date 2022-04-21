# IRMA container
Main tool: [IRMA](https://wonder.cdc.gov/amd/flu/irma/)
# Example Usage
```{bash}
#Paired-end files:
#USAGE:	IRMA <MODULE-config> <R1.fastq.gz/R1.fastq> <R2.fastq.gz/R2.fastq> <sample_name>

IRMA FLU Sample1_R1.fastq.gz Sample1_R2.fastq.gz Sample1

IRMA EBOLA Patient1_R1.fastq Patient1_R2.fastq MyPatient

IRMA FLU-utr Sample1_R1.fastq.gz Sample1_R2.fastq.gz Sample1WithUTRs

#Single read files:
#USAGE:	IRMA <MODULE-config> <fastq/fastq.gz> <sample_name>

IRMA FLU SingleEndIllumina.fastq.gz MyIlluminaSample

IRMA FLU-pacbio ccs_reads.fastq MyPacBioSample

IRMA FLU-pgm pgm_reads.fastq MyIonTorrentSample

```
Better documentation can be found at [https://wonder.cdc.gov/amd/flu/irma/](https://wonder.cdc.gov/amd/flu/irma/)

The manuscript can be found at [https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-3030-6](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-3030-6)
