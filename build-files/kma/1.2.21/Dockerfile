# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL container.version="1"
LABEL software="kma"
LABEL software.version="1.2.21"
LABEL description="K-mer alignment"
LABEL website="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license.type="Apache License, V2.0"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get -y install \
  gcc \
  libz-dev \
  make \
  git

RUN git clone https://bitbucket.org/genomicepidemiology/kma.git && \
  cd /kma && \
  git fetch && \
  git checkout 1.2.21 && \
  make && \
  mkdir /data

ENV PATH="$PATH:/kma" \
    LC_ALL=C

WORKDIR /data
