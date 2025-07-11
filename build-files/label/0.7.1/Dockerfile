FROM ubuntu:jammy AS app

ARG LABEL_VER="0.7.1"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Label"
LABEL software.version="${LABEL_VER}"
LABEL description="Rapid annotation of influenza"
LABEL documentation="https://wonder.cdc.gov/amd/flu/label/"
LABEL website="https://github.com/CDCgov/label"
LABEL license="https://github.com/CDCgov/label/blob/master/LICENSE"
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

RUN wget https://github.com/CDCgov/label/releases/download/v${LABEL_VER}/label-v${LABEL_VER}-universal.zip && \
    unzip label-v${LABEL_VER}-universal.zip && \
    rm label-v${LABEL_VER}-universal.zip

ENV PATH="/flu-amd/:$PATH" \
    LC_ALL=C

CMD ["label", "-h"]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN LABEL -h

RUN LABEL /flu-amd/LABEL_RES/training_data/H9v2011/H9v2011_downsample.fa test_project H9v2011 && \
    head *txt