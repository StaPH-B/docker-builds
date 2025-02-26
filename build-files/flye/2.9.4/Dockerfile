# for easy upgrade later
ARG FLYE_VER="2.9.4"

FROM ubuntu:jammy as app

# have to re-instantiate variable within app stage
ARG FLYE_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Flye"
LABEL software.version="${FLYE_VER}"
LABEL description="Fast and accurate de novo assembler for single molecule sequencing reads"
LABEL website="https://github.com/fenderglass/Flye"
LABEL license="https://github.com/fenderglass/Flye/blob/flye/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

RUN apt-get update && apt-get install --no-install-recommends -y \
    make \
    gcc \
    g++ \
    python3 \
    python3-pip \
    python3-setuptools \
    zlib1g-dev \
    wget \
    ca-certificates \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install flye
RUN wget -q https://github.com/fenderglass/Flye/archive/${FLYE_VER}.tar.gz && \
    tar -xf ${FLYE_VER}.tar.gz && \
    rm -v ${FLYE_VER}.tar.gz && \
    cd Flye-${FLYE_VER} && \
    python3 setup.py build && \
    python3 setup.py install && \
    mkdir /data

# set final working directory
WORKDIR /data

# for singularity compatibility
ENV LC_ALL=C

#### begin the test stage ####
FROM app as test

# have to re-instantiate variable within app stage
ARG FLYE_VER

# run flye toy dataset test
RUN python3 /Flye-${FLYE_VER}/flye/tests/test_toy.py

# download test data (ONT and ILMN FASTQs) and run through flye
RUN echo "downloading ONT test data from bactopia/bactopia-tests on GitHub..." && \
    wget -q https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz && \
    flye --nano-raw ERR3772599.fastq.gz -o flye-test-portiera -t 2 && \
    flye --version

# the following takes too long, but this would be the test I would recommend if testing this locally.
# from https://github.com/fenderglass/Flye/blob/flye/docs/USAGE.md
# RUN wget https://zenodo.org/record/1172816/files/E.coli_PacBio_40x.fasta && \
#    flye --pacbio-raw E.coli_PacBio_40x.fasta --out-dir out_pacbio --threads 4 && \
#    wget https://zenodo.org/record/1172816/files/Loman_E.coli_MAP006-1_2D_50x.fasta && \
#    flye --nano-raw Loman_E.coli_MAP006-1_2D_50x.fasta --out-dir out_nano --threads 4
