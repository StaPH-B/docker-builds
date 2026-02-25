FROM staphb/kma:1.6.4 AS kma

FROM ubuntu:noble AS app

ARG PLASMIDFINDER_VER="3.0.2"
# Sometimes does not get a proper version
# If a commit does not have a verion, I think we should do what we do for the other *finder tools and use the latest commit
# see here: https://bitbucket.org/genomicepidemiology/plasmidfinder_db/commits/4add282963c788762cdc3c6e91eb46c3d109f19b
# commit date: 2025-09-10
ARG DB_COMMIT_HASH="2.2.0"

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
RUN wget https://bitbucket.org/genomicepidemiology/plasmidfinder_db/get/${DB_COMMIT_HASH}.tar.gz &&\
    mkdir /database &&\
    tar -C /database --strip-components=1 -xvf ${DB_COMMIT_HASH}.tar.gz &&\
    rm ${DB_COMMIT_HASH}.tar.gz  &&\
    cd /database && python3 INSTALL.py kma_index

# install plasmidfinder to specific tag/version; make /data
RUN pip3 install --no-cache-dir PlasmidFinder==${PLASMIDFINDER_VER} && \
    mkdir /data

# set $PATH and locale settings for singularity compatibility
ENV PATH="${PATH}" \
    LC_ALL=C.UTF-8 \
    CGE_BLASTN=/usr/bin/blastn \
    CGE_PLASMIDFINDER_DB=/database \
    PLASMID_DB=/database

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
