
ARG PROKKA_VER="1.15.6"
ARG MINCED_VER="0.4.2"

FROM ubuntu:noble AS app

ARG PROKKA_VER
ARG MINCED_VER

LABEL base.image="mambaorg/micromamba:2.4.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Prokka"
LABEL software.version="${PROKKA_VER}"
LABEL description="Automated prokaryotic genome annotation tool"
LABEL website="https://github.com/tseemann/prokka"
LABEL license="https://github.com/tseemann/prokka#licence"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

ARG DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    perl \
    aragorn \
    barrnap \
    ncbi-blast+ \
    hmmer \
    infernal \
    parallel \
    bioperl \
    libbio-searchio-hmmer-perl \
    libxml-simple-perl \
    prodigal \
    ncbi-tools-bin \
    default-jre-headless \
    dpkg-dev \
    gcc

# ncbi-tools-bin provides table2asn
# dpkg-dev and gcc is for suppressing a warning (may be removed)

# install minced
RUN wget https://github.com/ctSkennerton/minced/releases/download/${MINCED_VER}/minced \
    https://github.com/ctSkennerton/minced/releases/download/${MINCED_VER}/minced.jar &&\
    chmod +x minced* &&\ 
    mv minced* /usr/local/bin/

# install prokka
RUN wget https://github.com/tseemann/prokka/archive/refs/tags/v${PROKKA_VER}.tar.gz &&\
    tar -xvf v${PROKKA_VER}.tar.gz && rm v${PROKKA_VER}.tar.gz

ENV PATH=$PATH:/prokka-${PROKKA_VER}/bin \
    LC_ALL=C

# index database
RUN prokka --setupdb

CMD ["prokka", "--help"]

WORKDIR /data

## Test ##
FROM app AS test

ARG PROKKA_VER

RUN prokka --listdb &&\
    prokka --version &&\
    blastp -help &&\
    barrnap --help 2>&1 | grep Options &&\
    prodigal -h &&\
    tbl2asn --help

RUN prokka /prokka-${PROKKA_VER}/test genome.fna