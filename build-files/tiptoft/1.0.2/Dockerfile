ARG TIPTOFT_VER="1.0.2"

# The base image being python 3.6 is important. 
# There are some issues with longintrepr.h, which homopolymer_compression.c references in more recent versions of python.
FROM python:3.6-slim AS builder
ARG TIPTOFT_VER

# Provides C compiler for installing cython.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Store packages in /opt/venv for lighter app stage.
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installed dependencies for tiptoft
RUN pip install --no-cache-dir \
    cython \
    "biopython>=1.68" \
    "pyfastaq>=3.12.0" 

# Modifications done to RefGenesGetter.py of tiptoft. Tiptoft uses plasmidfinder in its database updater.
# https://bitbucket.org/genomicepidemiology/plasmidfinder_db/src/master/
# Enterobacteriaceae is renamed to enterobacteriales in the URL fileserver above.
RUN wget https://github.com/andrewjpage/tiptoft/archive/refs/tags/v${TIPTOFT_VER}.tar.gz && \
    tar -xzf v${TIPTOFT_VER}.tar.gz && \
    cd tiptoft-${TIPTOFT_VER} && \
    sed -i 's/enterobacteriaceae/enterobacteriales/g' tiptoft/RefGenesGetter.py && \
    pip install --no-cache-dir . && \
    cd .. && \
    rm -rf v${TIPTOFT_VER}.tar.gz tiptoft-${TIPTOFT_VER}
  

FROM python:3.6-slim AS app
ARG TIPTOFT_VER

LABEL base.image="python:3.6-slim"
LABEL dockerfile.version="1"
LABEL software="tiptoft"
LABEL software.version="${TIPTOFT_VER}"
LABEL description="Predict plasmids from uncorrected long read data"
LABEL website="https://github.com/andrewjpage/tiptoft"
LABEL license="https://github.com/andrewjpage/tiptoft/blob/master/LICENSE"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"
LABEL maintainer3="Raheel Ahmed"
LABEL maintainer3.email="raheelsyedahmed@gmail.com"

# Copies over python packages from builder stage and adds venv to the path again.
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    LC_ALL=C

# Installing curl so that tiptoft_database_downloader works.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /data

CMD [ "tiptoft", "--help"]


FROM app AS test
ARG TIPTOFT_VER

WORKDIR /test

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN tiptoft --help && \
    tiptoft --version

# This will store a database in /test/tiptoftDB marked with the date it was downloaded 
# (docker image was built on this day)
# Tiptoft will use it's included DB by default, you must specify this DB with:
# -d /tiptoftDB/tiptoftDB-downloaded-on-$(date +%Y-%m-%d) if you want to use it.
RUN mkdir /test/tiptoftDB && \
    cd /test/tiptoftDB && \
    DB_DATE=$(date +%Y-%m-%d) && \
    tiptoft_database_downloader tiptoftDB-downloaded-on-${DB_DATE} && \
    wget -q https://github.com/andrewjpage/tiptoft/raw/refs/heads/master/example_data/ERS654932_plasmids.fastq.gz && \
    tiptoft -d /test/tiptoftDB/tiptoftDB-downloaded-on-${DB_DATE}.fa ERS654932_plasmids.fastq.gz