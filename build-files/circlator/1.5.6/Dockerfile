# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="Circlator"
LABEL software.version="1.5.6"
LABEL description="A tool to circularize genome assemblies"
LABEL website="https://github.com/sanger-pathogens/circlator"
LABEL license="https://github.com/sanger-pathogens/circlator/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update -qq && apt-get install -y python \
  python3-pip \
  git \
  wget \
  unzip \
  zlib1g-dev \
  libncurses5-dev \
  libbz2-dev \
  liblzma-dev

# get latest release and install python dependencies
RUN wget https://github.com/sanger-pathogens/circlator/archive/v1.5.6.tar.gz && \
  tar -xvf v1.5.6.tar.gz && \
  cd circlator-1.5.6 && \
  pwd && \
  bash install_dependencies.sh

ENV PATH="/circlator-1.5.6:/circlator-1.5.6/build:\
/circlator-1.5.6/build/bwa-0.7.12:\
/circlator-1.5.6/build/canu-1.4/Linux-amd64/bin/:\
/circlator-1.5.6/build/prodigal-2.6.2:/circlator-1.5.6/build/samtools-1.3:\
/circlator-1.5.6/build/MUMmer3.23:\
/circlator-1.5.6/build/SPAdes-3.7.1-Linux/bin:\
${PATH}"

# install circlator
RUN cd /circlator-1.5.6 && \
  python3 setup.py install

# check install
RUN circlator progcheck
