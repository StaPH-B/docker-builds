FROM mambaorg/micromamba:0.23.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG sets environment variables during the build stage
ARG NGMASTER_VER="0.5.8"

LABEL base.image="mambaorg/micromamba:0.23.0"
LABEL dockerfile.version="1"
LABEL software="ngmaster"
LABEL software.version=${NGMASTER_VER}
LABEL description="In silico multi-antigen sequence typing for Neisseria gonorrhoeae (NG-MAST)"
LABEL website="https://github.com/MDU-PHL/ngmaster"
LABEL license="https://github.com/MDU-PHL/ngmaster/blob/master/LICENSE"
LABEL maintainer="Curtis kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"

# Install dependencies via apt-get; procps to get the 'ps' command for nextflow compatibility
# cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# create conda env 'ngmaster-env' and install python, pip, biopython, isPcr version 33;
# cleanup conda garbage
RUN micromamba create -n ngmaster-env -c bioconda -c conda-forge -c defaults \
 python>=3.6 \
 pip \
 biopython \
 ispcr=33 && \
 micromamba clean -a -y

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="ngmaster-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# install ngmaster via pypi; using pip installed via micromamba
RUN pip install ngmaster==${NGMASTER_VER}

# hardcode conda env into the PATH; set locale settings
ENV PATH="${PATH}:/opt/conda/envs/ngmaster-env/bin/" \
 LC_ALL=C.UTF-8

# set final & default working dir to /data
WORKDIR /data

# test layer
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="ngmaster-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# show help and version outputs; run the program's internal tests
RUN ngmaster --help && ngmaster --version && \
 ngmaster --test
