FROM ubuntu:jammy as app

# List all software versions are ARGs near the top of the dockerfile
ARG SHIGAPASS_VER=1.5.0
ARG BLAST_VER=2.12.0

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="ShigaPass"
LABEL software.version="${SHIGAPASS_VER}"
LABEL description="In silico tool used to predict Shigella serotypes and to differentiate between Shigella, EIEC (Enteroinvasive E. coli), and non Shigella/EIEC using assembled whole genomes."
LABEL website="https://github.com/imanyass/ShigaPass/"
LABEL license="https://github.com/imanyass/ShigaPass/blob/main/LICENSE"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="qpk9@cdc.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  ca-certificates \
  git \
  libgomp1 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install ncbi-blast+ 2.12.0 pre-compiled linux binaries
ARG BLAST_VER=2.12.0

#creating variable for referencing database
ENV DB_PATH=/ShigaPass-${SHIGAPASS_VER}/SCRIPT/ShigaPass_DataBases/

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz 
 
# install Shigapass
RUN wget https://github.com/imanyass/ShigaPass/archive/refs/tags/v${SHIGAPASS_VER}.tar.gz && \
    tar -xzf v${SHIGAPASS_VER}.tar.gz && \
    rm -r v${SHIGAPASS_VER}.tar.gz && \
    chmod +x /ShigaPass-${SHIGAPASS_VER}/SCRIPT/ShigaPass.sh && \
    chmod -R a+rw ${DB_PATH} && \
    mkdir /data

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="/ncbi-blast-${BLAST_VER}+/bin/:/ShigaPass-${SHIGAPASS_VER}/SCRIPT:$PATH" \
 LC_ALL=C

#creating variable for referencing database
ENV DB_PATH=/ShigaPass-${SHIGAPASS_VER}/SCRIPT/ShigaPass_DataBases/

# running test to index the database
RUN gunzip /ShigaPass-${SHIGAPASS_VER}/Example/Input/*.gz && \
sed -i "s/^/\/ShigaPass-${SHIGAPASS_VER}\//" /ShigaPass-${SHIGAPASS_VER}/Example/Input/ShigaPass_test.txt && \
ShigaPass.sh -l /ShigaPass-${SHIGAPASS_VER}/Example/Input/ShigaPass_test.txt -o ShigaPass_Results -p ${DB_PATH} -u

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "ShigaPass.sh" ]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

## print help and version info to ensure ShigaPass is in path and is executable
RUN ShigaPass.sh -h && \
 ShigaPass.sh -v

# Testing a script - need to unzip the test files and correct the path for the container
RUN ShigaPass.sh -l /ShigaPass-${SHIGAPASS_VER}/Example/Input/ShigaPass_test.txt -o ShigaPass_Results -p ${DB_PATH}