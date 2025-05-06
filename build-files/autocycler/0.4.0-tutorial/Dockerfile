FROM mambaorg/micromamba:2.0.5-ubuntu22.04 AS app

ARG AUTOCYCLER_VER="0.4.0"

USER root
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.0.5-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Autocycler"
LABEL software.version="${AUTOCYCLER_VER}"
LABEL description="generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Autocycler"
LABEL license="https://github.com/rrwick/Autocycler/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# get conda environment file for extra tools
RUN wget -q https://github.com/rrwick/Autocycler/archive/refs/tags/v${AUTOCYCLER_VER}.tar.gz && \
    tar -xvf v${AUTOCYCLER_VER}.tar.gz && \
    rm v${AUTOCYCLER_VER}.tar.gz && \
    micromamba env create --file /Autocycler-${AUTOCYCLER_VER}/scripts/environment.yml --name autocycler && \
    micromamba clean -a -f -y && \
    rm -rf /Autocycler-${AUTOCYCLER_VER} && \
    mkdir /data

# install autocycler and helper scripts
WORKDIR /usr/local/bin

RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    tar -vxf autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    rm autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    wget -q https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz && \
    tar -vxf autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz && \
    rm autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz

ENV PATH="/opt/conda/envs/autocycler/bin/:/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "autocycler", "--help" ]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

COPY test.sh .
    
RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -vxf autocycler-demo-dataset.tar && \
    bash test.sh && \
    head autocycler_out/consensus_assembly.fasta

RUN micromamba list -n autocycler