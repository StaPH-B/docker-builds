ARG DSK_VER="2.3.3"

FROM ubuntu:jammy as app
ARG DSK_VER
ARG GATBCORE_VER="1.4.2"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="DSK"
LABEL software.version=${DSK_VER}
LABEL description="DSK is a k-mer counter for reads or genomes."
LABEL website="https://github.com/GATB/dsk"
LABEL documentation="https://gatb.inria.fr/software/dsk/"
LABEL license="https://github.com/GATB/dsk/blob/master/LICENSE"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends\
    build-essential \
    cmake \
    wget \
    libz-dev \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Download DSK source code
RUN wget -q https://github.com/GATB/dsk/archive/refs/tags/v${DSK_VER}.tar.gz && \
    tar -xzf v${DSK_VER}.tar.gz && \
    rm v${DSK_VER}.tar.gz && \
    cd /dsk-${DSK_VER}/thirdparty && \
    # Install GATB dependency where DSK expects it
    wget -q https://github.com/GATB/gatb-core/archive/refs/tags/v${GATBCORE_VER}.tar.gz && \
    tar -xzf v${GATBCORE_VER}.tar.gz && \
    rm v${GATBCORE_VER}.tar.gz && \
    rm -rf gatb-core && mv gatb-core-${GATBCORE_VER} gatb-core && \
    cd /dsk-${DSK_VER} && \
    sh INSTALL

# Add DSK executable to PATH
ENV PATH="/dsk-${DSK_VER}/build/bin:$PATH"

CMD dsk

WORKDIR /data

FROM app as test
ARG DSK_VER

RUN dsk

# Run DSK's internal tests
WORKDIR /dsk-${DSK_VER}/scripts
RUN ./simple_test.sh
