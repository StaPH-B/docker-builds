ARG SEQTK_VER="1.4"

FROM ubuntu:jammy as builder

ARG SEQTK_VER

# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    make \
    wget \
    gcc \
    zlib1g-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/lh3/seqtk/archive/v${SEQTK_VER}.tar.gz && \
    tar -xzvf v${SEQTK_VER}.tar.gz && \
    rm v${SEQTK_VER}.tar.gz && \
    cd seqtk-${SEQTK_VER} && \
    make && \
    cp seqtk /usr/local/bin/.

FROM ubuntu:jammy as app

ARG SEQTK_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="seqtk"
LABEL software.version="${SEQTK_VER}"
LABEL description="Toolkit for processing sequences in FASTA/Q formats"
LABEL website="https://github.com/lh3/seqtk"
LABEL license="https://github.com/lh3/seqtk/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"

# copy in files and executables into app stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH" LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "seqtk"]

# 'WORKDIR' sets working directory
WORKDIR /data

FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# seqtk does not have a -h option, and just calling the command results in an error
RUN which seqtk 

RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    seqtk sample -s100 SRR13957123_1.fastq.gz 10000 > sub1.fq && \
    seqtk sample -s100 SRR13957123_2.fastq.gz 10000 > sub2.fq && \
    seqtk trimfq SRR13957123_1.fastq.gz > trimfq_out.fq.gz && \
    wc -l *fastq.gz *fq*