ARG FLYE_VER="2.9.1"

FROM ubuntu:bionic as app

ARG FLYE_VER

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="Flye"
LABEL software.version=${FLYE_VER}
LABEL description="Fast and accurate de novo assembler for single molecule sequencing reads"
LABEL website="https://github.com/fenderglass/Flye"
LABEL license="https://github.com/fenderglass/Flye/blob/flye/LICENSE"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    gcc \
    g++ \
    python \
    python-pip \
    python-setuptools \
    zlib1g-dev \
    wget && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget https://github.com/fenderglass/Flye/archive/${FLYE_VER}.tar.gz && \
    tar -xvf ${FLYE_VER}.tar.gz && \
    rm ${FLYE_VER}.tar.gz && \
    cd Flye-${FLYE_VER} && \
    python setup.py build && \
    python setup.py install && \
    mkdir /data

WORKDIR /data

ENV LC_ALL=C

FROM app as test

ARG FLYE_VER

RUN python /Flye-${FLYE_VER}/flye/tests/test_toy.py

# the following takes too long, but this would be the test I would recommend if testing this locally.
# from https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md
# RUN wget https://zenodo.org/record/1172816/files/E.coli_PacBio_40x.fasta && \
#    flye --pacbio-raw E.coli_PacBio_40x.fasta --out-dir out_pacbio --threads 4 && \
#    wget https://zenodo.org/record/1172816/files/Loman_E.coli_MAP006-1_2D_50x.fasta && \
#    flye --nano-raw Loman_E.coli_MAP006-1_2D_50x.fasta --out-dir out_nano --threads 4

