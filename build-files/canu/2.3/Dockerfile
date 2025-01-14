# Use ubuntu as base image
FROM ubuntu:jammy AS app

ARG CANU_VERSION="2.3"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL software="Canu"
LABEL software.version="${CANU_VERSION}"
LABEL dockerfile.version="1"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/marbl/canu"
LABEL license="https://github.com/marbl/canu/blob/master/README.license.GPL"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# dependencies
# samtools version 1.13
# gnuplot version 5.4 patchlevel 2
RUN apt-get update && apt-get install -y --no-install-recommends \
   perl \
   samtools \
   default-jre \
   gnuplot \
#   libgcc-5-dev \
   libgomp1 \
#   maven \
#   git \
   wget \
   ca-certificates \
   xz-utils \
   minimap2 \
#   python3 \
#   build-essential \
#   cmake \
#   zlib1g-dev 
   && \
   apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
   mkdir /data

# install canu
RUN wget https://github.com/marbl/canu/releases/download/v${CANU_VERSION}/canu-${CANU_VERSION}.Linux-amd64.tar.xz && \
   tar -xvf canu-${CANU_VERSION}.Linux-amd64.tar.xz && \
   rm canu-${CANU_VERSION}.Linux-amd64.tar.xz

ENV PATH="/canu-${CANU_VERSION}/bin:${PATH}"

CMD ["canu", "-h"]

WORKDIR /data

# set perl locale settings
ENV LC_ALL=C

# ======== Adding a test layer ========

FROM app AS test

RUN canu -h

# creating test working DIR.  
WORKDIR /test_canu

# download test input file into /test_canu/ directory
RUN wget -q https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz

# testing analysis RUN, canu need to know approx genome size (for coverage calculation) and sequencing platform
RUN canu \
   -p portiera -d portiera-nanopore \
   genomeSize=0.3m \
   -nanopore ERR3772599.fastq.gz \
   maxMemory=7 maxThreads=2 \
   redMemory=7 redThreads=2 \
   corMemory=7 corThreads=2 \
   oeaMemory=7 oeaThreads=2 \
   batMemory=7 batThreads=2 \
   cnsMemory=7 cnsThreads=2 
