ARG MYLOASM_VER="0.7.0"
ARG MYLOASM_KMC_VER="0.1.0"

FROM rust:1.85-slim-bookworm AS builder

ARG MYLOASM_KMC_VER

# Install C++ compiler (g++), zlib header files, and download utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    zlib1g-dev \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Download and extract the source release
WORKDIR /build
RUN wget https://github.com/bluenote-1577/myloasm-kmc/archive/refs/tags/v${MYLOASM_KMC_VER}.tar.gz && \
    tar -xzf v${MYLOASM_KMC_VER}.tar.gz

WORKDIR /build/myloasm-kmc-${MYLOASM_KMC_VER}

# Compile in release mode
RUN cargo build --release


FROM ubuntu:noble AS app
ARG MYLOASM_VER
ARG MYLOASM_KMC_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="myloasm"
LABEL software.version="${MYLOASM_VER}"
LABEL description="A de novo metagenome assembler for long-read sequencing data"
LABEL website="https://github.com/bluenote-1577/myloasm"
LABEL license="https://github.com/bluenote-1577/myloasm/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

# Copy the compiled binary from the builder stage
COPY --from=builder /build/myloasm-kmc-${MYLOASM_KMC_VER}/target/release/myloasm-kmc-v1 /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    zlib1g && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/bluenote-1577/myloasm/releases/download/v${MYLOASM_VER}/myloasm-${MYLOASM_VER}-x86_64-avx2 && \
    chmod +x myloasm-${MYLOASM_VER}-x86_64-avx2 && \
    mv ./myloasm-${MYLOASM_VER}-x86_64-avx2 /usr/local/bin/myloasm

ENV LC_ALL=C

WORKDIR /data

RUN myloasm --help

CMD [ "myloasm", "--help" ]


FROM app AS test
ARG MYLOASM_VER

WORKDIR /test

RUN myloasm --version && myloasm --help

RUN wget -q -O mmlong2_np.fastq.gz https://zenodo.org/records/12168493/files/mmlong2_np.fastq.gz?download=1 && \
    wget -q -O mmlong2_pb.fastq.gz https://zenodo.org/records/12168493/files/mmlong2_pb.fastq.gz?download=1

RUN myloasm mmlong2_np.fastq.gz -o np_test -t 4

RUN myloasm mmlong2_pb.fastq.gz -o pb_test -t 4 --hifi

RUN myloasm mmlong2_np.fastq.gz -o np_kmc_test -t 4 --kmc --kmc-ram 4
RUN myloasm mmlong2_pb.fastq.gz -o pb_kmc_test -t 4 --hifi --kmc --kmc-ram 4