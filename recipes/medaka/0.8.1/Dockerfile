FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="Medaka"
LABEL software.version="0.8.1"
LABEL description="Consensus sequence correction provided by ONT Research"
LABEL website="https://github.com/nanoporetech/medaka"
LABEL license="https://github.com/nanoporetech/medaka/blob/master/LICENSE.md"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install --no-install-recommends -y make \
  bzip2 \
  gcc \
  g++ \
  python \
  zlib1g-dev \
  wget \
  curl \
  libffi-dev \
  libncurses5-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  libssl-dev \
  python3-all-dev \
  python-virtualenv \
  virtualenv

RUN wget https://github.com/nanoporetech/medaka/archive/v0.8.1.tar.gz &&\
  tar xf v0.8.1.tar.gz &&\
  rm v0.8.1.tar.gz &&\
  cd medaka-0.8.1 &&\
  make install &&\
  mkdir /data

WORKDIR /data

# acts similar to activating python venv before running
ENV PATH="/medaka-0.8.1/venv/bin:$PATH"
