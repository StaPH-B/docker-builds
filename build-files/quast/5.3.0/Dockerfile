ARG QUAST_VER="5.3.0"

## Builder ##
FROM ubuntu:focal as builder

ARG QUAST_VER

# define timezone to avoid build stalls
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python2 \
    perl \
    cpanminus \
    g++ \
    make \
    openjdk-8-jre-headless \
    r-base \
    pkg-config \
    libfreetype6-dev \
    libpng-dev \
    libboost-all-dev \
    locales &&\
    locale-gen en_US.UTF-8 &&\
    cpanm Time::HiRes &&\
    apt-get autoclean &&\
    rm -rf /var/lib/apt/lists/*

# python dependencies
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2 1 &&\
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && python get-pip.py &&\
    pip install --no-cache matplotlib simplejson joblib

# install quast
RUN wget https://github.com/ablab/quast/releases/download/quast_${QUAST_VER}/quast-${QUAST_VER}.tar.gz && \
    tar -xzf quast-${QUAST_VER}.tar.gz && \
    rm -rf quast-${QUAST_VER}.tar.gz && \
    cd /quast-${QUAST_VER} && \
    ./setup.py install

# add GRIDSS for SV detection
ADD https://github.com/ablab/quast/raw/master/external_tools/gridss/gridss-1.4.1.jar /quast-${QUAST_VER}/quast_libs/gridss/

## App ##
FROM ubuntu:jammy as app

ARG QUAST_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="QUAST"
LABEL software.version=${QUAST_VER}
LABEL description="Genome assembly evaluation tool"
LABEL website="https://github.com/ablab/quast"
LABEL license="https://github.com/ablab/quast/blob/master/LICENSE.txt"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

# define timezone to avoid build stalls
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install only necessary programs and libraries to run quast
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python3 \
    python3-matplotlib \
    perl \
    openjdk-8-jre-headless \
    r-base \
    libidn12 \ 
    locales &&\
    locale-gen en_US.UTF-8 &&\
    apt-get autoclean &&\
    rm -rf /var/lib/apt/lists/* &&\
    update-alternatives --install /usr/bin/python python /usr/bin/python3 1 &&\
    ln -s /usr/lib/x86_64-linux-gnu/libidn.so.12 /usr/lib/x86_64-linux-gnu/libidn.so.11

# copy quast and compiled tools
COPY --from=builder /quast-${QUAST_VER} /quast-${QUAST_VER}

ENV LC_ALL=C \
    PATH=$PATH:/quast-${QUAST_VER} 

CMD quast.py --help && quast-lg.py --help && metaquast.py --help

WORKDIR /data

## Test ##
FROM app as test
# test quast
RUN quast.py --test-sv && mv ./quast_test_output/ ./quast_test_sv_output/    
# test quast-lg
RUN quast-lg.py --test && mv ./quast_test_output/ ./quast_test_lg_output/    
# test metaquast
RUN metaquast.py --test-no-ref    
# check logs
RUN tail -n5 ./quast_test_sv_output/quast.log &&\
    tail -n5 ./quast_test_lg_output/quast.log &&\
    tail -n5 ./quast_test_output/metaquast.log

# Note: libidn is required for makeblastdb. libidn.so.11 symlink is a temporary patch for this version.

