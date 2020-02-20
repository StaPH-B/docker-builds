FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL container.version="1.0.0"
LABEL software="Medaka"
LABEL software.version="0.11.5"
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
  virtualenv \
  git-lfs \
  cmake \
  make \
  python3-pip

RUN pip3 install medaka==0.11.5

#RUN wget https://github.com/nanoporetech/medaka/archive/v0.11.5.tar.gz &&\
#  tar xf v0.11.5.tar.gz &&\
#  rm v0.11.5.tar.gz &&\
#  cd medaka-0.11.5 &&\
#  make install &&\
#  mkdir /data

WORKDIR /data

# acts similar to activating python venv before running
ENV PATH="/medaka-0.11.5/venv/bin:$PATH" \
    LC_ALL=C
