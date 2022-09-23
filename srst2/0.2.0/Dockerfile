FROM ubuntu:xenial as app

# for easy upgrade later. ARG variables only persist at build time
ARG SRST2_VER=0.2.0

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="SRST2"
LABEL software.version="v0.2.0"
LABEL description="Short Read Sequence Typing for Bacterial Pathogens"
LABEL website="https://github.com/katholt/srst2"
LABEL license="https://github.com/katholt/srst2/blob/master/LICENSE.txt"
LABEL maintainer="Holly Halstead"
LABEL maintainer1.email="holly.halstead@doh.wa.gov"


# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y \
python2.7 \
python-pip \
python-scipy \
python-biopython \
make \
libc6-dev \
g++ \
zlib1g-dev \
build-essential \
git \
libx11-dev \
xutils-dev \
zlib1g-dev \
python-pip \
bowtie2=2.2.6-2 \
curl \
libncurses5-dev \
unzip \
wget  \
locate

# download pre-compiled binary; unzip; put binary in /usr/bin; make /data
RUN curl -O -L https://sourceforge.net/projects/samtools/files/samtools/0.1.18/samtools-0.1.18.tar.bz2 && \
tar xvfj samtools-0.1.18.tar.bz2 && \
cd samtools-0.1.18 && \
make && \
cp samtools /usr/local/bin && \
cp bcftools/bcftools /usr/local/bin && \
cd misc/ &&  \
cp *.pl maq2sam-long maq2sam-short md5fa md5sum-lite wgsim /usr/local/bin/ && \
cd

# Install SRST2
RUN pip install biopython git+https://github.com/katholt/srst2.git@v${SRST2_VER} && \
mkdir /data

# set working directory
WORKDIR /data

FROM app as test

RUN srst2 --version && \
getmlst.py -h
