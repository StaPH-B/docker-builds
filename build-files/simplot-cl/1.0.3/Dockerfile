FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

ARG SIMPLOT_CL_VER="1.0.3"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="simplot-cl"
LABEL software.version="${SIMPLOT_CL_VER}"
LABEL description="A Command-Line Similarity Plot Generator"
LABEL website="https://github.com/hodcroftlab/simplot-cl/"
LABEL license="https://github.com/hodcroftlab/simplot-cl/blob/main/LICENSE.txt"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

# Standard packages for downloading source code
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Decompress source code in /opt and llink /opt/simplot-cl-1.0.3 to /usr/local/bin for discovery in python path.
WORKDIR /opt

RUN wget -q https://github.com/hodcroftlab/simplot-cl/archive/refs/tags/v${SIMPLOT_CL_VER}.tar.gz && \
    tar -xzf v${SIMPLOT_CL_VER}.tar.gz && \
    rm v${SIMPLOT_CL_VER}.tar.gz && \
    chmod +x /opt/simplot-cl-1.0.3/simplot.py && \
    ln -s /opt/simplot-cl-${SIMPLOT_CL_VER}/simplot.py /usr/local/bin/simplot.py

# Install from environment available in source code folder.
RUN micromamba install --name base -f /opt/simplot-cl-${SIMPLOT_CL_VER}/environment.yml -y && \
    micromamba clean -a -f -y && \
    mkdir /data

# Add micromamba packages to path and set locale.
ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

WORKDIR /data

CMD [ "simplot.py", "-h" ]



FROM app AS test

ARG SIMPLOT_CL_VER="1.0.3"

# List micromamba dependencies
RUN micromamba list -n base

WORKDIR /test


# Run simplot help command
RUN simplot.py -h

# Generate simplots for queries listed through -q, using all other sequences in the supplied FASTA file as a reference.
RUN simplot.py \
    -s /opt/simplot-cl-${SIMPLOT_CL_VER}/demo_data/query_alignment.fasta \
    -q OP137282.1 JX274981.1 \
    -ws 150 \
    -ss 50 \
    -p simplots \
    --no-align

# Generate simplots for all sequences in the supplied FASTA file using all sequences in the reference FASTA as references.
RUN simplot.py \
    -s /opt/simplot-cl-${SIMPLOT_CL_VER}/demo_data/query_alignment.fasta \
    -r /opt/simplot-cl-${SIMPLOT_CL_VER}/demo_data/reference_alignment.fasta \
    -ws 200 \
    -ss 100 \
    -p simplots \
    --no-align