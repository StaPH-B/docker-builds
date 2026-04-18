FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

ARG PLING_VER="3.0.1"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="Pling"
LABEL software.version="${PLING_VER}"
LABEL description="Pling is a software workflow for plasmid analysis using rearrangement distances, specifically the Double Cut and Join Indel (DCJ-Indel) distance."
LABEL website="https://github.com/iqbal-lab-org/pling"
LABEL license="https://github.com/iqbal-lab-org/pling/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

RUN micromamba install --name base -c conda-forge -c bioconda pling=${PLING_VER} && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

WORKDIR /data

CMD [ "pling", "--help" ]

FROM app AS test

RUN apt-get update && apt-get -y install --no-install-recommends \
    curl \
    ca-certificates \
    xz-utils && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /test

RUN pling --help && pling --version

# adapted from https://pling.readthedocs.io/latest/tutorial.html
# Unfortunately the old link: https://figshare.com/ndownloader/files/48723568 is no longer readily accessible through curl or wget.
COPY fastas.tar.xz /test/fastas.tar.xz
    
RUN tar -xvf fastas.tar.xz && \
    cd fastas && \
    ls -d -1 $PWD/*.fna > ../input.txt && \
    cd .. && \
    head -n 20 input.txt > test.txt
    
RUN pling cluster align test.txt pling_out --cores 8 --sourmash --visualisation all

RUN micromamba list -n base