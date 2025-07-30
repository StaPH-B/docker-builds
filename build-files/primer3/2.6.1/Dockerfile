ARG PRIMER3_VERSION="2.6.1"

FROM ubuntu:jammy AS builder

ARG PRIMER3_VERSION

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    unzip \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Build Primer3 from source
RUN wget https://github.com/primer3-org/primer3/archive/refs/tags/v${PRIMER3_VERSION}.tar.gz && \
    tar -xzf v${PRIMER3_VERSION}.tar.gz && \
    rm v${PRIMER3_VERSION}.tar.gz && \
    cd /primer3-${PRIMER3_VERSION}/src && \
    make && \
    make test && \
    cp primer3_core ntdpal oligotm long_seq_tm_test /usr/local/bin/ && \
    mkdir -p /usr/local/share/primer3_config && \
    cp -r primer3_config/* /usr/local/share/primer3_config/

FROM ubuntu:jammy AS app

ARG PRIMER3_VERSION

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Primer3"
LABEL software.version=$PRIMER3_VERSION
LABEL description="Primer3 is a widely used open-source tool for designing PCR primers."
LABEL website="https://github.com/primer3-org/primer3"
LABEL license="https://github.com/primer3-org/primer3/blob/main/LICENSE"
LABEL maintainer="Rong Jin"
LABEL maintainer.email="jinrongshanghai@gmail.com"

COPY --from=builder /usr/local/bin/* /usr/local/bin/
COPY --from=builder /usr/local/share/primer3_config/* /usr/local/share/primer3_config/

# Set environment variables
ENV PRIMER3_CONFIG=/usr/local/share/primer3_config \
    PATH="$PATH" \
    LC_ALL=C

# Default command
CMD ["primer3_core"]

# Working directory
WORKDIR /data

FROM app AS test

WORKDIR /test

RUN primer3_core || echo "This prints to stderr"
RUN ntdpal || echo "This prints to stderr"
RUN oligotm  || echo "This prints to stderr"

# test for primer3_core
RUN echo -e "=SEQUENCE_ID=Test\nSEQUENCE_TEMPLATE=ATCGATCGATCG\nPRIMER_TASK=generic\nPRIMER_THERMODYNAMIC_PARAMETERS_PATH=${PRIMER3_CONFIG}/\n=" > test_input.txt && \
    primer3_core test_input.txt

# test for ntdpal
RUN ntdpal ACGTACGTACGT ACGTACGTACGT g

# test for oligotm
RUN oligotm AGCTAGCTAGCT && oligotm -mv 50 -dv 1.5 -n 0.6 -d 50 -tp 1 -sc 1 AGCTAGCTAGCT && oligotm -dm 10 AGCTAGCTAGCT
