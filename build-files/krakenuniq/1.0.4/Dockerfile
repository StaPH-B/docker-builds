ARG KRAKENUNIQ_VER="1.0.4"

FROM ubuntu:jammy as app

ARG KRAKENUNIQ_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="KrakenUniq"
LABEL software.version="${KRAKENUNIQ_VER}"
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/fbreitwieser/krakenuniq"
LABEL license="https://github.com/fbreitwieser/krakenuniq/blob/master/LICENSE.GPL-3.0"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y   \
    curl \
    perl \
    cpanminus \
    make \
    g++ \
    libbz2-dev \
    zlib1g-dev \
    ca-certificates \
    ncbi-blast+ \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# krakenuniq requires jellyfish v1.x.x
RUN curl -LJO https://github.com/gmarcais/Jellyfish/releases/download/v1.1.12/jellyfish-linux &&\
    mv jellyfish-linux /usr/local/bin/jellyfish &&\
    chmod u+x /usr/local/bin/jellyfish

# required perl libraries
RUN cpanm File::Copy LWP::Simple Getopt::Std

RUN curl -LJO https://github.com/fbreitwieser/krakenuniq/archive/refs/tags/v${KRAKENUNIQ_VER}.tar.gz && \
    tar -xvf krakenuniq-${KRAKENUNIQ_VER}.tar.gz && rm krakenuniq-${KRAKENUNIQ_VER}.tar.gz &&\
    cd krakenuniq-${KRAKENUNIQ_VER} && \
    ./install_krakenuniq.sh /usr/local/bin

ENV PATH=$PATH:/krakenuniq-${KRAKENUNIQ_VER}/scripts \
    LC_ALL=C

CMD krakenuniq --help

WORKDIR /data

## Test ##
FROM app as test

RUN krakenuniq --help && \
    krakenuniq-build --help && \
    krakenuniq-filter --help && \
    krakenuniq-mpa-report --help && \
    krakenuniq-report --help && \
    krakenuniq-translate --help

# doswload & build test database
RUN krakenuniq-download --dust --db DB refseq/archaea/Chromosome taxonomy &&\
    krakenuniq-build --db DB --threads 2 --kmer-len 21 --minimizer-len 12 --taxids-for-genomes --taxids-for-sequences --jellyfish-bin /usr/local/bin/jellyfish

# test kraken uniq with test db
RUN krakenuniq -db DB --report-file kuniq-report.txt ./DB/library/archaea/Chromosome/Thermococcus_aggregans_strain_TY-tax110163-GCF_024022995.1_ASM2402299v1_genomic-dustmasked.fna &&\
    head kuniq-report.txt