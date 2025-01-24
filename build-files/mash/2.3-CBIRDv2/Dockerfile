ARG FOLDER_ID="1kUITKsrjBaxmxf5MXrZcDLIfrytz9zaX"
ARG FOLDER_NAME="C-BIRDv2_ref"

## Gdrive Download ##
FROM ubuntu:jammy AS downloader

ARG FOLDER_ID
ARG FOLDER_NAME

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/* &&\
    pip3 install --no-cache-dir gdown

# download sketch from gdrive
RUN gdown --folder ${FOLDER_ID} &&\
    cd ${FOLDER_NAME} &&\
    md5sum -c md5sum.txt

## App ##
FROM ubuntu:jammy AS app

ARG MASH_VER="v2.3"
ARG FOLDER_NAME

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MASH"
LABEL software.version=${MASH_VER}
LABEL description="MASH with C-BIRDv2 reference sketch"
LABEL website="https://github.com/marbl/Mash"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget &&\
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install mash
RUN wget --no-check-certificate https://github.com/marbl/Mash/releases/download/${MASH_VER}/mash-Linux64-${MASH_VER}.tar &&\
    tar -xvf mash-Linux64-${MASH_VER}.tar --no-same-owner &&\
    rm mash-Linux64-${MASH_VER}.tar &&\
    mv /mash-Linux64-${MASH_VER}/mash /usr/local/bin/

# copy reference mash sketch
COPY --from=downloader /${FOLDER_NAME} /db

ENV LC_ALL=C

CMD ["/bin/bash", "-c", "mash -h && echo '** C-BIRDv2 reference sketch is located at /db/cbird-v2.0-lite.msh'"]

WORKDIR /data

## Test ##
FROM app AS test

# check db
WORKDIR /db
RUN md5sum -c md5sum.txt &&\
    mash info cbird-v2.0-lite.msh | head -n 6

# download a test file [ Enterobacter hormaechei (CDC Enteric Group 75) FDAARGOS 1433 ]
WORKDIR /data
RUN wget -q --no-check-certificate https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/019/048/245/GCF_019048245.1_ASM1904824v1/GCF_019048245.1_ASM1904824v1_genomic.fna.gz &&\
    gunzip GCF_019048245.1_ASM1904824v1_genomic.fna.gz

# test screen
RUN mash screen -p 4 /db/cbird-v2.0-lite.msh GCF_019048245.1_ASM1904824v1_genomic.fna > screen.tsv &&\
    sort -gr screen.tsv > sorted.screen.tsv &&\
    head sorted.screen.tsv 