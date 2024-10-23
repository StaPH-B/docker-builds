FROM ubuntu:jammy AS app

WORKDIR /

# using a git commit because the last release was over three years ago, despite recent(ish) activity in the repo's main branch
# this commit is from 2023-11-16: https://github.com/jenniferlu717/KrakenTools/commit/d4a2fbe2833c2392a724697c0c97a3014e748474
ARG KRAKENTOOLS_VERSION="d4a2fbe2833c2392a724697c0c97a3014e748474"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="KrakenTools"
LABEL software.version=${KRAKENTOOLS_VERSION}
LABEL description="KrakenTools is a set of tools for processing Kraken output"
LABEL website="https://github.com/jenniferlu717/KrakenTools"
LABEL documentation="https://github.com/jenniferlu717/KrakenTools"
LABEL license="https://github.com/jenniferlu717/KrakenTools/blob/master/LICENSE"
LABEL maintainer="Sage Wright"
LABEL maintainer.email="sagemwright@gmail.com"


# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    python3 \
    python3-pip \
    python3-setuptools \
    git \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install biopython==1.84 \
    pandas==2.2.3

RUN git clone https://github.com/jenniferlu717/KrakenTools.git && \
    cd KrakenTools && \
    git checkout ${KRAKENTOOLS_VERSION} && \
    chmod +x *

ENV PATH=/KrakenTools:${PATH}

WORKDIR /data

FROM app AS test

RUN python3 /KrakenTools/extract_kraken_reads.py --help