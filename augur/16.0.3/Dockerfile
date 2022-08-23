# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM --platform=linux/x86_64 ubuntu:bionic as app

# ARG sets environment variables during the build stage
ARG AUGUR_VER="16.0.3"


# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="augur"
LABEL software.version=$AUGUR_VER
LABEL description="Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data.The output of augur is a series of JSONs that can be used to visualize your results using Auspice."
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# RUN executes code during the build
# Install dependencies via apt-get
RUN apt-get update && apt-get install -y \
  wget \
  build-essential \
  zlib1g-dev \
  libncurses5-dev \
  libgdbm-dev \
  libnss3-dev \
  libssl-dev \
  libreadline-dev \
  libffi-dev \
  libsqlite3-dev \
  libbz2-dev \
  liblzma-dev \
  pkg-config \
  libpng-dev \
  libfreetype6-dev \
  mafft python2.7- \
  iqtree \
  raxml \
  fasttree  \
  vcftools \
  git && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

#Install Python from source
RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz && \
    tar -xf Python-3.8.0.tgz && \
    rm Python-3.8.0.tgz && \
    cd Python-3.8.0 && ./configure --enable-optimizations && make -j 8 && make altinstall

#Install pip and python dependencies
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3.8 get-pip.py && rm get-pip.py && \
    pip3 install --upgrade pip && \
    pip install Cython

RUN wget https://github.com/nextstrain/augur/archive/refs/tags/${AUGUR_VER}.tar.gz && \
    tar -xzvf ${AUGUR_VER}.tar.gz && \
    rm ${AUGUR_VER}.tar.gz && \
    cd augur-${AUGUR_VER} && \
    python3.8 -m pip install '.[full]'

WORKDIR /data

FROM app as test

RUN git clone https://github.com/snakemake/snakemake && cd snakemake && python3.8 setup.py install

RUN git clone https://github.com/nextstrain/zika-tutorial && \
    cd zika-tutorial && \
    snakemake --cores 1
