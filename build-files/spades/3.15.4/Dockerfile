FROM ubuntu:focal as app

# to make it easier to upgrade for new versions; ARG variables only persist during docker image build time
ARG SPAdesVer=3.15.4

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SPAdes"
LABEL software.version="3.15.4"
LABEL description="de novo DBG genome assembler"
LABEL website="https://github.com/ablab/spades"
LABEL license="https://github.com/ablab/spades/blob/v3.15.3/assembler/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
# python v3.8.10 is installed here; point 'python' to python3
RUN apt-get update && apt-get install --no-install-recommends -y python3 \
 python3-distutils \
 wget \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
 update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# install SPAdes binary; make /data
RUN wget https://github.com/ablab/spades/releases/download/v${SPAdesVer}/SPAdes-${SPAdesVer}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPAdesVer}-Linux.tar.gz && \
  rm -r SPAdes-${SPAdesVer}-Linux.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C.UTF-8 \
    PATH="${PATH}:/SPAdes-${SPAdesVer}-Linux/bin"

WORKDIR /data

# test layer
FROM app as test

# print version and run the supplied test flag
RUN spades.py --version && spades.py --test
