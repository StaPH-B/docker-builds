FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL software="Roary"
LABEL software.version="3.12.0"
LABEL description="Rapid large-scale prokaryotic pan genome analysis"
LABEL website="https://github.com/sanger-pathogens/Roary"
LABEL license="https://github.com/sanger-pathogens/Roary/blob/master/GPL-LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

# install roary 3.12.0 via apt; cleanup apt garbage; make /data and /kraken_db
RUN apt-get update && apt-get install -y --no-install-recommends roary && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/* && \
 mkdir /data /kraken_db

WORKDIR /data
# set perl locale settings
ENV LC_ALL=C
