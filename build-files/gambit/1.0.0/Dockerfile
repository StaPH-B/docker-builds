# Software installation, no database files
FROM mambaorg/micromamba:0.27.0 as app_base

ARG GAMBIT_SOFTWARE_VERSION="1.0.0"
ARG GAMBIT_GIT_TAG=v${GAMBIT_SOFTWARE_VERSION}
ARG GAMBIT_SRC_URL=https://github.com/jlumpe/gambit/archive/refs/tags/${GAMBIT_GIT_TAG}.tar.gz

LABEL base.image="mambaorg/micromamba:0.27.0"
LABEL dockerfile.version="1"
LABEL software="GAMBIT"
LABEL software.version=${GAMBIT_SOFTWARE_VERSION}
LABEL description="Rapid genomic-distance comparison for taxonomic identification of microbial pathogens"
LABEL website="https://github.com/jlumpe/gambit"
LABEL license="https://github.com/jlumpe/gambit/blob/master/LICENSE"
LABEL maintainer1="Kevin Libuit"
LABEL maintainer.email1="kevin.libuit@theiagen.com"
LABEL maintainer2="Michelle Scribner"
LABEL maintainer.email2="michelle.scribner@theiagen.com"
LABEL maintainer3="Jared Lumpe"
LABEL maintainer.email3="jared@jaredlumpe.com"

# Environment
ENV GAMBIT_DB_PATH=/gambit-db
ENV LC_ALL=C.UTF-8

# Install mamba environment
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

ARG MAMBA_DOCKERFILE_ACTIVATE=1  # Subsequent RUN commands use environment

# Install GAMBIT package
RUN pip install ${GAMBIT_SRC_URL} && \
  micromamba clean -a -y

USER root
RUN mkdir $GAMBIT_DB_PATH /data && \
  chown $MAMBA_USER:$MAMBA_USER $GAMBIT_DB_PATH /data
USER $MAMBA_USER
WORKDIR /data

# Make sure conda, python, and GAMBIT are in the path
ENV PATH="/opt/conda/bin:${PATH}"


# With database files added
FROM app_base AS app

ARG GAMBIT_DB_BASE_URL=https://storage.googleapis.com/jlumpe-gambit/public/databases/refseq-curated/1.0
ARG GAMBIT_DB_GENOMES_URL=$GAMBIT_DB_BASE_URL/gambit-refseq-curated-1.0.gdb
ARG GAMBIT_DB_SIGNATURES_URL=$GAMBIT_DB_BASE_URL/gambit-refseq-curated-1.0.gs

ADD --chown=$MAMBA_USER:$MAMBA_USER $GAMBIT_DB_GENOMES_URL $GAMBIT_DB_PATH/
ADD --chown=$MAMBA_USER:$MAMBA_USER $GAMBIT_DB_SIGNATURES_URL $GAMBIT_DB_PATH/


# Run test
FROM app as test

COPY test.sh .
RUN bash test.sh

