FROM mambaorg/micromamba:2.3.0-ubuntu22.04 AS app

ARG HICEXPLORER_VER="3.7.6"

USER root
WORKDIR /

# metadata
LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="HiCExplorer"
LABEL software.version="${HICEXPLORER_VER}"
LABEL description="A powerful and easy to use set of tools to process, normalize and visualize Hi-C data"
LABEL website="https://github.com/deeptools/HiCExplorer"
LABEL license="https://github.com/deeptools/HiCExplorer/blob/master/LICENSE"
LABEL maintainer="Weifan Lv"
LABEL maintainer.email="lvweifan@pku.edu.cn"

RUN micromamba install --name base -c conda-forge -c bioconda hicexplorer=${HICEXPLORER_VER} && \
  micromamba clean -a -f -y && \
  mkdir /data

# add programs to path
ENV PATH="/opt/conda/bin/:${PATH}" LC_ALL=C.UTF-8

WORKDIR /data

CMD ["hicexplorer", "-h"]

FROM app AS test

# install ubuntu dependencies
RUN apt-get update && apt-get -y install \
    wget \
    ca-certificates

WORKDIR /test

RUN hicexplorer -h

RUN wget https://github.com/open2c/cooler/raw/refs/heads/master/tests/data/manycontigs.1.cool && \
  hicInfo -m manycontigs.1.cool

RUN micromamba list -n base
