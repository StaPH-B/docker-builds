# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM --platform=linux/amd64 ubuntu:xenial as app

# ARG sets environment variables during the build stage
ARG PLASMIDSEEKER_VER="1.3"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="PlasmidSeeker"
LABEL software.version=$PLASMIDSEEKER_VER
LABEL description="A k-mer based program for the identification of known plasmids from bacterial whole genome sequencing reads."
LABEL website="https://github.com/bioinfo-ut/PlasmidSeeker"
LABEL license="https://github.com/bioinfo-ut/PlasmidSeeker/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update -y && apt-get install -y \
    apt-utils \
    wget \
    perl \
    unzip \
    jq \
    gzip \
    curl \
    libz-dev \
    r-base \
    r-base-dev&& \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Download git repository for PlasmidSeeker
RUN wget https://github.com/bioinfo-ut/PlasmidSeeker/archive/refs/tags/${PLASMIDSEEKER_VER}.tar.gz && \
    mkdir PlasmidSeeker && tar -xvf ${PLASMIDSEEKER_VER}.tar.gz -C PlasmidSeeker --strip-components 1 && \
    chmod 755 /PlasmidSeeker/plasmidseeker.pl && \
    chmod 755 /PlasmidSeeker/database_builder.pl && \
    chmod 755 /PlasmidSeeker/testfunction.R && \
    chmod 755 /PlasmidSeeker/make_mutations.pl && \
    sed -i '1 i #!/usr/bin/perl' /PlasmidSeeker/make_mutations.pl && \
    sed -i '1 i #!/usr/bin/perl' /PlasmidSeeker/database_builder.pl

ENV PATH="$PATH:/PlasmidSeeker"


# WORKDIR sets working directory
WORKDIR /data

##### NO DATABASE INCLUDED WITH THIS DOCKER IMAGE #####
## User will need to mount a directory from their host machine that contains latest PlasmidSeeker database files
## The latest release at the time of this docker file release is http://bioinfo.ut.ee/plasmidseeker/plasmidseeker_db_w20.tar.gz
## The database is around 12 GB when compressed
## This tool's git repository also provides a script and instructions for making your own.
## Here is example usage of mounting volumes when running container:
## docker run -v `pwd`:`pwd` -w `pwd` -i -t plasmidseeker/john plasmidseeker.pl  -d /Users/johnarnn/Documents/plasmidseekerdb/db_w20  -i /Users/johnarnn/Documents/plasmidseeker/ERR1937840.fastq -b /Users/johnarnn/Documents/plasmidseeker/e_coli_sakai_ref.fna  -o EC_1_results.txt
## Here are the links to the files needed along with the database:
## wget http://bioinfo.ut.ee/plasmidseeker/e_coli_sakai_ref.fna
## wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz

FROM app as test

COPY test.sh .
RUN bash test.sh
