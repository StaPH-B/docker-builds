FROM ubuntu:jammy AS app

ARG MOBSUITE_VER="3.1.9"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MOB-suite"
LABEL software.version="${MOBSUITE_VER}"
LABEL description="Software tools for clustering, reconstruction and typing of plasmids from draft assemblies"
LABEL website="https://github.com/phac-nml/mob-suite"
LABEL license="https://github.com/phac-nml/mob-suite/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    ncbi-blast+ \
    mash &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir mob_suite==${MOBSUITE_VER} 

ENV LC_ALL=C

CMD ["/bin/sh", "-c", "mob_init -h && mob_typer -h && mob_recon -h && mob_cluster -h"]

WORKDIR /data

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y \
    git \
    python3-pytest

RUN mob_init &&\
    git clone https://github.com/phac-nml/mob-suite.git &&\
    cd mob-suite/mob_suite/tests &&\
    pytest-3 &&\
    rm -rf /usr/local/lib/python3.10/dist-packages/mob_suite/databases
