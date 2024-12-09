FROM ubuntu:xenial

ARG FASTQSCAN_VER="0.4.3"

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="fastq-scan"
LABEL software.version="0.4.3"
LABEL description="Output FASTQ summary statistics in JSON format"
LABEL website="https://github.com/rpetit3/fastq-scan"
LABEL license="https://github.com/rpetit3/fastq-scan/blob/master/LICENSE"
LABEL maintainer="Robert A. Petit III"
LABEL maintainer.email="robert.petit@wyo.gov"

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

#### Example commands ####

## Example stats for a uncompressed FASTQ
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastq-scan:0.4.3 \
#   /bin/bash -c "cat /fastq-scan/example.fq | fastq-scan"

## Example stats for a compressed (gzip) FASTQ
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastq-scan:0.4.3 \
#   /bin/bash -c "zcat /data/SRX0000000_R1.fastq.gz | fastq-scan"

## Eaxmple using jq to extract the total number of reads in the FASTQ
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data fastq-scan:0.4.3 \
#   /bin/bash -c "cat /fastq-scan/example.fq | fastq-scan | jq .qc_stats.read_total"

## View full fastq-scan help options
# $ docker run --rm -u $(id -u):$(id -g) -v ${PWD}:/data staphb/fastq-scan:0.4.3 fastq-scan -h
