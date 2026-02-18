FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

# Version arguments
# ARG variables only persist during build time
ARG POPPUNK_VERSION="2.7.8"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="PopPUNK"
LABEL software.version=${POPPUNK_VERSION}
LABEL description="POPulation Partitioning Using Nucleotide Kmers"
LABEL website="https://github.com/bacpop/PopPUNK"
LABEL license="https://github.com/bacpop/PopPUNK/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"
LABEL maintainer2="Harry Hung"
LABEL maintainer2.email="ch31@sanger.ac.uk"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

#-------------------------------------------------------------------------
# Create PopPUNK conda environment called poppunk-env from bioconda recipe
# Original line from 2.7.7
# RUN micromamba create -n poppunk-env -c conda-forge -c bioconda poppunk=${POPPUNK_VERSION} && \
#     micromamba clean -a -f -y

# Test out a different version of setuptools
RUN micromamba create -n poppunk-env -c conda-forge -c bioconda \
    poppunk=${POPPUNK_VERSION} \
    setuptools=80.10.2 && \
    micromamba clean -a -f -y


#----------------------------------------------------------------------------------    
# set the environment, put new conda env in PATH by default; set locales to UTF-8
ENV PATH="/opt/conda/envs/poppunk-env/bin:${PATH}" \
    LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

CMD ["poppunk", "--help"]

# new base for testing
FROM app AS test

# print out various help options and version
RUN poppunk --help && \
    poppunk_assign --help && \
    poppunk_visualise --help && \
    poppunk_mst --help && \
    poppunk_references --help && \
    poppunk_info --help && \
    poppunk_mandrake --help && \
    poppunk --version

# Download 100 S. Pneumo assemblies from GPS Public Data on ENA
# Build PopPUNK database from the assemblies
# Assign clusters on the same assemblies using the built database
# Compare the database clusters and assigned clusters of the assemblies
RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/refs/heads/master/build-files/poppunk/2.7.5/ftps.txt && \
    wget https://raw.githubusercontent.com/StaPH-B/docker-builds/refs/heads/master/build-files/poppunk/2.7.5/test.sh && \
    bash test.sh && cmp assigned.csv database.csv

RUN micromamba list -n poppunk-env
