FROM ubuntu:jammy as app 

ARG PBMM2_VER="1.13.1"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pbmm2"
LABEL software.version="${PBMM2_VER}"
LABEL description="A minimap2 SMRT wrapper for PacBio data: native PacBio data in and out."
LABEL website="https://github.com/PacificBiosciences/pbmm2"
LABEL license="https://github.com/PacificBiosciences/pbmm2/blob/develop/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends  -y \
    wget &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -P /usr/local/bin/ --no-check-certificate https://github.com/PacificBiosciences/pbmm2/releases/download/v${PBMM2_VER}/pbmm2 &&\
    chmod 755 /usr/local/bin/pbmm2

ENV LC_ALL=C

CMD ["pbmm2", "-h"]

WORKDIR /data

## Test ##
FROM app as test

RUN wget -q --no-check-certificate https://downloads.pacbcloud.com/public/dataset/HiFiViral/Nov_2021/m64012_210821_095651.hifi_reads.bam &&\
    wget -q --no-check-certificate https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/858/895/GCF_009858895.2_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.fna.gz &&\
    gunzip -c GCF_009858895.2_ASM985889v3_genomic.fna.gz > ref.fasta

RUN pbmm2 index ref.fasta ref.mmi --preset HiFi &&\
    pbmm2 align -j 4 ref.mmi m64012_210821_095651.hifi_reads.bam mapped.hifi.reads.bam --preset HiFi

