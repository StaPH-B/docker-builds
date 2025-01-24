FROM mambaorg/micromamba:1.5.8 AS app

# Version arguments
# ARG variables only persist during build time
ARG FREYJA_SOFTWARE_VERSION="1.5.2"
ARG IVAR_VER="1.4.3"
ARG SAMTOOLS_VER="1.21"
ARG USHER_VER="0.6.3"


# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.8"
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
    procps \
    git && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Create Freyja conda environment called freyja-env from bioconda recipe
# clean up conda garbage
RUN micromamba create -n freyja-env -c conda-forge -c bioconda -c defaults \
    ivar=${IVAR_VER} \
    usher=${USHER_VER} \
    samtools=${SAMTOOLS_VER} \
    pip \
    biopython \
    click \
    cvxpy \
    epiweeks \
    joblib \
    matplotlib-base \
    numpy \
    pandas \
    plotly \
    pyarrow \
    pysam \
    pyyaml \
    requests \
    seaborn \
    tqdm && \
    micromamba clean -a -y -f 

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/freyja-env/bin:/opt/conda/envs/env/bin:${PATH}" \
    LC_ALL=C.UTF-8

RUN wget -q https://github.com/andersen-lab/Freyja/archive/refs/tags/v${FREYJA_SOFTWARE_VERSION}.tar.gz && \
    pip install --no-cache-dir v${FREYJA_SOFTWARE_VERSION}.tar.gz && \
    rm v${FREYJA_SOFTWARE_VERSION}.tar.gz


# update barcodes
# NOTE: this will download the latest version of the `freyja/data/usher_barcodes.csv` file from GitHub
RUN freyja update

# set working directory to /data
WORKDIR /data

# default command is to pull up help options
CMD [ "freyja", "--help" ]

# new base for testing
FROM app AS test

RUN freyja --help && freyja --version

# Grab test data from Freyja version 1.3.4
RUN wget -O /data/Freyja_WWSC2.bam https://github.com/StaPH-B/docker-builds/blob/master/build-files/freyja/1.3.4/tests/Freyja_WWSC2.bam?raw=true && \
    wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/freyja/1.3.4/tests/Freyja_depths.tsv && \
    wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/freyja/1.3.4/tests/Freyja_variants.tsv && \
    wget -P /data https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/freyja/1.3.4/tests/nCoV-2019.reference.fasta

# Run Freyja
RUN freyja variants /data/Freyja_WWSC2.bam --variants /data/test_variants.tsv --depths /data/test_depths.tsv --ref /data/nCoV-2019.reference.fasta && \
    freyja demix /data/test_variants.tsv /data/test_depths.tsv --output /data/test_demix.tsv

# Check validity of outputs
RUN head /data/test_variants.tsv && \
    head /data/test_depths.tsv && \
    head /data/test_demix.tsv && \
    grep "Omicron" /data/test_demix.tsv

# print barcode version and freyja version
RUN freyja demix --version
