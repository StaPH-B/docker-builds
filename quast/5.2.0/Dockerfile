ARG QUAST_VER="5.2.0"

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
    /quast-${QUAST_VER}/setup.py install

# add GRIDSS for SV detection
ADD https://github.com/ablab/quast/raw/master/external_tools/gridss/gridss-1.4.1.jar /quast-${QUAST_VER}/quast_libs/gridss/

## App ##
FROM ubuntu:focal as app

ARG QUAST_VER

LABEL base.image="ubuntu:focal"
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
    python2 \
    perl \
    openjdk-8-jre-headless \
    r-base \
    libidn11 \ 
    locales &&\
    locale-gen en_US.UTF-8 &&\
    apt-get autoclean &&\
    rm -rf /var/lib/apt/lists/*

# python dependencies
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2 1 &&\
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && python get-pip.py &&\
    pip install --no-cache matplotlib simplejson joblib
# copy quast and compiled tools
COPY --from=builder /quast-${QUAST_VER} /quast-${QUAST_VER}
# copy compiled Time::HiRes perl module
COPY --from=builder /usr/local/lib/x86_64-linux-gnu/perl/5.30.0/Time/ /usr/local/lib/x86_64-linux-gnu/perl/5.30.0/Time/

ENV LC_ALL=C
ENV PATH=$PATH:/quast-${QUAST_VER} 

CMD quast.py --help && quast-lg.py --help && metaquast.py --help

WORKDIR /data

## Test ##
FROM app as test
# test quast
RUN quast.py --test-sv && mv ./quast_test_output/ ./quast_test_sv_output/    
# test quast-lg
RUN quast-lg.py --test && mv ./quast_test_output/ ./quast_test_lg_output/    
# test metaquast
RUN metaquast.py --test    
# check logs
RUN tail -n5 ./quast_test_sv_output/quast.log &&\
    tail -n5 ./quast_test_lg_output/quast.log &&\
    tail -n5 ./quast_test_output/metaquast.log

# Note 1: "Warnings are GenMark license related. They disappear when a valid licence is provided."
# Note 2: "metaquast.py --test-no-ref" throws error related Krona plot (known bug of Quast 5.2.0)
