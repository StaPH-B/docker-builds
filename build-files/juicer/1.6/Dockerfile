FROM ubuntu:noble AS builder

ARG BWA_VER="0.7.19"
ARG SAMTOOLS_VER="1.24"

# install dependencies required for compiling samtools and bwa
RUN apt-get update && apt-get install --no-install-recommends -y \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    libdeflate-dev \
    gcc \
    make \
    bzip2 \
    wget \
    ca-certificates

# build bwa
RUN wget https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz -qO - | tar xvz && \
    cd bwa-${BWA_VER} && \
    make && \
    mv bwa /usr/local/bin/

# build samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 -qO - | tar xvj && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install


FROM ubuntu:noble AS app

ARG JUICER_VER="1.6"
ARG JUICER_TOOLS_VER="1.22.01"

# metadata
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Juicer"
LABEL software.version="${JUICER_VER}"
LABEL description="A One-Click System for Analyzing Loop-Resolution Hi-C Experiments"
LABEL website="https://github.com/theaidenlab/Juicer"
LABEL license="https://github.com/theaidenlab/Juicer/blob/master/LICENSE"
LABEL maintainer="Weifan Lv"
LABEL maintainer.email="lvweifan@pku.edu.cn"

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    libdeflate-dev \
    default-jdk \
    python-is-python3 \
    perl-modules \
    gawk \
    locales \
    bzip2 \
    wget \
    ca-certificates \
    procps \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# gawk has the 'and' function, needed for chimeric_blacklist
RUN update-alternatives --set awk /usr/bin/gawk

# need to be sure we have this for stats
RUN locale-gen en_US.UTF-8

WORKDIR /opt/

# copy in samtools and bwa executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/

# install juicer
RUN wget https://github.com/theaidenlab/juicer/archive/${JUICER_VER}.tar.gz -qO - | tar xvz

# install juicer tools
RUN wget https://s3.amazonaws.com/hicfiles.tc4ga.com/public/juicer/juicer_tools_${JUICER_TOOLS_VER}.jar -qO /opt/juicer-${JUICER_VER}/CPU/common/juicer_tools.jar

RUN mkdir /opt/juicer && \
    ln -s /opt/juicer-${JUICER_VER}/CPU /opt/juicer/scripts && \
    ln -s /opt/juicer-${JUICER_VER}/misc /opt/juicer/misc && \
    chmod +x /opt/juicer/misc/*

ENV PATH=/opt/juicer/scripts:/opt/juicer/scripts/misc:/opt/juicer/scripts/common:$PATH LC_ALL=C.UTF-8

CMD ["juicer.sh", "--help"]

FROM app AS test

WORKDIR /test

RUN mkdir fastq

RUN wget https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR139/079/SRR13994279/SRR13994279_1.fastq.gz -O - | gzip -dc | head -n 1000000 > fastq/SRR13994279_R1.fastq

RUN wget https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR139/079/SRR13994279/SRR13994279_2.fastq.gz -O - | gzip -dc | head -n 1000000 > fastq/SRR13994279_R2.fastq

RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/002/163/515/GCA_002163515.1_ASM216351v1/GCA_002163515.1_ASM216351v1_genomic.fna.gz -O - | gzip -dc > reference.fna

RUN bwa index reference.fna

RUN python /opt/juicer/misc/generate_site_positions.py DpnII reference.fna reference.fna

RUN awk -vOFS=\\t '{print $1,$NF}' reference.fna_DpnII.txt > reference.fna.chrom.sizes

RUN juicer.sh -z reference.fna -y reference.fna_DpnII.txt -p reference.fna.chrom.sizes

RUN ls -al aligned
