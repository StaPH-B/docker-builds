FROM python:3.13.12-slim AS app

ARG SIMPLOT_CL_VER="1.0.3"

WORKDIR /

LABEL base.image="python:3.13.12-slim"
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
    procps \
    mafft \
    libgomp1 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Decompress source code in /opt and llink /opt/simplot-cl-1.0.3 to /usr/local/bin for discovery in python path.
WORKDIR /opt

RUN wget -q https://github.com/hodcroftlab/simplot-cl/archive/refs/tags/v${SIMPLOT_CL_VER}.tar.gz && \
    tar -xzf v${SIMPLOT_CL_VER}.tar.gz && \
    rm v${SIMPLOT_CL_VER}.tar.gz && \
    chmod +x /opt/simplot-cl-1.0.3/simplot.py && \
    ln -s /opt/simplot-cl-${SIMPLOT_CL_VER}/simplot.py /usr/local/bin/simplot.py

# Install packages listed in installation steps for simplot-cl.
RUN pip install --no-cache biopython pandas numpy matplotlib argcomplete

# Add micromamba packages to path and set locale.
ENV LC_ALL=C

WORKDIR /data

CMD [ "simplot.py", "-h" ]



FROM app AS test

ARG SIMPLOT_CL_VER="1.0.3"

# List package dependencies
RUN pip freeze

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