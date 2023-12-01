FROM ubuntu:jammy as app

ARG MULTIQC_VER="1.18"
ARG PANDOC_VER="2.7.3"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MultiQC"
LABEL software.version="${MULTIQC_VER}"
LABEL description="Aggregate bioinformatics results across many samples into a single report."
LABEL website="https://github.com/ewels/MultiQC"
LABEL license="https://github.com/ewels/MultiQC/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
# Although... let's be honest. Most of this is copied and pasted from Abigail Shockey

# install software-properties-common for add-apt-repository
RUN apt-get update && apt-get install -y \
  software-properties-common

# add universe repository for texlive-xetex and texlive-math-extra
RUN add-apt-repository universe

# install remaining dependencies
RUN apt-get update && apt-get install -y \
  wget \
  git \
  python3 \
  python3-dev \
  python3-pip \
  locales && \
  locale-gen en_US.UTF-8 && \
  apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install multiqc
RUN pip3 install "multiqc==${MULTIQC_VER}"

# install pandoc
RUN wget https://github.com/jgm/pandoc/releases/download/${PANDOC_VER}/pandoc-${PANDOC_VER}-linux.tar.gz && \
  tar -xvf pandoc-${PANDOC_VER}-linux.tar.gz && \
  rm pandoc-${PANDOC_VER}-linux.tar.gz

ENV LC_ALL='C.UTF-8' LANG='C.UTF-8'

# add pandoc to path
ENV PATH="/pandoc-${PANDOC_VER}/bin:${PATH}"

RUN mkdir /data
WORKDIR /data

# testing layer starts here
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
RUN mkdir /test
WORKDIR /test

RUN git clone https://github.com/ewels/MultiQC_TestData
RUN multiqc .
