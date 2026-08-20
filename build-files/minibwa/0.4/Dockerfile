ARG MINIBWA_VER="0.4"

FROM ubuntu:noble AS app
ARG MINIBWA_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="minibwa"
LABEL software.version="${MINIBWA_VER}"
LABEL description="Aligns short reads against a reference genome; it is 3x as fast as bwa-mem and 2x as fast as bwa-mem2 at comparable accuracy."
LABEL website="https://github.com/lh3/minibwa"
LABEL license="https://github.com/lh3/minibwa/blob/master/LICENSE.txt"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    bzip2 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin/minibwa

RUN wget -O minibwa.tar.bz2 "https://github.com/lh3/minibwa/releases/download/v${MINIBWA_VER}/minibwa-${MINIBWA_VER}_x64-linux.tar.bz2" && \
    tar --strip-components=1 -xjf minibwa.tar.bz2 && \
    rm minibwa.tar.bz2

WORKDIR /data
ENV PATH="/usr/local/bin/minibwa:$PATH" \
    LC_ALL=C

CMD [ "minibwa", "--help" ]


FROM app AS test
ARG MINIBWA_VER

WORKDIR /test
RUN minibwa version && minibwa --help

RUN mkdir /test/minibwa_source && \
    wget -O minibwa.tar.gz "https://github.com/lh3/minibwa/archive/refs/tags/v${MINIBWA_VER}.tar.gz" && \
    tar -C /test/minibwa_source --strip-components=1 -xzf minibwa.tar.gz && \
    mv /test/minibwa_source/test/* /test && \
    rm minibwa.tar.gz

# From the project README.md
# Index the genome and align and output in sam format
RUN minibwa index chrM-human.fa.gz chrM-human && \                  
    minibwa map chrM-human chrM-read_?.fa.gz > aln.sam && \
    head -n 20 aln.sam

