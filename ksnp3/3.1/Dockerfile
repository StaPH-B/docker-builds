FROM ubuntu:xenial
 
# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="kSNP3"
LABEL software.version="3.1"
LABEL description="K-mer-based phylgenetic inference"
LABEL website="https://github.com/cdeanj/kSNP3/blob/master/kSNP3"

MAINTAINER Kevin Libuit <kevin.libuit@dgs.virginia.gov>

RUN apt-get update && apt-get install -y python \
  wget tcsh unzip

RUN wget https://sourceforge.net/projects/ksnp/files/kSNP3.1_Linux_package.zip && \
  unzip kSNP3.1_Linux_package.zip && \
  mv /kSNP3.1_Linux_package/kSNP3/ /usr/local && \
  rm -r kSNP3.1_Linux_package.zip && \
  mkdir data

ENV PATH ="${PATH}:/usr/local/kSNP3/"

WORKDIR /data
