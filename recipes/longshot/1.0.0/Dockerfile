FROM mambaorg/micromamba:1.5.8 as app

# List all software versions are ARGs near the top of the dockerfile
# 'ARG' sets environment variables during the build stage
# 'ARG' variables are ONLY available during image build, they do not persist in the final image
ARG LONGSHOT_VERSION="1.0.0"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="longshot"
LABEL software.version="${LONGSHOT_VERSION}"
LABEL description="A variant calling tool for noisy reads"
LABEL website="https://github.com/pjedge/longshot"
LABEL license="https://github.com/pjedge/longshot/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# Example apt-get command for commonly-missing dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install your desired software into the base conda/micromamba environment, pinning the version
# clean up conda garbage
# make /data to use as a working directory
RUN micromamba install --name base -c conda-forge -c bioconda -c defaults longshot=${LONGSHOT_VERSION} && \
    micromamba clean -a -y && \
    mkdir /data

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# set the environment, add base conda/micromamba bin directory into path
# set locale settings to UTF-8
ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD longshot --help

# set final working directory to /data
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
# new base for testing
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN longshot --help && \
    longshot --version

RUN wget -q https://raw.githubusercontent.com/pjedge/longshot/master/example_data/genome.fa && \
    wget -q https://raw.githubusercontent.com/pjedge/longshot/master/example_data/genome.fa.fai && \
    wget -q https://raw.githubusercontent.com/pjedge/longshot/master/example_data/ground_truth_variants.vcf && \
    wget -q https://raw.githubusercontent.com/pjedge/longshot/master/example_data/pacbio_reads_30x.bam && \
    wget -q https://raw.githubusercontent.com/pjedge/longshot/master/example_data/pacbio_reads_30x.bam.bai && \
    longshot --bam pacbio_reads_30x.bam --ref genome.fa --out longshot_output.vcf && \
    head *vcf