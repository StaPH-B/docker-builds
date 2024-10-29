FROM ubuntu:jammy AS app

ARG CHECKV_VER="1.0.3"
ARG DIAMOND_VER="2.1.8"
ARG PRODIGALGV_VER="2.11.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="CheckV"
LABEL software.version="${CHECKV_VER}"
LABEL description="CheckV is a fully automated command-line pipeline for assessing the quality of single-contig viral genomes"
LABEL website="https://bitbucket.org/berkeleylab/checkv/"
LABEL license="https://bitbucket.org/berkeleylab/checkv/src/master/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    hmmer \
    ncbi-blast+ \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install diamond
RUN wget -q https://github.com/bbuchfink/diamond/releases/download/v${DIAMOND_VER}/diamond-linux64.tar.gz &&\
    tar -C /usr/local/bin/ -xvf diamond-linux64.tar.gz &&\
    rm diamond-linux64.tar.gz
# install prodigal-gv
RUN wget -q https://github.com/apcamargo/prodigal-gv/releases/download/${PRODIGALGV_VER}/prodigal-gv-linux &&\
    chmod +x prodigal-gv-linux &&\
    mv prodigal-gv-linux /usr/local/bin/prodigal-gv
# install checkv
RUN pip3 install --no-cache-dir checkv==${CHECKV_VER}

ENV LC_ALL=C

CMD [ "checkv", "--help" ]

WORKDIR /data


## Test ##
FROM app AS test 

# download database (current v1.5)
RUN checkv download_database /db 

# download test fna and run checkv
RUN wget -q https://bitbucket.org/berkeleylab/checkv/raw/51a5293f75da04c5d9a938c9af9e2b879fa47bd8/test/test_sequences.fna &&\
    checkv end_to_end -d /db/checkv-db-v1.5 test_sequences.fna test_out -t 4


