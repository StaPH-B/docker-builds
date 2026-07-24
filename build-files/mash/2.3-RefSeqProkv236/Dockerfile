FROM ubuntu:noble AS app

ARG MASH_VER="v2.3"
ARG SKETCH_VER="236"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Mash"
LABEL software.version="2.3"
LABEL description="Fast genome/metagenome distance estimation (MinHash), bundled with a refreshed RefSeq prokaryotic reference sketch (Zenodo 10.5281/zenodo.20293962)"
LABEL website="https://github.com/marbl/Mash"
LABEL license="https://github.com/marbl/Mash/blob/master/LICENSE.txt"
LABEL maintainer="Arnold Rodriguez"
LABEL maintainer.email="arnold.rodriguezhilario@flhealth.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install mash 2.3 precompiled linux64 binary
RUN wget https://github.com/marbl/Mash/releases/download/${MASH_VER}/mash-Linux64-${MASH_VER}.tar && \
    tar -xvf mash-Linux64-${MASH_VER}.tar --no-same-owner && \
    rm mash-Linux64-${MASH_VER}.tar && \
    mv /mash-Linux64-${MASH_VER}/mash /usr/local/bin/ && \
    mkdir /data

# refreshed RefSeq prokaryotic sketch, embedded at build time
RUN mkdir /db && cd /db && \
    wget -O RefSeqProkSketchesv${SKETCH_VER}.msh.gz "https://zenodo.org/records/21341143/files/RefSeqSketches_${SKETCH_VER}.msh.gz?download=1" && \
    gunzip RefSeqProkSketchesv${SKETCH_VER}.msh.gz

ENV LC_ALL=C

CMD ["/bin/bash", "-c", "mash -h && echo '** RefSeq prokaryotic reference sketch (v235) is located at /db/RefSeqProkSketchesv235.msh'"]

WORKDIR /data

FROM app AS test

ARG SKETCH_VER

# verify tool and reference sketch integrity
WORKDIR /db
RUN mash --version && mash -h && \
    mash info RefSeqProkSketchesv${SKETCH_VER}.msh | head -n 10

# functional test: Enterobacter hormaechei FDAARGOS_1433 (ECC) screened against the refreshed sketch
WORKDIR /test
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/019/048/245/GCF_019048245.1_ASM1904824v1/GCF_019048245.1_ASM1904824v1_genomic.fna.gz && \
    gunzip GCF_019048245.1_ASM1904824v1_genomic.fna.gz && \
    mash screen -p 4 /db/RefSeqProkSketchesv${SKETCH_VER}.msh GCF_019048245.1_ASM1904824v1_genomic.fna | sort -gr | head
