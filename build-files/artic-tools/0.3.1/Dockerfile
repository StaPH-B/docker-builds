ARG ARTIC_TOOLS_VER="0.3.1"

FROM ubuntu:noble AS builder

ARG ARTIC_TOOLS_VER

# Installs certificate requirements, make and build essentials, and git
# An earlier version of gcc and g++ are installed to match the version of make the author used to compile the source code.
RUN apt-get update && apt-get -y install --no-install-recommends \
    ca-certificates \
    procps \
    cmake \
    build-essential \
    gcc-12 \
    g++-12 \
    libboost-dev \
    libboost-filesystem-dev \
    libcurl4-gnutls-dev \
    libhts-dev \
    zlib1g-dev \
    libbz2-dev \
    git && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 12

WORKDIR /opt

# Git is used to clone the appropriate version from GitHub. 
# I used this in lieu of downloading the source code since the source code does not have the submodules needed for make to build the binary.
# No binary was available at the time of building this version of artic-tools.
RUN git clone --recursive https://github.com/will-rowe/artic-tools.git /opt/artic-tools && \
    cd /opt/artic-tools && \
    git checkout v${ARTIC_TOOLS_VER} && \
    git submodule update --init --recursive && \
    mkdir ./build

# Steps to make the binary, now stored as /opt/artic-tools/bin/artic-tools
WORKDIR /opt/artic-tools
RUN cd build && \
    cmake .. && \
    make -j4 && \
    make test
    


FROM ubuntu:noble AS app

ARG ARTIC_TOOLS_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="artic-tools"
LABEL software.version="${ARTIC_TOOLS_VER}"
LABEL description="A set of tools for working with the ARTIC pipeline."
LABEL website="https://github.com/will-rowe/artic-tools"
LABEL license="https://github.com/will-rowe/artic-tools/blob/master/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

# Packages needed for artic-tools to pass proper installation checks.
# HTSlib, curlgnutls, and potentially a C++17 compiler are still needed even after building the binary.
RUN apt-get update && apt-get -y install --no-install-recommends \
    ca-certificates \
    libhts3 \
    libboost-filesystem1.83.0 \
    libcurl3-gnutls \
    libbz2-1.0 \
    zlib1g && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

# Copy the binary over from build stage
COPY --from=builder /opt/artic-tools/bin/artic-tools /usr/local/bin/artic-tools

ENV LC_ALL=C

RUN mkdir /data

WORKDIR /data

CMD ["artic-tools", "-h"]



FROM app AS test

WORKDIR /test

# Copy some test files over from build stage
COPY --from=builder /opt/artic-tools/tests/data/SCoV2.scheme.v3.bed /test/SCoV2.scheme.v3.bed
COPY --from=builder /opt/artic-tools/tests/data/CVR1.merged.vcf.gz /test/CVR1.merged.vcf.gz

# Help and version checks for both the binary and its subcommands
RUN artic-tools --help && \
    artic-tools --version
 
RUN artic-tools check_vcf --help && \
    artic-tools get_scheme --help && \
    artic-tools validate_scheme --help && \
    artic-tools align_trim --help

# Get scheme, validate scheme, and check_vcf commands.
RUN artic-tools get_scheme ebola

RUN artic-tools validate_scheme SCoV2.scheme.v3.bed

RUN artic-tools check_vcf -o summary.txt --vcfOut variants_passed.txt CVR1.merged.vcf.gz SCoV2.scheme.v3.bed
