ARG DSK_VER="0.0.100"

FROM ubuntu:focal as app
ARG DSK_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="DSK"
LABEL software.version=$DSK_VER
LABEL description="DSK is a k-mer counter for reads or genomes."
LABEL website="https://gatb.inria.fr/software/dsk/"
LABEL license="https://github.com/GATB/dsk/blob/master/LICENSE"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
 build-essential \
 cmake \
 git \
 wget \
 libz-dev

# Download DSK source code
RUN wget https://github.com/GATB/dsk/archive/refs/tags/v$DSK_VER.tar.gz && \
 tar -xzf v$DSK_VER.tar.gz && \
 rm v$DSK_VER.tar.gz

# Install GATB dependency where DSK expects it
RUN git clone https://github.com/GATB/gatb-core.git /dsk-$DSK_VER/thirdparty/gatb-core

# Compile DSK
WORKDIR /dsk-$DSK_VER/build
RUN cmake .. && make

# Add DSK executable to PATH
ENV PATH="/dsk-$DSK_VER/build/bin:$PATH"

WORKDIR /data

FROM app as test
ARG DSK_VER

# Run DSK's internal tests
WORKDIR /dsk-$DSK_VER/scripts
RUN ./simple_test.sh
