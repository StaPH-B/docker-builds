FROM staphb/samtools:1.21 AS samtools 
FROM staphb/bedtools:2.31.1 AS bedtools

FROM ubuntu:jammy AS app
# Set global variables
ARG HOSTILE_VER="2.0.0"
ARG BOWTIE2_VER="2.5.1"
ARG MINIMAP2_VER="2.28"

LABEL base.image="ubuntu:jammy" 
LABEL dockerfile.version="1" 
LABEL software="hostile"
LABEL software.version=${HOSTILE_VER}
LABEL description="Precise host read removal."
LABEL website="https://github.com/bede/hostile"
LABEL license.url="https://github.com/bede/hostile?tab=MIT-1-ov-file#readme"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email="ltj8@cdc.gov"

# most of these are for samtools
RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    zlib1g \
    libncurses5 \
    bzip2 \
    liblzma5 \
    libcurl3-gnutls \
    libdeflate0 \
    wget \
    python3-pip \
    unzip \
    ca-certificates \
    curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


COPY --from=bedtools /usr/local/bin/* /usr/local/bin/
COPY --from=samtools /usr/local/bin/* /usr/local/bin/

# install bowtie2
RUN wget -q https://github.com/BenLangmead/bowtie2/releases/download/v${BOWTIE2_VER}/bowtie2-${BOWTIE2_VER}-linux-x86_64.zip && \ 
    unzip bowtie2-${BOWTIE2_VER}-linux-x86_64.zip && \
    rm bowtie2-${BOWTIE2_VER}-linux-x86_64.zip

# install minimap2
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner

# install hostile and get reference files
RUN wget -q https://github.com/bede/hostile/archive/refs/tags/${HOSTILE_VER}.tar.gz && \
    tar -xzvf ${HOSTILE_VER}.tar.gz && \
    mv /hostile-${HOSTILE_VER} /hostile && \
    pip install --no-cache-dir ${HOSTILE_VER}.tar.gz && \
    rm -rf ${HOSTILE_VER}.tar.gz && \
    mkdir /data

ENV PATH="/bowtie2-${BOWTIE2_VER}-linux-x86_64:/minimap2-${MINIMAP2_VER}_x64-linux:$PATH"

CMD ["hostile", "--help"]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN hostile clean --index /hostile/tests/data/sars-cov-2/sars-cov-2 --fastq1  /hostile/tests/data/sars-cov-2_1_1.fastq --fastq2  /hostile/tests/data/sars-cov-2_1_2.fastq

