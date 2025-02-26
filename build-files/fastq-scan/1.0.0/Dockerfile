# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the following stage. We use `app` for the production image
FROM ubuntu:xenial as app

ARG FASTQSCAN_VER="1.0.0"

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="fastq-scan"
LABEL software.version=$FASTQSCAN_VER
LABEL description="Output FASTQ summary statistics in JSON format"
LABEL website="https://github.com/rpetit3/fastq-scan"
LABEL license="https://github.com/rpetit3/fastq-scan/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# install dependencies and cleanup
RUN apt-get update && apt-get install -y \
 g++ \
 make \
 jq \
 wget && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*


# install and/or setup more things. Make /data for use as a working dir
RUN wget https://github.com/rpetit3/fastq-scan/archive/refs/tags/v${FASTQSCAN_VER}.tar.gz && \
 tar -xzf v${FASTQSCAN_VER}.tar.gz && \
 rm v${FASTQSCAN_VER}.tar.gz && \
 mv fastq-scan-${FASTQSCAN_VER} /fastq-scan && \
 cd /fastq-scan && \
 make && \
 mkdir /data

# set environmental variables e.g. $PATH and locale settings for singularity compatibility
ENV PATH="/fastq-scan:$PATH" \
 LC_ALL=C

# set working directory
WORKDIR /data

FROM app as test

# The git repository used in the build has test files to run
RUN fastq-scan -h
RUN cat /fastq-scan/example.fq | fastq-scan -g 150000
