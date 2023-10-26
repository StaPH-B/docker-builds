ARG DRPRG_VER="0.1.1"

FROM ubuntu:jammy AS builder
# "inspired" by https://github.com/mbhall88/drprg/blob/main/Dockerfile

ARG DRPRG_VER
ARG RASUSA_VER="0.7.0"
ARG SEQFU_VER="1.16.0"
ARG PANDORA_VER="0.9.2"
ARG MAKEPRG_VER="0.3.0"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    unzip && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# download drprg source code from github
RUN wget -q https://github.com/mbhall88/drprg/releases/download/${DRPRG_VER}/drprg-${DRPRG_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    tar -xvf drprg-${DRPRG_VER}-x86_64-unknown-linux-gnu.tar.gz && \
    cp drprg-${DRPRG_VER}-x86_64-unknown-linux-gnu/drprg /usr/bin/drprg && \
    chmod +x /usr/bin/drprg    

# download makeprg
RUN wget -q https://github.com/leoisl/make_prg/releases/download/v${MAKEPRG_VER}/make_prg_${MAKEPRG_VER} && \
    cp make_prg_${MAKEPRG_VER} /usr/bin/make_prg && \
    chmod +x /usr/bin/make_prg

# downloading pandora
RUN wget -q https://github.com/rmcolq/pandora/releases/download/${PANDORA_VER}/pandora-linux-precompiled-v${PANDORA_VER} && \
    cp pandora-linux-precompiled-v${PANDORA_VER} /usr/bin/pandora && \
    chmod +x /usr/bin/pandora

# install rasusa
RUN wget -q https://github.com/mbhall88/rasusa/releases/download/${RASUSA_VER}/rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl.tar.gz && \
    tar -xvf rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl.tar.gz && \
    cp rasusa-${RASUSA_VER}-x86_64-unknown-linux-musl/rasusa /usr/bin/rasusa && \
    chmod +x /usr/bin/rasusa

# install seqfu
RUN wget -q https://github.com/telatin/seqfu2/releases/download/v${SEQFU_VER}/SeqFu-v${SEQFU_VER}-Linux-x86_64.zip && \
    unzip -d /usr/bin SeqFu-v${SEQFU_VER}-Linux-x86_64.zip

# test dependencies before moving on
RUN drprg --help && \
    pandora --help && \
    make_prg --help && \
    seqfu version && \
    rasusa --version

FROM staphb/bcftools:1.18 AS builder2

FROM ubuntu:jammy AS app

ARG MAFFT_VER="7.505"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Dr. PRG"
LABEL software.version="${DRPRG_VER}"
LABEL description="Antimicrobial resistance prediction"
LABEL website="https://github.com/mbhall88/drprg"
LABEL license="https://github.com/mbhall88/drprg/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

COPY --from=builder  /usr/bin/*       /usr/local/bin/
COPY --from=builder2 /usr/local/bin/* /usr/local/bin/

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    unzip \
    perl \
    zlib1g \
    libncurses5 \
    bzip2 \
    liblzma-dev \
    libcurl4-gnutls-dev \
    procps && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

# install mafft
RUN wget -q https://mafft.cbrc.jp/alignment/software/mafft_${MAFFT_VER}-1_amd64.deb && \
    dpkg -i mafft_${MAFFT_VER}-1_amd64.deb

# test dependencies before moving on
RUN drprg --help && \
    pandora --help && \
    make_prg --help && \
    mafft --version && \
    bcftools --version && \
    seqfu version && \
    rasusa --version

ENV PATH="$PATH" \
    LC_ALL=C

CMD drprg --help

WORKDIR /data

FROM app AS test

WORKDIR /test

# test dependencies
RUN drprg --help && \
    pandora --help && \
    make_prg --help && \
    mafft --version && \
    bcftools --version && \
    seqfu version && \
    rasusa --version

# testing index and prediction
RUN drprg index --download mtb@latest && \
    drprg index --list && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR230/005/SRR23086705/SRR23086705_1.fastq.gz && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR230/005/SRR23086705/SRR23086705_2.fastq.gz && \
    cat SRR23086705_1.fastq.gz SRR23086705_2.fastq.gz > test.fastq.gz && \
    drprg predict -x mtb -i test.fastq.gz --illumina -o outdir/ && \
    ls outdir/*