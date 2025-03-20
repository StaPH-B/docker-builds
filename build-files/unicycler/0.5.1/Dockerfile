ARG unicyclerVer="0.5.1"
ARG blastVer="2.16.0"
ARG raconVer="1.5.0"
ARG spadesVer="4.1.0"

FROM ubuntu:jammy AS builder

ARG raconVer
ARG unicyclerVer

RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    default-jre \
    gnuplot \
    libgomp1 \
    maven \
    git \
    wget \
    python3 \
    python3-distutils \
    python3-pip \
    build-essential \
    cmake \
    zlib1g-dev \
    curl \
    bzip2 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install Racon
RUN wget -q https://github.com/lbcb-sci/racon/archive/refs/tags/${raconVer}.tar.gz && \
    tar -xvf ${raconVer}.tar.gz && \
    cd racon-${raconVer} && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release .. && \
    make

# Install Unicycler
RUN wget -q https://github.com/rrwick/Unicycler/archive/v${unicyclerVer}.tar.gz && \
    tar -xvf v${unicyclerVer}.tar.gz && \
    ls && \
    cd Unicycler-${unicyclerVer} && \
    python3 setup.py install

FROM ubuntu:jammy AS app

ARG unicyclerVer
ARG blastVer
ARG spadesVer
ARG raconVer

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Unicycler"
LABEL software.version="${unicyclerVer}"
LABEL description="Unicycler is an assembly pipeline for bacterial genomes."
LABEL website="https://github.com/rrwick/Unicycler"
LABEL license="https://github.com/rrwick/Unicycler/blob/main/LICENSE"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 \
    wget \
    libgomp1 \
    libz-dev \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /racon-${raconVer}/build/bin/* /usr/local/bin/
COPY --from=builder /usr/local/bin/* /usr/local/bin/
COPY --from=builder /usr/lib /usr/lib
COPY --from=builder /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages

# install SPAdes binary
RUN wget -q https://github.com/ablab/spades/releases/download/v${spadesVer}/SPAdes-${spadesVer}-Linux.tar.gz && \
    tar -xzf SPAdes-${spadesVer}-Linux.tar.gz && \
    rm -v SPAdes-${spadesVer}-Linux.tar.gz

RUN wget -q https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
    tar -xzf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
    rm ncbi-blast-${blastVer}+-x64-linux.tar.gz

# LC_ALL for singularity compatibility
# TERM set so that output is pretty during tests - also ensures unicycler unit tests pass 
ENV PATH="/SPAdes-${spadesVer}-Linux/bin:/ncbi-blast-${blastVer}+/bin/:${PATH}" \
    LC_ALL=C.UTF-8 \
    TERM=xterm-256color

CMD ["unicycler", "help"]


# final working directory in app layer is /data, as usual
WORKDIR /data

FROM app AS test

COPY --from=builder /Unicycler-${unicyclerVer} /unicycler

RUN unicycler --version && \
    unicycler --help

# testing on the test data (ILMN and ONT) provided with unicycler code
RUN unicycler -1 /unicycler/sample_data/short_reads_1.fastq.gz \
    -2 /unicycler/sample_data/short_reads_2.fastq.gz \
    -l /unicycler/sample_data/long_reads_high_depth.fastq.gz \
    --out sample_data_hybrid_asm_test && \
    head sample_data_hybrid_asm_test/assembly.fasta
