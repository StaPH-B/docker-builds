FROM ubuntu:jammy AS app

ARG PLASMIDFINDER_VER="2.1.6"
# There is a plasmidfinder database version (2.1), but that hasn't been updated in... awhile
# Instead, I think we should do what we do for the other *finder tools and use the latest commit
# see here: https://bitbucket.org/genomicepidemiology/plasmidfinder_db/commits/4add282963c788762cdc3c6e91eb46c3d109f19b
# commit date: 2024-11-14
ARG DB_COMMIT_HASH="4add282963c788762cdc3c6e91eb46c3d109f19b"

LABEL base.image="ubuntu:jammy"
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

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python3-biopython \
    python3-cgecore \
    python3-tabulate \
    python3-distutils \
    kma \
    ca-certificates \
    ncbi-blast+ &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install plasmidfinder
RUN wget -q https://bitbucket.org/genomicepidemiology/plasmidfinder/get/${PLASMIDFINDER_VER}.tar.gz && \
    tar -C /usr/local/bin/ --strip-components=1 --wildcards -xvf ${PLASMIDFINDER_VER}.tar.gz */plasmidfinder.py &&\
    rm ${PLASMIDFINDER_VER}.tar.gz
    
# download plasmindfinder database
RUN wget -q https://bitbucket.org/genomicepidemiology/plasmidfinder_db/get/${DB_COMMIT_HASH}.tar.gz &&\
    mkdir /database &&\
    tar -C /database --strip-components=1 -xvf ${DB_COMMIT_HASH}.tar.gz &&\
    rm ${DB_COMMIT_HASH}.tar.gz  &&\
    cd /database && python3 INSTALL.py kma_index

ENV LC_ALL=C

CMD ["plasmidfinder.py", "-h"]

WORKDIR /data

FROM app AS test

RUN plasmidfinder.py -h

RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz && \
    gzip -d ERR1937840.fastq.gz && mkdir test && \
    plasmidfinder.py -i ERR1937840.fastq -o test
