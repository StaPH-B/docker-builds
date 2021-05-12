FROM debian:stretch

ENV DEBIAN_FRONTEND noninteractive

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="mlst"
LABEL software.version="2.19.0"
LABEL description="CGE Multi-Locus Sequence Typing 2.0"
LABEL website="https://cge.cbs.dtu.dk/services/MLST/"
LABEL maintainer="Center for Genomic Epidemiology"
LABEL maintainer.email="food-cgehelp@dtu.dk"
LABEL comments="MLST allele sequence and profile data are obtained from PubMLST.org."
LABEL comments="Campylobacter coli and Campylobacter jejuni are considered together."
LABEL comments="Input can be fasta or fastq."
LABEL comments="doi: 10.1128/JCM.06094-11"

### RUN set -ex; \
RUN apt-get update && apt-get install -y \
 build-essential \
 autoconf \
 zlib1g-dev \
 python3 \
 wget \
 libbz2-dev \
 liblzma-dev \
 libncurses-dev \
 git \
 bedtools \
 python3-pip \
 vim \
 nano && \
 apt-get install -y -qq git \
 apt-utils \
 ncbi-blast+ \
 libz-dev 
    
ENV DEBIAN_FRONTEND Teletype

# Install python dependencies
RUN pip3 install -U biopython==1.73 tabulate cgecore==1.4.4

# Clone and enter the CGE mlst directory
RUN git clone https://bitbucket.org/genomicepidemiology/mlst.git \
	&& cd mlst
# Download and install MLST database
RUN git clone https://bitbucket.org/genomicepidemiology/mlst_db.git \
	&& cd mlst_db

# Install kma
RUN git clone --depth 1 https://bitbucket.org/genomicepidemiology/kma.git; \
    cd kma && make; \
    mv kma* /bin/

RUN ln -s /mlst_db /database

ENV PATH $PATH:/mlst

WORKDIR /workdir

