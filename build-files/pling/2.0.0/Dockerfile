FROM mambaorg/micromamba:2.0.8-ubuntu22.04 AS app

ARG PLING_VER="2.0.0"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.0.8-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Pling"
LABEL software.version="${PLING_VER}"
LABEL description="Pling is a software workflow for plasmid analysis using rearrangement distances, specifically the Double Cut and Join Indel (DCJ-Indel) distance."
LABEL website="https://github.com/iqbal-lab-org/pling"
LABEL license="https://github.com/iqbal-lab-org/pling/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN micromamba install --name base -c conda-forge -c bioconda pling=${PLING_VER} && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "pling", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test 

RUN apt-get update && apt-get install -y wget xz-utils

# adapted from https://pling.readthedocs.io/latest/tutorial.html
RUN wget --content-disposition https://figshare.com/ndownloader/files/48723568 &&\
    tar -xvf fastas.tar.xz &&\
    ls -d $(pwd)/fastas/*.fna > input.txt &&\
    head -n 20 input.txt > test.txt
    
RUN pling input.txt pling_out align --cores 4 --sourmash &&\
    cat pling_out/all_plasmids_distances.tsv




