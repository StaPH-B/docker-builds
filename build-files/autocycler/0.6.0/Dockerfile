

FROM ubuntu:jammy AS app

ARG AUTOCYCLER_VER="0.6.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Autocycler"
LABEL software.version="${AUTOCYCLER_VER}"
LABEL description="generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Autocycler"
LABEL license="https://github.com/rrwick/Autocycler/blob/main/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates
    

WORKDIR /usr/local/bin

# install autocycler and helper scripts
RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz

RUN tar -vxf autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz

RUN rm autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz

# Removed this section of installations since helper scripts are not available for this release.
# See: https://github.com/rrwick/Autocycler/releases/tag/v0.6.0

# RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz
# RUN tar -vxf autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz
# RUN rm autocycler-helper-scripts-v${AUTOCYCLER_VER}.tar.gz

ENV PATH=$PATH LC_ALL=C

CMD [ "autocycler", "--help" ]

WORKDIR /data



FROM app AS test

ARG AUTOCYCLER_VER

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

# demo dataset does not change with version
RUN wget -q https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -vxf autocycler-demo-dataset.tar && \
    autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --genome_size "242000"