# Base Image
FROM ubuntu:xenial

# Metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Legsta"
LABEL software.version="0.3.7"
LABEL description="In silico Legionella pneumophila Sequence Based Typing (SBT)"
LABEL website="https://github.com/tseemann/legsta"
LABEL license="https://raw.githubusercontent.com/tseemann/legsta/master/LICENSE"
LABEL maintainer="Jake Garfin"
LABEL maintainer.email="jake.garfin@state.mn.us"

RUN apt-get update && apt-get install -y \
  cpanminus \
  build-essential \
  libc6-i386 \
  wget

# Install perl module
RUN cpanm Data::Dumper 

# Install Legsta
RUN wget 'https://github.com/tseemann/legsta/archive/v0.3.7.tar.gz' && \
  tar -xvf 'v0.3.7.tar.gz' && \
  rm v0.3.7.tar.gz

ENV PATH="${PATH}:/legsta-0.3.7/bin"

# set perl locale settings for singularity compatibility
ENV LC_ALL=C

WORKDIR /data
