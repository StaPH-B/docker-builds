ARG PASTY_VERSION="1.0.2"
# formatted for apt version syntax
ARG BLAST_VERSION="2.12.0+ds-3build1" 

FROM ubuntu:jammy as app

# have to re-instatiate these variables
ARG PASTY_VERSION
ARG BLAST_VERSION

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pasty"
LABEL software.version="${PASTY_VERSION}"
LABEL description="In silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies"
LABEL website="https://github.com/rpetit3/pasty"
LABEL license="https://github.com/rpetit3/pasty/blob/main/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="curtis.kapsak@theiagen.com"

# install dependencies
# ncbi-blast+ version in apt for ubuntu:jammy = v2.12.0 
# python v3.10.6
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3 \
  python3-pip \
  ncbi-blast+=${BLAST_VERSION} \
  wget \
  ca-certificates \
  procps && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install python deps
RUN pip3 install executor rich-click

# download pasty; make /data
RUN echo "downloading pasty source code..." && \
  wget -q https://github.com/rpetit3/pasty/archive/refs/tags/v${PASTY_VERSION}.tar.gz && \
  tar -zxf v${PASTY_VERSION}.tar.gz && \
  rm -rf v${PASTY_VERSION}.tar.gz && \
  mkdir /data 

# set $PATH
# set perl locale settings for singularity compatibility
ENV PATH="${PATH}:/pasty-${PASTY_VERSION}/bin"\
  LC_ALL=C.UTF-8

# final working directory is /data
WORKDIR /data

# testing layer starts here
FROM app as test

# re-instatiate for use below in test layer
ARG PASTY_VERSION

# running the below test commands from the root pasty directory
WORKDIR /pasty-${PASTY_VERSION}

# shamelessly stolen and modified from https://github.com/rpetit3/pasty/blob/main/.github/workflows/test-pasty.yml
RUN echo "O1-GCF_000504045" && \
    pasty --assembly test/O1-GCF_000504045.fna.gz --prefix O1-GCF_000504045 && \
    cat O1-GCF_000504045.tsv && \
    cat O1-GCF_000504045.details.tsv && \
    echo "O2-GCF_000006765" && \
    pasty --assembly test/O2-GCF_000006765.fna.gz --prefix O2-GCF_000006765 --outdir O2 && \
    cat O2/O2-GCF_000006765.tsv && \
    cat O2/O2-GCF_000006765.details.tsv && \
    echo "O3-GCF_000271365" && \
    pasty --assembly test/O3-GCF_000271365.fna.gz --prefix O3-GCF_000271365 --outdir O3 && \
    cat O3/O3-GCF_000271365.tsv && \
    cat O3/O3-GCF_000271365.details.tsv && \
    echo "O4-GCF_024652945" && \
    pasty --assembly test/O4-GCF_024652945.fna.gz --prefix O4-GCF_024652945 --outdir O4 && \
    cat O4/O4-GCF_024652945.tsv && \
    cat O4/O4-GCF_024652945.details.tsv && \
    echo "O6-GCF_001457615" && \
    pasty --assembly test/O6-GCF_001457615.fna.gz --prefix O6-GCF_001457615 && \
    cat O6-GCF_001457615.tsv && \
    cat O6-GCF_001457615.details.tsv && \
    echo "O7-GCF_001482325" && \
    pasty --assembly test/O7-GCF_001482325.fna.gz --prefix O7-GCF_001482325 && \
    cat O7-GCF_001482325.tsv && \
    cat O7-GCF_001482325.details.tsv && \
    echo "O9-GCF_002075065" && \
    pasty --assembly test/O9-GCF_002075065.fna.gz --prefix O9-GCF_002075065 && \
    cat O9-GCF_002075065.tsv && \
    cat O9-GCF_002075065.details.tsv && \
    echo "O10-GCF_009676765" && \
    pasty --assembly test/O10-GCF_009676765.fna.gz --prefix O10-GCF_009676765 && \
    cat O10-GCF_009676765.tsv && \
    cat O10-GCF_009676765.details.tsv && \
    echo "O11-GCF_002192495" && \
    pasty --assembly test/O11-GCF_002192495.fna.gz --prefix O11-GCF_002192495 && \
    cat O11-GCF_002192495.tsv && \
    cat O11-GCF_002192495.details.tsv && \
    echo "O12-GCF_000981825" && \
    pasty --assembly test/O12-GCF_000981825.fna.gz --prefix O12-GCF_000981825 && \
    cat O12-GCF_000981825.tsv && \
    cat O12-GCF_000981825.details.tsv && \
    echo "NT-GCF_000292685" && \
    pasty --assembly test/NT-GCF_000292685.fna.gz --prefix NT-GCF_000292685 && \
    cat NT-GCF_000292685.tsv && \
    cat NT-GCF_000292685.details.tsv && \
    echo "empty" && \
    pasty --assembly test/empty.fasta --prefix empty && \
    cat empty.tsv && \
    cat empty.details.tsv && \
    echo "not-a-fasta" && \
    pasty --assembly test/not-a-fasta.fasta --prefix not-a-fasta && \
    cat not-a-fasta.tsv && \
    cat not-a-fasta.details.tsv && \
    echo "poor" && \
    pasty --assembly test/poor.fasta --prefix poor --outdir poor && \
    cat poor/poor.tsv && \
    cat poor/poor.details.tsv

# print help and version info
RUN pasty --help && \
    pasty --version