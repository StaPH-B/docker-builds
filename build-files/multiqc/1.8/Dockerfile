# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="MultiQC"
LABEL software.version="1.8"
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
  python3 \
  python3-dev \
  python3-pip \
  texlive-xetex \
  texlive-math-extra \
  locales && \
  locale-gen en_US.UTF-8 && \
  apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install multiqc
RUN pip3 install "multiqc==1.8"

# install pandoc
RUN wget https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-linux.tar.gz && \
  tar -xvf pandoc-2.7.3-linux.tar.gz && \
  rm pandoc-2.7.3-linux.tar.gz

ENV LC_ALL='C.UTF-8' LANG='C.UTF-8'

# add pandoc to path
ENV PATH="/pandoc-2.7.3/bin:${PATH}"

RUN mkdir /data
WORKDIR /data
