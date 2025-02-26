FROM ubuntu:bionic

LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="bedtools"
LABEL software.version="2.29.2"
LABEL description="bedtools - the swiss army knife for genome arithmetic"
LABEL website="https://github.com/arq5x/bedtools2"
LABEL license="https://github.com/arq5x/bedtools2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

RUN apt-get update && apt-get install -y \
 wget

# for ease in creating new dockerfiles. LC_ALL just in case for singularity
ENV bedtoolsVer=2.29.2 \
    LC_ALL=C

# download bedtools static binary
RUN cd /usr/local/bin && \
 wget https://github.com/arq5x/bedtools2/releases/download/v${bedtoolsVer}/bedtools.static.binary && \
 mv bedtools.static.binary bedtools && \
 chmod +x bedtools && \
 mkdir /data

WORKDIR /data
