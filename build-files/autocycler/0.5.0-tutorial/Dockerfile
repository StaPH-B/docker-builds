ARG AUTOCYCLER_VER="0.5.0"

FROM mambaorg/micromamba:2.3.0-ubuntu22.04 AS app

ARG AUTOCYCLER_VER

USER root
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Autocycler"
LABEL software.version="${AUTOCYCLER_VER}"
LABEL description="generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Autocycler"
LABEL license="https://github.com/rrwick/Autocycler/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \ 
    parallel && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get conda environment file for extra tools
RUN wget -q https://github.com/rrwick/Autocycler/archive/refs/tags/v${AUTOCYCLER_VER}.tar.gz && \
    tar -xvf v${AUTOCYCLER_VER}.tar.gz && \
    rm v${AUTOCYCLER_VER}.tar.gz && \
    micromamba env create --name autocycler --file /Autocycler-${AUTOCYCLER_VER}/pipelines/Conda_environment_file_by_Ryan_Wick/environment.yml autocycler==${AUTOCYCLER_VER} && \
    micromamba clean -a -f -y && \
    rm -rf /Autocycler-${AUTOCYCLER_VER} && \
    mkdir /data


ENV PATH="/opt/conda/envs/autocycler/bin/:/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

RUN plassembler download -d /plassembler_db

CMD [ "autocycler", "--help" ]

WORKDIR /data

FROM app AS test

ARG AUTOCYCLER_VER

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

RUN wget -q https://github.com/rrwick/Autocycler/archive/refs/tags/v${AUTOCYCLER_VER}.tar.gz && \
    tar -xvf v${AUTOCYCLER_VER}.tar.gz

RUN ls Autocycler-${AUTOCYCLER_VER}/pipelines

RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -vxf autocycler-demo-dataset.tar && \
    bash Autocycler-${AUTOCYCLER_VER}/pipelines/Automated_Autocycler_Bash_script_by_Ryan_Wick/autocycler_full.sh reads.fastq.gz 4 1 && \
    head autocycler_out/consensus_assembly.fasta

RUN micromamba list -n autocycler
