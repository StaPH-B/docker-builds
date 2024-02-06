ARG QUAST_VER="5.2.0"

FROM ubuntu:jammy as app

ARG QUAST_VER

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
    python3-pip \
    minimap2 \
    locales &&\
    locale-gen en_US.UTF-8 &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache quast==${QUAST_VER}

ENV LC_ALL=C

CMD quast.py --help && quast-lg.py --help && metaquast.py --help

WORKDIR /data

## Test ##
FROM app as test

ARG QUAST_VER

RUN apt-get update && apt-get install -y wget
# download test data
RUN wget https://github.com/ablab/quast/releases/download/quast_${QUAST_VER}/quast-${QUAST_VER}.tar.gz &&\
    tar --strip-components=1 -xvf  quast-${QUAST_VER}.tar.gz quast-${QUAST_VER}/test_data

# test quast
RUN quast.py test_data/contigs_1.fasta test_data/contigs_2.fasta -r test_data/reference.fasta.gz -o quast_out
# test metaquast
RUN metaquast.py test_data/meta_contigs_1.fasta test_data/meta_contigs_2.fasta -r test_data/meta_ref_1.fasta,test_data/meta_ref_2.fasta,test_data/meta_ref_3.fasta -o metaquast_out
