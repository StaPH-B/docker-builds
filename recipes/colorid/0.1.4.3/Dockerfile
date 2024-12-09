FROM ubuntu:xenial

ARG COLORIDVER="0.1.4.3"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="colorid"
LABEL software.version="0.1.4.3"
LABEL description="Experiments with using BIGSI data structure for metagenomic and QC applications"
LABEL website="https://github.com/hcdenbakker/colorid"
LABEL license="https://github.com/hcdenbakker/colorid/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install minimal dependencies, cleanup apt garbage
RUN apt-get update && apt-get install -y \
 wget \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# ColorID install
RUN mkdir colorid && \
 cd colorid && \
 wget --no-check-certificate https://github.com/hcdenbakker/colorid/releases/download/v${COLORIDVER}/colorid_Linux64v${COLORIDVER} && \
 mv colorid_Linux64v${COLORIDVER} colorid && \
 chmod +x colorid && \
 mkdir /data

# set PATH and locale settings just in case 
ENV PATH="$PATH:/colorid"\
    LC_ALL=C

WORKDIR /data
