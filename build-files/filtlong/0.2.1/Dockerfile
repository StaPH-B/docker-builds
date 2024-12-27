ARG FILTLONG_VER="0.2.1"
# setting as global variable for persistence across all build layers 

FROM ubuntu:jammy as app

# re-instantiating for the app build layer if using ARG as a global variable above
ARG FILTLONG_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="3"
LABEL software="Filtlong"
LABEL software.version="${FILTLONG_VER}"
LABEL description="Filters long reads by quality and length. Can use Illumina reads as reference."
LABEL website="https://github.com/rrwick/Filtlong"
LABEL license="https://github.com/rrwick/Filtlong/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Thomas A. Christensen II"
LABEL maintainer2.email="25492070+MillironX@users.noreply.github.com"
LABEL maintainer3="Stephen Beckstrom-Sternberg"
LABEL maintainer3.email="stephen.beckstrom-sternberg@azdhs.gov"

# Install dependencies and cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 g++ \
 zlib1g-dev \
 make \
 python3 \
 pigz \
 less \
 bc  \
 gzip \
 ca-certificates \
 procps && \
 update-alternatives --install /usr/bin/python python /usr/bin/python3 10 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# installing filtlong
RUN wget https://github.com/rrwick/Filtlong/archive/v${FILTLONG_VER}.tar.gz && \
 tar -xzf v${FILTLONG_VER}.tar.gz && \
 rm -r v${FILTLONG_VER}.tar.gz && \
 cd /Filtlong-${FILTLONG_VER}/ && \
 make -j && \
 sed -i 's/\$hist/\$hist --dot "*"/g' scripts/read_info_histograms.sh && \
 mkdir /data

ENV PATH="$PATH:/Filtlong-$FILTLONG_VER/bin:/Filtlong-$FILTLONG_VER/scripts:/Filtlong-$FILTLONG_VER/test" LC_ALL=C 

# set workdir to default for building; set to /data at the end
WORKDIR /data

# new base for testing
FROM app as test

ARG FILTLONG_VER

RUN filtlong -h && filtlong --version

# unittest
RUN cd /Filtlong-${FILTLONG_VER} && python3 -m unittest -h

WORKDIR /test
RUN wget --no-verbose "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/056/SRR19008456/SRR19008456_1.fastq.gz" && \
 wget --no-verbose "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/056/SRR19008456/SRR19008456_2.fastq.gz" && \
 read_info_histograms.sh /data/*fastq.gz

RUN echo "Run filtlong with options on a pair of long reads in /data dir: " && \
 filtlong --min_length 250 --min_mean_q 40 SRR19008456_1.fastq.gz|gzip  > SRR19008456_1_filt.fastq.gz && \
 filtlong --min_length 250 --min_mean_q 40 SRR19008456_2.fastq.gz|gzip  > SRR19008456_2_filt.fastq.gz
