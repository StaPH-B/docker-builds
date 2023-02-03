FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during image building stage
ARG FILTLONG_VER=0.2.1

USER root

# re-instantiating for the app build layer if using ARG as a global variable above
#ARG FILTLONG_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="3"
LABEL software="Filtlong"
LABEL software.version="${FILTLONG_VER}"
LABEL description="Filters long reads by quality and length. Can use Illumina reads as reference."
LABEL website="https://github.com/rrwick/Filtlong"
LABEL license="https://github.com/rrwick/Filtlong/blob/master/LICENSE"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
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
 gzip && \
 update-alternatives --install /usr/bin/python python /usr/bin/python3 10 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH"

# set workdir to /opt for installing Filtlong; set to /data for testing
WORKDIR /opt

# install filtlong
RUN wget --progress=dot:gi \
https://github.com/rrwick/Filtlong/archive/v${FILTLONG_VER}.tar.gz \
--no-check-certificate && \
tar -xzf v${FILTLONG_VER}.tar.gz && \
rm -rf v${FILTLONG_VER}.tar.gz

WORKDIR /opt/Filtlong-${FILTLONG_VER}
RUN make
RUN chmod +x bin/filtlong 

ENV PATH="$PATH:/opt/Filtlong-$FILTLONG_VER/bin:\
/opt/Filtlong-$FILTLONG_VER/scripts:\
/opt/Filtlong-$FILTLONG_VER/test" LC_ALL=C 

RUN echo "Put symlink to filtlong in /usr/local/bin " && 
 ln -s /opt/Filtlong-$FILTLONG_VER/bin/filtlong /usr/local/bin/

# set workdir to /data for testing
WORKDIR /data

# new base for testing
FROM app as test
ARG FILTLONG_VER
RUN echo "Running Test layer"
ENV PATH="$PATH:/data"

# download a pair of long-read sequences from European Nucleotide Archive (ENA) and run them through Filtlong
# SRR19008456_1.fastq and SRR19008456_2.fastq
RUN wget --no-verbose "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/056/SRR19008456/SRR19008456_1.fastq.gz"
RUN wget --no-verbose "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/056/SRR19008456/SRR19008456_2.fastq.gz"

RUN echo "Running read_info_histograms.sh"
RUN sed -i 's/\$hist/\$hist --dot "*"/g' /opt/Filtlong-${FILTLONG_VER}/scripts/read_info_histograms.sh
RUN /opt/Filtlong-${FILTLONG_VER}/scripts/read_info_histograms.sh /data/*fastq.gz 
RUN echo "Done with histograms"

RUN echo "Show help file for installed unittest"
RUN cd /opt/Filtlong-${FILTLONG_VER} && \
 python3 -m unittest -h

RUN echo "Run unittest without args: "&& \
 python3 -m unittest
RUN echo "Done with unittest"

RUN echo && echo "View Filtlong help file:  " && \
filtlong -h

RUN echo && \
 echo "Run Filtlong with length and quality options on a pair of long read sequences in /data dir: " && \
 filtlong --min_length 250 --min_mean_q 40 SRR19008456_1.fastq.gz|gzip  > SRR19008456_1_filt.fastq.gz && \
 filtlong --min_length 250 --min_mean_q 40 SRR19008456_2.fastq.gz|gzip  > SRR19008456_2_filt.fastq.gz

 echo && echo "Successful installation of Filtlong-${FILTLONG_VER}"