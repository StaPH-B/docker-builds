FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time
ARG SNVPHYL_VER="1.8.2"
ARG SAMTOOLSVER="1.9"

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SNVPhyl-tools"
LABEL software.version="1.8.2"
LABEL description="The SNVPhyl-tools are for a pipeline for identifying Single Nucleotide Variants (SNV) within a collection of microbial genomes and constructing a phylogenetic tree."
LABEL website="https://github.com/phac-nml/snvphyl-tools"
LABEL license="https://github.com/phac-nml/snvphyl-tools/blob/master/LICENSE"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="jvhagey@gmail.com"

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    pkg-config \
    curl \
    automake \
    autoconf \
    libncurses5-dev \
    build-essential \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev \
    libexpat1-dev \
    perl \
    wget && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# Install perl package dependencies
RUN yes | cpan App::cpanminus && \ 
    cpanm Test::Exception \
    Parallel::ForkManager@1.19 \
    Bio::Perl@1.007001 \
    Template@2.27 \
    Test::Deep \
    JSON@2.94 \
    JSON::Parse@0.49 \
    List::MoreUtils@0.419 \
    Hash::Merge@0.200 \
    String::Util@1.26 \
    Text::Diff@1.45 \
    Math::Round@0.07 \
    Text::CSV@1.95 \
    Bio::Phylo@0.58 

RUN wget https://github.com/phac-nml/snvphyl-tools/archive/refs/tags/${SNVPHYL_VER}.tar.gz && \
    tar -xvzf ${SNVPHYL_VER}.tar.gz && \
    rm ${SNVPHYL_VER}.tar.gz && \
    cd snvphyl-tools-${SNVPHYL_VER} && \
    ./install_deps.sh

# setting up the following environment variables
ENV BCFTOOLS_PLUGINS="/snvphyl-tools-${SNVPHYL_VER}/bcftools-1.9/plugins" \
    PERL5LIB="/snvphyl-tools-${SNVPHYL_VER}/lib/perl5"

# Build and install samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
    rm samtools-${SAMTOOLSVER}.tar.bz2 && \
    cd samtools-${SAMTOOLSVER} && \
    ./configure && \
    make && \
    make install

# Finish building and installing vcftools
RUN cd /snvphyl-tools-${SNVPHYL_VER}/vcftools-0.1.15 && \
    ./autogen.sh && \
    ./configure \
    make && \
    make install

# set perl locale settings
# Required by most tools that use perl with singularity so we can use container with both docker and singularity
ENV LC_ALL=C

# Add path to scripts
ENV PATH="${PATH}:/snvphyl-tools-${SNVPHYL_VER}/bcftools-1.9\
:/snvphyl-tools-${SNVPHYL_VER}/MUMmer3.23\
:/snvphyl-tools-${SNVPHYL_VER}\
:/snvphyl-tools-${SNVPHYL_VER}/bin\
:/samtools-${SAMTOOLSVER}\
:/snvphyl-tools-${SNVPHYL_VER}/vcftools-0.1.15\
:/snvphyl-tools-${SNVPHYL_VER}/htslib-1.9"

# Add references and entrypoint script
WORKDIR /data

# new base for testing
FROM app as test

#run test
RUN cd /snvphyl-tools-${SNVPHYL_VER} && \
    prove
