FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during image build time
ARG FILTLONG_VER=0.2.1

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="Filtlong"
LABEL software.version="0.2.1"
LABEL description="Filter long reads by quality and length. Can use ILMN reads as reference."
LABEL website="https://github.com/rrwick/Filtlong"
LABEL license="https://github.com/rrwick/Filtlong/blob/master/LICENSE"
LABEL maintainer="Thomas A. Christensen II"
LABEL maintainer.email="25492070+MillironX@users.noreply.github.com"

# install deps; cleanup apt garbage
RUN apt-get update && apt-get install -y \
 wget \
 g++ \
 zlib1g-dev \
 make \
 python3 \
 pigz \
 less \
 bc && \
 update-alternatives --install /usr/bin/python python /usr/bin/python3 10 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install filtlong; make /data
RUN wget https://github.com/rrwick/Filtlong/archive/v${FILTLONG_VER}.tar.gz && \
 tar -xzf v${FILTLONG_VER}.tar.gz && \
 rm -r v${FILTLONG_VER}.tar.gz && \
 cd Filtlong-${FILTLONG_VER}/ && \
 make -j && \
 sed -i 's/\$hist/\$hist --dot "*"/g' scripts/read_info_histograms.sh && \
 mkdir /data

# required for singularity compatibility; update PATH
ENV LC_ALL=C \
 PATH="${PATH}:/Filtlong-${FILTLONG_VER}/bin:/Filtlong-${FILTLONG_VER}/scripts"

WORKDIR /data
