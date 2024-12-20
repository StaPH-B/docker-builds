FROM mambaorg/micromamba:1.3.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG sets environment variables during the build stage
ARG NGMASTER_VER="1.0.0"
ARG MLST_VER="2.23.0"
ARG ANY2FASTA_VER="0.4.2"

LABEL base.image="mambaorg/micromamba:1.3.0"
LABEL dockerfile.version="2"
LABEL software="ngmaster"
LABEL software.version=${NGMASTER_VER}
LABEL description="In silico multi-antigen sequence typing for Neisseria gonorrhoeae (NG-MAST)"
LABEL website="https://github.com/MDU-PHL/ngmaster"
LABEL license="https://github.com/MDU-PHL/ngmaster/blob/master/LICENSE"
LABEL maintainer="Curtis kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"

# Install dependencies via apt-get; procps to get the 'ps' command for nextflow compatibility
# cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install python, pip, biopython, isPcr version 33 into base micromamba env
# cleanup conda garbage
RUN micromamba install -n base -c conda-forge -c bioconda -c defaults \
 'python>=3.7' \
 pip \
 biopython \
 any2fasta=${ANY2FASTA_VER} \
 mlst=${MLST_VER} \
 ngmaster=${NGMASTER_VER} && \
 micromamba clean -a -y

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# hardcode conda env into the PATH; set locale settings
ENV PATH="/opt/conda/bin:${PATH}" \
 LC_ALL=C.UTF-8

# set final & default working dir to /data
WORKDIR /data

# test layer
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# show help and version outputs; run the program's internal tests
RUN ngmaster --help && echo && \
 ngmaster --version && mlst --version && echo && \
 ngmaster --test

# getting unzip for unziping archive downloaded from NCBI
RUN apt-get update && apt-get install unzip curl ca-certificates -y --no-install-recommends

# so that testing outputs are in /test
WORKDIR /test

# test with an actual assembly downloaded from RefSeq
# more info on this genome here: https://www.ncbi.nlm.nih.gov/labs/data-hub/genome/GCF_013030075.1/
RUN curl -OJX GET "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/GCF_013030075.1/download?include_annotation_type=GENOME_FASTA,GENOME_GFF,RNA_FASTA,CDS_FASTA,PROT_FASTA,SEQUENCE_REPORT&filename=GCF_013030075.1.zip" \
 -H "Accept: application/zip" && \
 unzip GCF_013030075.1.zip && \
 ngmaster /test/ncbi_dataset/data/GCF_013030075.1/GCF_013030075.1_ASM1303007v1_genomic.fna > ngmaster.out.tsv && \
 cat /test/ngmaster.out.tsv