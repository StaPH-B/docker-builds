ARG GAMBIT_DB_BASE_URL=https://storage.googleapis.com/jlumpe-gambit/public/databases/refseq-curated/1.0
ARG GAMBIT_DB_GENOMES_URL=$GAMBIT_DB_BASE_URL/gambit-refseq-curated-1.0.gdb
ARG GAMBIT_DB_SIGNATURES_URL=$GAMBIT_DB_BASE_URL/gambit-refseq-curated-1.0.gs
ARG GAMBIT_SOFTWARE_VERSION="1.1.0"
ARG GAMBIT_GIT_TAG=v${GAMBIT_SOFTWARE_VERSION}
ARG GAMBIT_SRC_URL=https://github.com/jlumpe/gambit/archive/refs/tags/${GAMBIT_GIT_TAG}.tar.gz

# Builder stage: compiles GAMBIT from source. This stage is discarded after the build
# so compiler tools (c-compiler, cython) never make it into the final image.
FROM mambaorg/micromamba:2.5.0 AS builder
ARG GAMBIT_SRC_URL

# Install the full conda environment (including build-only deps like c-compiler and cython)
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Create the install directory where the compiled GAMBIT package will be placed,
# then copy it into the runtime image via COPY --from=builder
USER root
RUN mkdir /install && chown $MAMBA_USER:$MAMBA_USER /install
USER $MAMBA_USER

# Compile and install GAMBIT into /install (isolated from the conda environment)
RUN pip install --no-cache-dir --prefix=/install ${GAMBIT_SRC_URL}

#runtime base (no compiler tools)
FROM mambaorg/micromamba:2.5.0 AS app_base
ARG GAMBIT_SOFTWARE_VERSION

#Environment
ENV GAMBIT_DB_PATH=/gambit-db
ENV LC_ALL=C.UTF-8
ENV PATH="/opt/conda/bin:${PATH}"

# Install mamba environment
COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes
ARG MAMBA_DOCKERFILE_ACTIVATE=1


# Copy only the built package from the builder stage — no compiler needed
COPY --from=builder /install /opt/conda

USER root
RUN mkdir $GAMBIT_DB_PATH /data && \
    chown $MAMBA_USER:$MAMBA_USER $GAMBIT_DB_PATH /data
USER $MAMBA_USER
WORKDIR /data

# With database files added
FROM app_base AS app
ARG GAMBIT_DB_BASE_URL
ARG GAMBIT_DB_GENOMES_URL
ARG GAMBIT_DB_SIGNATURES_URL
ARG GAMBIT_SOFTWARE_VERSION
#ARG GAMBIT_GIT_TAG
#ARG GAMBIT_SRC_URL

LABEL base.image="mambaorg/micromamba:2.5.0"
LABEL dockerfile.version="1"
LABEL software="GAMBIT"
LABEL software.version=${GAMBIT_SOFTWARE_VERSION}
LABEL description="Rapid genomic-distance comparison for taxonomic identification of microbial pathogens"
LABEL website="https://github.com/jlumpe/gambit"
LABEL license="https://github.com/jlumpe/gambit/blob/master/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@theiagen.com"
LABEL maintainer2="Michelle Scribner"
LABEL maintainer2.email="michelle.scribner@theiagen.com"
LABEL maintainer3="Jared Lumpe"
LABEL maintainer3.email="jared@jaredlumpe.com"

# Install ps (procps) required for Nextflow workflows
USER root
RUN apt-get update && apt-get install -y --no-install-recommends procps && \
    rm -rf /var/lib/apt/lists/*
USER $MAMBA_USER

ADD --chown=$MAMBA_USER:$MAMBA_USER $GAMBIT_DB_GENOMES_URL $GAMBIT_DB_PATH/
ADD --chown=$MAMBA_USER:$MAMBA_USER $GAMBIT_DB_SIGNATURES_URL $GAMBIT_DB_PATH/

WORKDIR /data
CMD ["gambit", "--help"]

# Run test
FROM app AS test
COPY test.sh .
RUN bash test.sh
