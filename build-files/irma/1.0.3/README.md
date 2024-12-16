# IRMA container
Main tool: [IRMA](https://wonder.cdc.gov/amd/flu/irma/)

IRMA was designed for the robust assembly, variant calling, and phasing of highly variable RNA viruses. Currently IRMA is deployed with modules for influenza, ebolavirus and coronavirus.

# Example Usage
```{bash}
#Paired-end files:
#USAGE:	IRMA <MODULE-config> <R1.fastq.gz/R1.fastq> <R2.fastq.gz/R2.fastq> <sample_name>

#WARNING!!!! IRMA expects Illumunia Fastq formatting: 
@<instrument>:<run number>:<flowcell ID>:<lane>:<tile>:<xpos>:<y-pos> <read>:<is filtered>:<control number>:<index> 

# If you are downloading samples from SRA please use the following code or IRMA's outputs will be empty
#SRR17940172 is used for an example; replace this with SRR id of fastq files that are needed
awk '{if(NR%2==1) $0=sprintf($1); print;}' SRR17940172_1.fastq > SRR17940172_1a.fastq && \
awk '{if(NR%4==1) $0=sprintf($1" 1:N:18:NULL"); print;}' SRR17940172_1a.fastq > SRR17940172_1.fastq && \
awk '{if(NR%2==1) $0=sprintf($1); print;}' SRR17940172_2.fastq > SRR17940172_2a.fastq && \
awk '{if(NR%4==1) $0=sprintf($1" 2:N:18:NULL"); print;}' SRR17940172_2a.fastq > SRR17940172_2.fastq

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
