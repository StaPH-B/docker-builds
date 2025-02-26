FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="Minimap2"
LABEL software.version="2.17"
LABEL description="versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database"
LABEL website="https://github.com/lh3/minimap2"
LABEL license="https://github.com/lh3/minimap2/blob/master/LICENSE.txt"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="Kelsey.florek@slh.wisc.edu"

RUN apt-get update && apt-get install -y python \
  curl\
  bzip2

RUN curl -L https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2 | tar -jxvf -

ENV PATH="${PATH}:/minimap2-2.17_x64-linux"
WORKDIR /data
