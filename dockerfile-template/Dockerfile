##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Thank you for using this Dockerfile template!                     #####
##### This is an outline for the flow of building a docker image.       #####
##### The docker image is built to the 'app' stage on dockerhub/quay.   #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 1. Set up the base image in the first stage.                 #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# 'FROM' defines where the Dockerfile is starting to build from. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. The production image uses everything to the 'app' stage.

FROM ubuntu:jammy as app

# List all software versions are ARGs near the top of the dockerfile
# 'ARG' sets environment variables during the build stage
# ARG variables are ONLY available during image build, they do not persist in the final image
ARG SOFTWARENAME_VER="1.0.0"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SoftwareName"
LABEL software.version="${SOFTWARENAME_VER}"
LABEL description="This software does X, Y, AND Z!"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"
LABEL maintainer="FirstName LastName"
LABEL maintainer.email="my.email@email.com"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
 dependency_a \
 dependency_b \
 dependency_c && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install and/or setup more things. Make /data for use as a working dir
# For readability, limit one install per 'RUN' statement.

# Example: install ncbi-blast+ 2.9.0 pre-compiled linux binaries
ARG BLAST_VER=2.9.0

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 mkdir /data

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="/software-${SOFTWARENAME_VER}/bin:$PATH" \
 LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "tool", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN softwarename --help && \
 softwarename --check && \
 softwarename --version

# Demonstrate that the program is successfully installed - which is highly dependant on what the tool is.

# Run the program's internal tests if available, for example with SPAdes:
RUN spades.py --test

# Option 1: write your own tests in a bash script in the same directory as your Dockerfile and copy them:
COPY my_tests.sh .
RUN bash my_tests.sh

# Option 2: write below common usage cases, for example with tb-profiler:
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_2.fastq.gz && \
    tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 4 -p ERR1664619 --txt
