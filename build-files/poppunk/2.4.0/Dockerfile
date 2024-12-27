FROM mambaorg/micromamba:0.24.0 as app

# Version arguments
# ARG variables only persist during build time
ARG POPPUNK_VERSION="2.4.0"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:0.24.0"
LABEL dockerfile.version="1"
LABEL software="PopPUNK"
LABEL software.version=${POPPUNK_VERSION}
LABEL description="POPulation Partitioning Using Nucleotide Kmers"
LABEL website="https://github.com/bacpop/PopPUNK"
LABEL license="https://github.com/bacpop/PopPUNK/blob/master/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="curtis.kapsak@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Create PopPUNK conda environment called poppunk-env from bioconda recipe
# clean up conda garbage
RUN micromamba create -n poppunk-env -c conda-forge -c bioconda -c defaults poppunk=${POPPUNK_VERSION} && \
 micromamba clean -a -y

# set the environment, put new conda env in PATH by default; set locales to UTF-8
ENV PATH="/opt/conda/envs/poppunk-env/bin:${PATH}" \
 LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

# new base for testing
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="poppunk-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# print out various help options and version
RUN poppunk --help && \
 poppunk_assign --help && \
 poppunk_visualise --help && \
 poppunk_mst --help && \
 poppunk_prune --help && \
 poppunk_references --help && \
 poppunk_tsne --help && \
 poppunk --version
