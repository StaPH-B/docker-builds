ARG ARTIC_VER=1.10.0

FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

ARG ARTIC_VER

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="artic"
LABEL software.version="${ARTIC_VER}"
LABEL description="A bioinformatics pipeline for working with virus sequencing data sequenced with nanopore"
LABEL website="https://github.com/artic-network/fieldbioinformatics"
LABEL license="https://github.com/artic-network/fieldbioinformatics/blob/master/LICENSE"
LABEL sop="https://artic.network/fieldbioinformatics/fieldbioinformatics-sop.html"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

USER root
WORKDIR /

RUN micromamba create -n artic -y -c conda-forge -c bioconda \
    artic=${ARTIC_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="${PATH}:/opt/conda/envs/artic/bin/" \
    CONDA_PREFIX="/opt/conda/envs/artic/" \
    LC_ALL=C.UTF-8

RUN artic_get_models

CMD ["artic","--help"]

WORKDIR /data


FROM app AS test
ARG ARTIC_VER

RUN artic --help && \
    artic --version

WORKDIR /

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*


RUN wget -q https://github.com/artic-network/fieldbioinformatics/archive/refs/tags/v${ARTIC_VER}.tar.gz && \
    tar -vxf v${ARTIC_VER}.tar.gz && \
    cd /fieldbioinformatics-${ARTIC_VER} && ls && \
    bash ./test-runner.sh clair3

WORKDIR /test

# using on "real" data (sample files were not sequenced with version 5.3.2 primers)
# filtering fastq files
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR224/050/SRR22452250/SRR22452250_1.fastq.gz && \
    artic guppyplex --min-length 400 --max-length 700  --directory . --prefix SRR22452250_1.fastq.gz --output SRR22452250_1_filtered.fastq

# running artic minion with user-provided bed and reference
RUN wget -q https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.primer.bed && \
    wget -q https://raw.githubusercontent.com/artic-network/primer-schemes/master/nCoV-2019/V5.3.2/SARS-CoV-2.reference.fasta

RUN artic minion --normalise 200 --threads 4 --model r941_prom_sup_g5014 --read-file SRR22452250_1_filtered.fastq --bed SARS-CoV-2.primer.bed --ref SARS-CoV-2.reference.fasta test1 && \
    ls test1*

# running artic as it pulls schemes from github
RUN artic minion --normalise 200 --threads 4 --model r941_prom_sup_g5014 --read-file SRR22452250_1_filtered.fastq --scheme-name sars-cov-2  --scheme-version  V5.3.2 --scheme-length 400 test2 && \
    ls test2*

RUN echo "included models" && \
    ls ${CONDA_PREFIX}/bin/models

RUN micromamba list -n artic
