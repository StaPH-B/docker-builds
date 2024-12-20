FROM ubuntu:jammy as app

ARG LABEL_VER="0.6.4"
ARG LABEL_DATE="202209" 

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Label"
LABEL software.version="${LABEL_VER}"
LABEL description="Rapid annotation of influenza"
LABEL website="https://wonder.cdc.gov/amd/flu/label/"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# MAFFT version v7.490
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    procps \
    ca-certificates \
    mafft \
    unzip \
    zip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install fasttree
WORKDIR /usr/local/bin/

WORKDIR /

RUN wget -q https://wonder.cdc.gov/amd/flu/label/flu-amd-LABEL-${LABEL_DATE}.zip && \
    unzip flu-amd-LABEL-${LABEL_DATE}.zip && \
    rm flu-amd-LABEL-${LABEL_DATE}.zip

ENV PATH="/flu-amd/:$PATH" \
    LC_ALL=C

CMD label -h

WORKDIR /data

FROM app as test

WORKDIR /test

RUN LABEL -h

RUN LABEL /flu-amd/test.fa test\_proj H9v2011 && \
    head *txt