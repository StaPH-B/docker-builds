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
# The link used in the prior dockerfile, https://figshare.com/ndownloader/files/48723568 , can be to download fastas.tar.xz 
# if used over Codespaces or if Figshare is not impacted by firewalls or security software with the following command:
# wget --content-disposition https://figshare.com/ndownloader/files/48723568

# For local builds, we can use the Figshare API instead.
RUN curl -L https://api.figshare.com/v2/file/download/48723568 -o fastas.tar.xz && \
    tar -xvf fastas.tar.xz && \
    ls -d $(pwd)/fastas/*.fna > input.txt && \
    head -n 20 input.txt > test.txt

RUN pling cluster align test.txt pling_out --cores 4 --sourmash --visualisation all &&\
    cat pling_out/all_plasmids_distances.tsv

RUN micromamba list -n base