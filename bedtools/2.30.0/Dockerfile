# For easy upgrade later. ARG variables only persist at build time
ARG BEDTOOLS_VER="2.30.0"

FROM ubuntu:bionic as app
ARG BEDTOOLS_VER

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL software="bedtools"
LABEL software.version=$BEDTOOLS_VER
LABEL description="bedtools - the swiss army knife for genome arithmetic"
LABEL website="https://github.com/arq5x/bedtools2"
LABEL license="https://github.com/arq5x/bedtools2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Sarah Nadeau"
LABEL maintainer2.email="sarah.nadeau@bsse.ethz.ch"

# only need wget to DL bedtools binary; cleanup apt garbage
RUN apt-get update && apt-get install -y \
 wget && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download bedtools static binary to location already in PATH; make /data
RUN cd /usr/local/bin && \
 wget https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VER}/bedtools.static.binary && \
 mv bedtools.static.binary bedtools && \
 chmod +x bedtools && \
 mkdir /data

# setting just in case for singularity compatibility
ENV LC_ALL=C

WORKDIR /data

FROM app as test
ARG BEDTOOLS_VER

# Run test script
COPY test.sh .
RUN bash test.sh $BEDTOOLS_VER
