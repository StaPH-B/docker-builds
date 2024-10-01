ARG ASSEMBLYSNPTYPER_VER="0.1.1"
ARG SAMTOOLS_VER="1.19"
ARG MINIMAP2_VER="2.28"

FROM ubuntu:jammy as builder

ARG SAMTOOLS_VER
ARG MINIMAP2_VER

# install dependencies required for compiling samtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    gcc \
    wget \
    make \
    perl \
    bzip2 \
    gnuplot \
    ca-certificates \
    curl

# download, compile, and install samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install

WORKDIR /usr/local/bin

RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner

### start of app stage ###
FROM ubuntu:jammy as app

ARG ASSEMBLYSNPTYPER_VER="0.1.1"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="assembly_snptyper"
LABEL software.version="${ASSEMBLYSNPTYPER_VER}"
LABEL description="Type assembly based on a VCF using minimap2 + samtools"
LABEL website="https://github.com/boasvdp/assembly_snptyper"
LABEL license="https://github.com/boasvdp/assembly_snptyper/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    zlib1g \
    libncurses5 \
    bzip2 \
    liblzma-dev \
    libcurl4-gnutls-dev \
    wget \
    ca-certificates \
    procps \
    python3 \
    python3-pip \
    python-is-python3 \
    curl \
    unzip \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# copy in samtools and minimap2 executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/

RUN pip install pandas

# install assembly_snptyper; make /data dir
RUN wget -q https://github.com/boasvdp/assembly_snptyper/archive/refs/tags/v${ASSEMBLYSNPTYPER_VER}.tar.gz && \
    pip install --no-cache-dir v${ASSEMBLYSNPTYPER_VER}.tar.gz && \
    tar -vxf v${ASSEMBLYSNPTYPER_VER}.tar.gz && \
    mv /assembly_snptyper-${ASSEMBLYSNPTYPER_VER} /assembly_snptyper && \
    rm v${ASSEMBLYSNPTYPER_VER}.tar.gz && \
    mkdir /data

ENV LC_ALL=C

CMD [ "assembly_snptyper", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app as test

RUN assembly_snptyper --help && \
    assembly_snptyper --version

WORKDIR /test

# running on S. pyogenes representative genome
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/900/475/035/GCA_900475035.1_41965_F01/GCA_900475035.1_41965_F01_genomic.fna.gz && \
    gunzip GCA_900475035.1_41965_F01_genomic.fna.gz && \
    ls *genomic.fna > fastas.txt && \
    assembly_snptyper --list_input fastas.txt -p 4 --reference /assembly_snptyper/data/MGAS5005.fa --vcf /assembly_snptyper/data/M1UK.vcf > m1uk.txt && \
    head m1uk.txt

RUN cd /assembly_snptyper && \
    bash tests/test_e2e.sh