ARG FREYJA_SOFTWARE_VERSION="2.0.5"

FROM mambaorg/micromamba:2.9.0-ubuntu22.04 AS app

# Version arguments
# ARG variables only persist during build time
ARG FREYJA_SOFTWARE_VERSION
ARG FREYJA_PATHOGEN="SARS-CoV-2"
ARG PANDAS_SOFTWARE_VERSION="2.3.3"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.9.0-ubuntu22.04"
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

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/freyja-env/bin:/opt/conda/envs/env/bin:${PATH}" \
    LC_ALL=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba create -n freyja-env -c conda-forge -c bioconda \
    freyja=${FREYJA_SOFTWARE_VERSION} \
    pandas=${PANDAS_SOFTWARE_VERSION} && \
    micromamba clean -a -y -f && \
    mkdir /data

# update barcodes
# NOTE: this will download the latest version of the `freyja/data/usher_barcodes.csv` file from GitHub
RUN freyja update --pathogen ${FREYJA_PATHOGEN}

# make directory editable
RUN chmod -R 777 /opt/conda/envs/freyja-env/lib/python*/site-packages/freyja/data

# set working directory to /data
WORKDIR /data

# default command is to pull up help options
CMD [ "freyja", "--help" ]

# new base for testing
FROM app AS test

ARG FREYJA_SOFTWARE_VERSION

RUN freyja --help && freyja --version

WORKDIR /test

# Grab test data from Freyja version 1.3.4
RUN wget -O /test/Freyja_WWSC2.bam https://github.com/StaPH-B/docker-builds/blob/master/build-files/freyja/1.3.4/tests/Freyja_WWSC2.bam?raw=true && \
    wget -P /test https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/freyja/1.3.4/tests/Freyja_depths.tsv && \
    wget -P /test https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/freyja/1.3.4/tests/Freyja_variants.tsv && \
    wget -P /test https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/freyja/1.3.4/tests/nCoV-2019.reference.fasta

# Run Freyja
RUN freyja variants /test/Freyja_WWSC2.bam --variants /test/test_variants.tsv --depths /test/test_depths.tsv --ref /test/nCoV-2019.reference.fasta && \
    freyja demix /test/test_variants.tsv /test/test_depths.tsv --output /test/test_demix.tsv

# Check validity of outputs
RUN head /test/test_variants.tsv && \
    head /test/test_depths.tsv && \
    head /test/test_demix.tsv && \
    grep "Omicron" /test/test_demix.tsv

# Using Freyja test data

WORKDIR /test_1

RUN wget https://github.com/andersen-lab/Freyja/archive/refs/tags/v${FREYJA_SOFTWARE_VERSION}.tar.gz && \
    tar -vxf v${FREYJA_SOFTWARE_VERSION}.tar.gz

RUN freyja plot Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/agg_outputs.tsv --output test_plot.pdf && \
    ls test_plot.pdf

RUN freyja dash Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/test_sweep.tsv \
                Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/sweep_metadata.csv \
                Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/title.txt \
                Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/introContent.txt \
                --lineageyml Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/lineages.yml \
                --output test_dash.html && \
    ls test_dash.html


RUN freyja get-lineage-def B.1.1.7 \
                  --annot Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/NC_045512_Hu-1.gff \
                  --ref Freyja-${FREYJA_SOFTWARE_VERSION}/freyja/data/NC_045512_Hu-1.fasta \
                  --output lineage_def.txt && \
    head lineage_def.txt


# print barcode version and freyja version
RUN freyja demix --version --pathogen ${FREYJA_PATHOGEN}

# get list of available organisms
RUN freyja update --help

# list installed deps
RUN micromamba list -n freyja-env
