ARG LRGE_VER="0.1.3"

FROM ubuntu:jammy AS app

ARG LRGE_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="lrge"
LABEL software.version="${LRGE_VER}"
LABEL description="Long Read-based Genome size Estimation from overlaps"
LABEL website="https://github.com/mbhall88/lrge"
LABEL license="https://github.com/mbhall88/lrge/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/mbhall88/lrge/releases/download/lrge-${LRGE_VER}/lrge-${LRGE_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    tar -xvf lrge-${LRGE_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    mv lrge-${LRGE_VER}-x86_64-unknown-linux-gnu/lrge /usr/local/bin && \
    rm -rf lrge-${LRGE_VER}-x86_64-unknown-linux-gnu.tar.gz lrge-0.1.3-x86_64-unknown-linux-gnu

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "lrge", "--help" ]

WORKDIR /data

FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN lrge --help && lrge --version

# stolen from https://github.com/mbhall88/lrge
RUN wget -q -O reads.fq.gz "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR283/049/SRR28370649/SRR28370649_1.fastq.gz" && \
    lrge -t 8 reads.fq.gz -o results.txt && \
    head results.txt
