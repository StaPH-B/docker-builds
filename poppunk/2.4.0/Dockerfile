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
LABEL software.version=${FREYJA_SOFTWARE_VERSION}
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

# Create Freyja conda environment called freyja-env from bioconda recipe
# clean up conda garbage
RUN micromamba create -n poppunk-env -c conda-forge -c bioconda -c defaults poppunk=${POPPUNK_VERSION} && \
 micromamba clean -a -y

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/poppunk-env/bin:${PATH}" \
 LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

# new base for testing
FROM app as test

RUN poppunk --help && poppunk --version

# Grab test data
# RUN wget -O /data/Freyja_WWSC2.bam https://github.com/StaPH-B/docker-builds/blob/master/freyja/1.3.4/tests/Freyja_WWSC2.bam?raw=true -O /data/Freyja_WWSC2.bam && \
#  wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/freyja/1.3.4/tests/Freyja_depths.tsv && \
#  wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/freyja/1.3.4/tests/Freyja_variants.tsv && \
#  wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/freyja/1.3.4/tests/nCoV-2019.reference.fasta

# # so that mamba/conda env is active when running below commands
# ENV ENV_NAME="freyja-env"
# ARG MAMBA_DOCKERFILE_ACTIVATE=1

# # Run Freyja
# RUN freyja variants /data/Freyja_WWSC2.bam --variants /data/test_variants.tsv --depths /data/test_depths.tsv --ref /data/nCoV-2019.reference.fasta && freyja demix /data/test_variants.tsv /data/test_depths.tsv --output /data/test_demix.tsv

# # Check validity of outputs
# RUN cmp /data/test_variants.tsv /data/Freyja_variants.tsv && cmp /data/test_depths.tsv /data/Freyja_depths.tsv
# RUN grep "Omicron" /data/test_demix.tsv && echo done
