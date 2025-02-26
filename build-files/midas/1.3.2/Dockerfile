## Builder ##
ARG MIDAS_VER="1.3.2"

FROM ubuntu:jammy as builder

RUN apt update && apt-get install -y \
    build-essential \
    wget \
    python2-dev \
	zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libncurses5-dev \
    curl

# build samtools 1.4
RUN wget --no-check-certificate https://github.com/samtools/samtools/releases/download/1.4/samtools-1.4.tar.bz2 &&\
    tar -xvf samtools-1.4.tar.bz2 &&\
    cd samtools-1.4 &&\
    ./configure && make && make install

# get python/pip dependencies  
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2 1 &&\
    curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py &&\
    python get-pip.py &&\
    pip install --user --no-cache-dir pandas==0.20.3 biopython==1.70 numpy==1.8.2 pysam==0.13 

## APP ##
FROM ubuntu:jammy as app

ARG MIDAS_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MIDAS"
LABEL software.version="${MIDAS_VER}"
LABEL description="Metagenomic Intra-Species Diversity Analysis System"
LABEL website="https://github.com/snayfach/MIDAS"
LABEL license="https://github.com/snayfach/MIDAS/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    python2 \
    zlib1g-dev \
    libcurl4 \
    bowtie2 \
    hmmer \
    vsearch &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install MIDAS   
RUN wget --no-check-certificate https://github.com/snayfach/MIDAS/archive/refs/tags/v${MIDAS_VER}.tar.gz &&\
    tar -xvf v${MIDAS_VER}.tar.gz && rm v${MIDAS_VER}.tar.gz &&\
    rm /MIDAS-${MIDAS_VER}/bin/Linux/bowtie2* &&\
    rm /MIDAS-${MIDAS_VER}/bin/Linux/samtools &&\
    ln -s /usr/bin/bowtie2* /MIDAS-${MIDAS_VER}/bin/Linux/ &&\
    update-alternatives --install /usr/bin/python python /usr/bin/python2 1

# collect dependencies from builder
COPY --from=builder /usr/local/bin/* /MIDAS-${MIDAS_VER}/bin/Linux/
COPY --from=builder /root/.local /root/.local

ENV PYTHONPATH="/MIDAS-${MIDAS_VER}:$PYTHONPATH"
ENV PATH="/MIDAS-${MIDAS_VER}/scripts:/MIDAS-${MIDAS_VER}/bin/Linux:/root/.local/bin:$PATH"
ENV LC_ALL=C

WORKDIR /data

## TEST ##
FROM app as test

ARG MIDAS_VER

# change workdir for test
WORKDIR /MIDAS-${MIDAS_VER}/test/

# create a test database
RUN tar --no-same-owner -xvf genomes.tar.gz &&\
    build_midas_db.py genomes genomes.mapfile /midas_database

# test runs with test db
RUN run_midas.py species ./sample -1 ./test.fq.gz -n 100 -d /midas_database &&\
    run_midas.py genes ./sample -1 ./test.fq.gz -n 100 --species_id Bacteroides_vulgatus -d /midas_database &&\
    run_midas.py snps ./sample -1 ./test.fq.gz -n 100 --species_id Bacteroides_vulgatus -d /midas_database