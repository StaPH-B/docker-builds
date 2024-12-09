FROM mambaorg/micromamba:1.4.1 as app

# Version arguments
# ARG variables only persist during build time
ARG FREYJA_SOFTWARE_VERSION="1.4.3"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:1.4.1"
LABEL dockerfile.version="1"
LABEL software="Freyja"
LABEL software.version=${FREYJA_SOFTWARE_VERSION}
LABEL description="Freyja is a tool to recover relative lineage abundances from mixed SARS-CoV-2 samples from a sequencing dataset (BAM aligned to the Hu-1 reference)"
LABEL website="https://github.com/andersen-lab/Freyja"
LABEL license="https://github.com/andersen-lab/Freyja/blob/main/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@theiagen.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Create Freyja conda environment called freyja-env from bioconda recipe
# clean up conda garbage
RUN micromamba create -n freyja-env -c conda-forge -c bioconda -c defaults freyja=${FREYJA_SOFTWARE_VERSION} && \
    micromamba clean -a -y

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/freyja-env/bin:/opt/conda/envs/env/bin:${PATH}" \
    LC_ALL=C.UTF-8

RUN freyja update

# set working directory to /data
WORKDIR /data

# default command is to pull up help options
CMD [ "freyja", "--help" ]

# new base for testing
FROM app as test

# Grab test data from Freyja version 1.3.4
RUN wget -O /data/Freyja_WWSC2.bam https://github.com/StaPH-B/docker-builds/blob/master/freyja/1.3.4/tests/Freyja_WWSC2.bam?raw=true -O /data/Freyja_WWSC2.bam && \
    wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/freyja/1.3.4/tests/Freyja_depths.tsv && \
    wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/freyja/1.3.4/tests/Freyja_variants.tsv && \
    wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/freyja/1.3.4/tests/nCoV-2019.reference.fasta

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="freyja-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Run Freyja
RUN freyja variants /data/Freyja_WWSC2.bam --variants /data/test_variants.tsv --depths /data/test_depths.tsv --ref /data/nCoV-2019.reference.fasta && \
    freyja demix /data/test_variants.tsv /data/test_depths.tsv --output /data/test_demix.tsv

# Check validity of outputs
RUN head /data/test_variants.tsv && \
    head /data/test_depths.tsv && \
    head /data/test_demix.tsv && \
    grep "Omicron" /data/test_demix.tsv

# test new Freyja demix version option
RUN freyja demix --version && freyja --version
