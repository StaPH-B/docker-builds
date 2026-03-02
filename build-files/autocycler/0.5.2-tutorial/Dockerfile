FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

ARG AUTOCYCLER_VER="0.5.2"

USER root
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
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
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

    
# get conda environment file for extra tools
RUN wget -q https://github.com/rrwick/Autocycler/archive/refs/tags/v${AUTOCYCLER_VER}.tar.gz && \
    tar -xvf v${AUTOCYCLER_VER}.tar.gz && \
    rm v${AUTOCYCLER_VER}.tar.gz && \
    micromamba env create --file /Autocycler-${AUTOCYCLER_VER}/pipelines/Conda_environment_file_by_Ryan_Wick/environment.yml --name autocycler && \
    micromamba clean -a -f -y && \
    rm -rf /Autocycler-${AUTOCYCLER_VER} && \
    mkdir /data

ENV PATH="/opt/conda/envs/autocycler/bin/:/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "autocycler", "--help" ]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

COPY test.sh .

# # Uncomment to run full reads in the assembler
# RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
#     tar -vxf autocycler-demo-dataset.tar && \
#     bash test.sh && \
#     head autocycler_out/consensus_assembly.fasta

# Runs test using demo dataset but with subsampled reads to improve efficiency
RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -xf autocycler-demo-dataset.tar && \
    (zcat reads.fastq.gz || true) | head -n 20000 | gzip > reads_small.fastq.gz && \
    mv reads_small.fastq.gz reads.fastq.gz && \
    bash test.sh

RUN micromamba list -n autocycler
