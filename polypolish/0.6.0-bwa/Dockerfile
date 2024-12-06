ARG POLYPOLISH_VER="0.6.0"
ARG BWA_VER="0.7.18"

FROM rust:1.75 AS builder

ARG POLYPOLISH_VER
ARG BWA_VER

RUN wget -q https://github.com/rrwick/Polypolish/archive/refs/tags/v${POLYPOLISH_VER}.tar.gz && \
    tar -vxf v${POLYPOLISH_VER}.tar.gz && \
    cd /Polypolish-${POLYPOLISH_VER} && \
    cargo build --release 

RUN wget https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz &&\
    tar -xvf v${BWA_VER}.tar.gz &&\
    cd bwa-${BWA_VER} &&\
    make &&\
    mv bwa /usr/local/bin/

FROM ubuntu:jammy AS app

ARG POLYPOLISH_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="polypolish"
LABEL software.version="${POLYPOLISH_VER}"
LABEL description="Polypolish is a tool for polishing genome assemblies with short reads."
LABEL website="https://github.com/rrwick/Polypolish"
LABEL license="https://github.com/rrwick/Polypolish/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Sage Wright"
LABEL maintainer2.email="sagemwright@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    unzip \
    python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /Polypolish-${POLYPOLISH_VER}/target/release/polypolish /usr/local/bin/polypolish
COPY --from=builder /usr/local/bin/bwa /usr/local/bin/

ENV LC_ALL=C

CMD ["polypolish", "--help"]

WORKDIR /data

FROM app AS test

RUN polypolish --help && polypolish --version

# using "toy" data
RUN wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/assembly.fasta && \
    wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/alignments.sam && \
    polypolish polish assembly.fasta alignments.sam > polished.fasta

# testing bwa
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_1.fastq.gz -O r1.fq.gz &&\
wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_2.fastq.gz -O r2.fq.gz &&\
wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz &&\
gunzip -c GCF_000006945.2_ASM694v2_genomic.fna.gz > ref.fa

RUN bwa index ref.fa &&\
bwa mem ref.fa r1.fq.gz r2.fq.gz > aln.sam &&\
head aln.sam