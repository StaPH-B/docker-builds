FROM mambaorg/micromamba:1.5.8 as app

ARG IPA_VER="1.8.0"

SHELL [ "/bin/bash", "-c" ]
USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="IPA"
LABEL software.version="${IPA_VER}"
LABEL description="PacBio Improved Phased Assembler"
LABEL website="https://github.com/PacificBiosciences/pbipa"
LABEL license="https://github.com/PacificBiosciences/pbipa/blob/master/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    time \
    procps && \    
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda python=3.8 pbipa=${IPA_VER} && \    
    eval "$(micromamba shell hook --shell bash)" &&\
    micromamba clean -a -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "ipa", "--help" ]

WORKDIR /data

## Test ##
FROM app as test

RUN apt-get update && apt-get install -y wget

RUN ipa validate

RUN wget -q https://downloads.pacbcloud.com/public/dataset/2021-11-Microbial-96plex/demultiplexed-reads/m64004_210929_143746.bc2009.bam &&\
    ipa local --njobs 1 --nthreads 4 -i m64004_210929_143746.bc2009.bam &&\
    head -c 1000 RUN/assembly-results/final.a_ctg.fasta



