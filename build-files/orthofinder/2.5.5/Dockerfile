ARG ORTHOFINDER_VER="2.5.5"

# base image
FROM mambaorg/micromamba:2.0.5-ubuntu22.04 AS app

ARG ORTHOFINDER_VER

USER root
WORKDIR /

# metadata
LABEL base.image="mambaorg/micromamba:2.0.5-ubuntu22.04"
LABEL version="1"
LABEL software="OrthoFinder"
LABEL software.version="${ORTHOFINDER_VER}"
LABEL description="Accurate inference of orthologous gene groups made easy"
LABEL website="https://github.com/davidemms/OrthoFinder"
LABEL license="https://github.com/davidemms/OrthoFinder/blob/master/License.md"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

RUN micromamba install --name base -c conda-forge -c bioconda orthofinder=${ORTHOFINDER_VER} && \
  micromamba clean -a -y && \
  mkdir /data

# add programs to path
ENV PATH="/opt/conda/bin/:${PATH}" LC_ALL=C.UTF-8

WORKDIR /data

CMD ["orthofinder", "-h"]

FROM app AS test

# install ubuntu dependencies
RUN apt-get update && apt-get -y install \
    wget \
    ca-certificates

WORKDIR /test

ARG ORTHOFINDER_VER

RUN orthofinder -h

RUN wget https://github.com/davidemms/OrthoFinder/releases/download/${ORTHOFINDER_VER}/ExampleData.tar.gz && \
  tar -xvf ExampleData.tar.gz && \
  orthofinder -f ExampleData

RUN micromamba list -n base
