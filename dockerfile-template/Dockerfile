# syntax=docker/dockerfile:1

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Thank you for using this Dockerfile template!                     #####
##### This is an outline for the flow of building a docker image.       #####
##### The docker image is built to the 'app' stage on dockerhub/quay.   #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 1. Set up the base image in the first stage.                 #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# 'FROM' defines where the Dockerfile is starting to build from.
# The 'as app' naming is required for the PR validation tests.
FROM ubuntu:jammy as app

# List all software versions as ARGs near the top of the dockerfile.
# ARG variables are ONLY available during image build.
ARG SOFTWARENAME_VER="1.0.0"

# 'LABEL' instructions tag the image with metadata. 
# NOTE: The "org.opencontainers" labels are REQUIRED to pass StaPH-B CI tests.

# Required Metadata Labels
# These follow the OCI Image Spec. They help users and automated systems 
# identify what is inside the container.
LABEL \
      # The date this image was last updated (Manually update this!)
      org.opencontainers.image.created="2024-05-20" \
      # The exact base image used for the 'app' stage (Must match the FROM instruction above)
      org.opencontainers.image.base.name="ubuntu:jammy" \
      # The name of the software (e.g., "BWA" or "Samtools")
      org.opencontainers.image.title="SoftwareName" \
      # The version of the software itself
      org.opencontainers.image.version="${SOFTWARENAME_VER}" \
      # The version of THIS Dockerfile (increment if you change the build logic)
      org.opencontainers.image.revision="1" \
      # A human-readable description of the tool
      org.opencontainers.image.description="A brief description of what this tool does" \
      # The project homepage or GitHub repository
      org.opencontainers.image.url="https://github.com/StaPH-B/docker-builds" \
      # Where users can find instructions or manuals for the software
      org.opencontainers.image.documentation="https://github.com/StaPH-B/docker-builds" \
      # Link to the source code used to build the image (which is often a GitHub url)
      org.opencontainers.image.source="https://github.com/StaPH-B/docker-builds" \
      # The software license (e.g., MIT, GPL-3.0, Apache-2.0) for the software
      org.opencontainers.image.licenses="GPL-3.0" \
      # The person/group maintaining this Dockerfile
      org.opencontainers.image.authors="firstName lastName <example@email.com>"

# 'RUN' executes code during the build.
# StaPH-B Requirement: You MUST install 'procps' and 'hostname' for Nextflow compatibility.
RUN apt-get update && apt-get install -y --no-install-recommends \
    dependency_a \
    dependency_b && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Setup Non-Root User
# Running as 'root' is a security risk. Your PR will fail if a user is not set.
RUN groupadd -r staphb && useradd -r -g staphb staphb

# Example: install ncbi-blast+ 2.9.0 pre-compiled linux binaries
ARG BLAST_VER=2.9.0
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
    rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz

# 'ENV' instructions set environment variables that persist into the resulting image.
ENV PATH="/ncbi-blast-${BLAST_VER}+/bin:$PATH" \
    LC_ALL=C

# 'WORKDIR' sets the default working directory. 
# StaPH-B Requirement: This MUST be set to /data.
WORKDIR /data

# Switch to the non-root user.
USER staphb

# 'CMD' instructions set a default command. This is typically 'tool --help.'
CMD [ "blastn", "-help" ]


##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM instruction creates a new stage for automated testing.
FROM app as test

# Set working directory so that all test inputs & outputs are kept in /test
# We switch back to root briefly if we need to install test-only tools, 
# but generally, we stay as the 'staphb' user.
WORKDIR /test

# Print help and version info to ensure the tool is in the PATH and executable.
RUN blastn -version

# Option 1: Run your own tests in a bash script and copy them:
# COPY my_tests.sh .
# RUN bash my_tests.sh

# Option 2: Write out usage cases directly:
# RUN wget <data_url> && blastn -query input.fasta ...
