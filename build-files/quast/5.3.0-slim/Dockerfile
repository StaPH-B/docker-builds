FROM ubuntu:jammy as app

ARG QUAST_VER="5.3.0"
ARG MINIMAP2_VER="2.28"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="QUAST"
LABEL software.version=${QUAST_VER}
LABEL description="Genome assembly evaluation tool"
LABEL website="https://github.com/ablab/quast"
LABEL license="https://github.com/ablab/quast/blob/master/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    bzip2 \
    python-is-python3 \
    locales &&\
    locale-gen en_US.UTF-8 &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 &&\
    tar --no-same-owner -jxvf minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 && rm minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 &&\
    wget --no-check-certificate https://github.com/ablab/quast/releases/download/quast_${QUAST_VER}/quast-${QUAST_VER}.tar.gz &&\
    tar -xvf quast-${QUAST_VER}.tar.gz && rm quast-${QUAST_VER}.tar.gz

ENV PATH=$PATH:/quast-${QUAST_VER}:/minimap2-${MINIMAP2_VER}_x64-linux/ \
    LC_ALL=C

CMD quast.py --help && quast-lg.py --help && metaquast.py --help

WORKDIR /data

## Test ##
FROM app as test

ARG QUAST_VER
ARG DPATH="/quast-${QUAST_VER}/test_data"

# test quast
RUN quast.py ${DPATH}/contigs_1.fasta ${DPATH}/contigs_2.fasta -r ${DPATH}/reference.fasta.gz -o quast_out
# test metaquast
RUN metaquast.py ${DPATH}/meta_contigs_1.fasta ${DPATH}/meta_contigs_2.fasta -r ${DPATH}/meta_ref_1.fasta,${DPATH}/meta_ref_2.fasta,${DPATH}/meta_ref_3.fasta -o metaquast_out
