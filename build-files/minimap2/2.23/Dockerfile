FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during image build time
ARG MINIMAP2_VER="2.23"

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Minimap2"
LABEL software.version="2.23"
LABEL description="versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database"
LABEL website="https://github.com/lh3/minimap2"
LABEL license="https://github.com/lh3/minimap2/blob/master/LICENSE.txt"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="Kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install deps and cleanup apt garbage
RUN apt-get update && apt-get install -y python \
 curl \
 bzip2 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install minimap2 binary; make /data
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - && \
 mkdir /data

ENV PATH="${PATH}:/minimap2-${MINIMAP2_VER}_x64-linux"
WORKDIR /data
