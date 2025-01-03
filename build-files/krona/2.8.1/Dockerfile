FROM ubuntu:jammy AS app

ARG KRONA_VER="2.8.1"
ARG KRAKENTOOLS_COMMIT="d4a2fbe2833c2392a724697c0c97a3014e748474"

USER root

WORKDIR /

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
    perl \
    unzip \
    python3 \
    python3-pip \
    python3-setuptools \
    make \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/miniconda3/bin:$PATH"

RUN wget https://github.com/marbl/Krona/releases/download/v${KRONA_VER}/KronaTools-${KRONA_VER}.tar && \
    tar -xvf KronaTools-${KRONA_VER}.tar && \
    rm KronaTools-${KRONA_VER}.tar && \
    mv KronaTools-${KRONA_VER} KronaTools && \
    cd KronaTools && \
    ./install.pl

RUN pip install biopython==1.84 \
    pandas==2.2.3

ARG KRAKENTOOLS_COMMIT="d4a2fbe2833c2392a724697c0c97a3014e748474"

RUN wget https://github.com/jenniferlu717/KrakenTools/archive/${KRAKENTOOLS_COMMIT}.zip && \
    unzip ${KRAKENTOOLS_COMMIT}.zip && \
    mv KrakenTools-${KRAKENTOOLS_COMMIT} KrakenTools && \
    chmod +x KrakenTools/*

WORKDIR /data

CMD ["ktImportTaxonomy"]

FROM app AS test

RUN python3 /KrakenTools/combine_kreports.py -h

RUN python3 /KrakenTools/extract_kraken_reads.py --help
RUN ktImportTaxonomy

