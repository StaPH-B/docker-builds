# Set global variables
ARG CAT_VER="5.3"
ARG DIAMOND_VER="2.1.9"

# Build Stage
FROM ubuntu:focal AS builder
ARG CAT_VER
ARG DIAMOND_VER

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget unzip less automake cmake zlib1g-dev libzstd-dev \
    python3 python3-pip git prodigal build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

# Install Python dependencies
RUN pip install --no-cache-dir certifi biopython

# Clone CAT and set permissions
RUN wget https://github.com/MGXlab/CAT_pack/archive/refs/tags/v${CAT_VER}.tar.gz && \
    tar -xvzf v${CAT_VER}.tar.gz && \
    chmod +x CAT_pack-${CAT_VER}/CAT_pack/CAT && \
    rm v${CAT_VER}.tar.gz


# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v${DIAMOND_VER}.tar.gz && \
    tar -xzf v${DIAMOND_VER}.tar.gz && \
    cd diamond-${DIAMOND_VER} && mkdir bin && cd bin && \
    cmake .. && make -j$(nproc) && make install && \
    cd ../../ && rm -rf diamond-${DIAMOND_VER}*

# Application Stage
FROM ubuntu:focal AS app
ARG CAT_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CAT"
LABEL software.version=${CAT_VER}
LABEL description="CAT: a tool for taxonomic classification of contigs and metagenome-assembled genomes (MAGs)."
LABEL website="https://github.com/dutilh/CAT"
LABEL license.url="https://github.com/dutilh/CAT/blob/master/LICENSE.md"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

# Copy necessary files from the builder stage
COPY --from=builder /CAT_pack-${CAT_VER}/ /CAT/
COPY --from=builder /usr/ /usr/

# Add CAT to PATH
ENV PATH="${PATH}:/CAT/CAT_pack"

CMD CAT --help
WORKDIR /data

# Optional stage: Test data
FROM app AS test

WORKDIR /data/test

RUN wget -nv --no-check-certificate \
    https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa \
    -O burk_wgs_pos_ctrl.fa &&\
    wget -nv --no-check-certificate \
    https://merenlab.org/data/refining-mags/files/GN02_MAG_IV_B_1-contigs.fa \
    -O GN02_MAG_IV_B_1-contigs.fa

# Prepare testing database
RUN mkdir -p db_tests && \
    gzip -d /CAT/tests/data/prepare/small.fa.gz && \
    CAT prepare --db_fasta /CAT/tests/data/prepare/small.fa \
    --acc2tax /CAT/tests/data/prepare/prot2acc.txt \
    --names /CAT/tests/data/prepare/names.dmp \
    --nodes /CAT/tests/data/prepare/nodes.dmp \
    --db_dir db_tests/

# Running CAT on contigs
RUN CAT contigs -c burk_wgs_pos_ctrl.fa \
    -d db_tests/db \
    -t db_tests/tax

# Running BAT on a set of MAGs
RUN CAT bins -b GN02_MAG_IV_B_1-contigs.fa \
    -d db_tests/db \
    -t db_tests/tax

WORKDIR /data
