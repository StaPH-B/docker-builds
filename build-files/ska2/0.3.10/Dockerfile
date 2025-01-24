FROM ubuntu:jammy as app

ARG SKA2_VER="0.3.10"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SKA2"
LABEL software.version="${SKA2_VER}"
LABEL description="A reimplementation of the SKA package in the rust language"
LABEL website="https://github.com/bacpop/ska.rust"
LABEL license="https://github.com/bacpop/ska.rust/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/bacpop/ska.rust/releases/download/v${SKA2_VER}/ska-v${SKA2_VER}-ubuntu-latest-stable.tar.gz &&\
    tar -C /usr/local/bin -xvf ska-v${SKA2_VER}-ubuntu-latest-stable.tar.gz ska &&\
    rm ska-v${SKA2_VER}-ubuntu-latest-stable.tar.gz

ENV LC_ALL=C

CMD [ "ska", "-h" ]

WORKDIR /data

## Test ##
FROM app as test

# force bash to avoid shell errors
SHELL ["/bin/bash", "-c"]

# adapted from tutorial https://www.bacpop.org/guides/building_trees_with_ska/
RUN wget --no-check-certificate https://zenodo.org/record/8172518/files/building_trees_with_ska.tar &&\
    tar -xvf building_trees_with_ska.tar assemblies/LA002.fa.gz assemblies/LA022.fa.gz assemblies/LA023.fa.gz assemblies/LA026.fa.gz &&\    
    paste <(ls assemblies | sed 's/[.].*$//g') <(ls -d assemblies/*) > laos_ska_input.tsv

RUN ska build -f laos_ska_input.tsv -k 31 -o laos_ska_index --threads 4 &&\
    ska align --min-freq 1 --filter no-filter laos_ska_index.skf -o laos_ska_alignment.aln --threads 4 &&\
    head -c 1000 laos_ska_alignment.aln &&\
    grep ">" laos_ska_alignment.aln



