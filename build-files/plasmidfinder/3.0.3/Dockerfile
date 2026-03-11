FROM staphb/kma:1.6.4 AS kma

FROM ubuntu:noble AS app

# set env to avoid /.gitconfig permission error on AWS
ENV HOME=/root

ARG PLASMIDFINDER_VER="3.0.3"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="plasmidfinder"
LABEL software.version="${PLASMIDFINDER_VER}"
LABEL description="Identifies plasmids in total or partial sequenced isolates of bacteria."
LABEL website="https://bitbucket.org/genomicepidemiology/plasmidfinder"
LABEL license="https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/README.md"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluinct@gmail.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# install dependencies; cleanup apt garbage 
# ncbi-blast+ v2.12.0 (ubuntu:jammy), min required version is 2.8.1
# python3 v3.10.12, min required version is 3.10
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    ncbi-blast+ \
    python3-pip \
    git \
    python-is-python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 10

COPY --from=kma /usr/local/bin/*    /usr/local/bin/
    
# download plasmindfinder database
RUN git clone -b plasmidfinder-${PLASMIDFINDER_VER} --depth 1 https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git &&\
    cd plasmidfinder_db &&\
    python INSTALL.py &&\
    rm -rf .git

# install plasmidfinder to specific tag/version; make /data
RUN pip3 install --no-cache-dir --break-system-packages PlasmidFinder==${PLASMIDFINDER_VER} && \
    mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="${PATH}" \
    LC_ALL=C.UTF-8 \
    CGE_BLASTN=/usr/bin/blastn \
    CGE_PLASMIDFINDER_DB=/plasmidfinder_db \
    PLASMID_DB=/plasmidfinder_db

# set final working directory for production docker image (app layer only)
WORKDIR /data

# default command is to pull up help options for virulencefinder
CMD ["python", "-m", "plasmidfinder", "-h"]

### START OF TEST STAGE ###
FROM app AS test

RUN python -m plasmidfinder -h

RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz && \
    gzip -d ERR1937840.fastq.gz && mkdir test && \
    python -m plasmidfinder -i ERR1937840.fastq -o test
