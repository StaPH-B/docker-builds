FROM mambaorg/micromamba:2.1.1-ubuntu22.04 AS app

ARG ECTYPER_VERSION="2.0.0"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.1.1-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="ECTyper"
LABEL software.version="${ECTYPER_VERSION}"
LABEL description="Rapid assessment of genome bin quality using machine learning."
LABEL website="https://github.com/phac-nml/ecoli_serotyping"
LABEL license="https://github.com/phac-nml/ecoli_serotyping/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

RUN micromamba install --name base -c conda-forge -c bioconda ectyper=${ECTYPER_VERSION} && \
micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
LC_ALL=C.UTF-8

CMD [ "ectyper", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test 

# download genome assembly from NCBI and test ECTyper with it
# expect 1 perfect match to stx2o subtype, with COMPLETE operon designation
# https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_012224845.2/
# grep below requires both strings to be present in the same line
RUN echo "Downloading E. coli test genome and running it through ECTyper" && \
wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
ectyper -i GCA_012224845.2_ASM1222484v2_genomic.fna.gz -o ectyper-test-outdir -c 2 --verify --pathotype && \
grep 'Shiga toxin 2 subtype o complete sequence' ectyper-test-outdir/output.tsv | grep 'STEC'

# add a test with reads (Illumina) to ensure that bowtie2 & other dependencies are working
# https://www.ncbi.nlm.nih.gov/biosample/?term=SAMN07709929
# Expect O23:H15 serotype
# This strain is the typestrain for the stx2n subtype Shiga toxin operon
# grep below requires both strings to be present in the same line
RUN echo "Downloading E. coli test reads and running them through ECTyper" && \
wget -q https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR612/009/SRR6128619/SRR6128619_1.fastq.gz && \
ectyper -i SRR6128619_1.fastq.gz -o ectyper-test-outdir-reads -c 2 --verify --pathotype && \
grep 'O23:H15' ectyper-test-outdir-reads/output.tsv | grep 'stx2n'

RUN ectyper --help && \
ectyper --version && \
mash --version && \
samtools --version && \
bcftools --version && \ 
blastn -version && \
bowtie2 --version
