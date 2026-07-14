FROM ubuntu:noble AS app

ARG ART_VER="2.5.8"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="ART"
LABEL software.version="${ART_VER}"
LABEL description="ART is a set of simulation tools to generate synthetic next-generation sequencing reads."
LABEL website="https://www.niehs.nih.gov/research/resources/software/biostatistics/art"
LABEL license="https://www.niehs.nih.gov/research/resources/software/biostatistics/art"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    perl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://www.niehs.nih.gov/sites/default/files/2024-02/artbinmountrainier2016.06.05linux64.tgz &&\
    tar -C /opt/ -xvf artbinmountrainier2016.06.05linux64.tgz &&\
    rm artbinmountrainier2016.06.05linux64.tgz

ENV PATH="/opt/art_bin_MountRainier:$PATH" \
    LC_ALL=C

CMD [ "art_illumina" ]

WORKDIR /data

## Test ##
FROM app AS test

WORKDIR /opt/art_bin_MountRainier/examples

RUN ./run_test_examples_illumina.sh

