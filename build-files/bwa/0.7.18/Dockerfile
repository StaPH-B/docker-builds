ARG BWA_VER=0.7.18

## Builder ##
FROM ubuntu:jammy as builder

ARG BWA_VER

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    make \
    gcc \
    zlib1g-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz &&\
    tar -xvf v${BWA_VER}.tar.gz &&\
    cd bwa-${BWA_VER} &&\
    make &&\
    mv bwa /usr/local/bin/

## App ##
FROM ubuntu:jammy as app 

ARG BWA_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="BWA"
LABEL software.version="${BWA_VER}"
LABEL description="Burrows-Wheeler Alignment Tool"
LABEL website="https://github.com/lh3/bwa"
LABEL license="https://github.com/lh3/bwa/blob/master/COPYING"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/bwa /usr/local/bin/

ENV LC_ALL=C

CMD ["bwa"]

WORKDIR /data

## Test ##
FROM app as test

RUN apt-get update && apt-get install -y wget

RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_1.fastq.gz -O r1.fq.gz &&\
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_2.fastq.gz -O r2.fq.gz &&\
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz &&\
    gunzip -c GCF_000006945.2_ASM694v2_genomic.fna.gz > ref.fa

RUN bwa index ref.fa &&\
    bwa mem ref.fa r1.fq.gz r2.fq.gz > aln.sam &&\
    head aln.sam