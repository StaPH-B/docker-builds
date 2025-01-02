FROM ubuntu:jammy AS app

ARG KRONA_VER="2.8.1"
ARG KRAKENTOOLS_VER="d4a2fbe"

LABEL base_image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="krona"
LABEL software.version="${KRONA_VER}"
LABEL description="Krona Tools is a set of scripts to create Krona charts from several Bioinformatics tools as well as from text and XML files."
LABEL website="https://github.com/marbl/Krona"
LABEL license="https://github.com/marbl/Krona/blob/master/KronaTools/LICENSE.txt"
LABEL maintainer="Sage Wright"
LABEL maintainer.email="sagemwright@gmail.com"

# 'LABEL' instructions tag the image with metadata that might be important to the user
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    curl \
    python3 \
    python3-pip \
    python3-setuptools \
    git \
    make \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm ~/miniconda3/miniconda.sh

ENV PATH="/root/miniconda3/bin:$PATH"

RUN conda install -c bioconda krona=${KRONA_VER} && \
    ktUpdateTaxonomy.sh

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
RUN ktImportTaxonomy

