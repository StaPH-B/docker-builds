ARG PBSIM3_VER="3.0.5"

## Builder ##
FROM ubuntu:noble AS builder

ARG PBSIM3_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/yukiteruono/pbsim3/archive/refs/tags/v${PBSIM3_VER}.tar.gz &&\
    tar -xvf v${PBSIM3_VER}.tar.gz && rm v${PBSIM3_VER}.tar.gz &&\
    cd pbsim3-${PBSIM3_VER} &&\
    ./configure &&\
    make && make install

## App ##
FROM ubuntu:noble AS app

ARG PBSIM3_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="SoftwareName"
LABEL software.version="${PBSIM3_VER}"
LABEL description="A simulator for all types of Pacific Biosciences (PacBio) and Oxford Nanopore Technologies (ONT) long reads."
LABEL website="https://github.com/yukiteruono/pbsim3"
LABEL license="https://github.com/yukiteruono/pbsim3/blob/master/COPYING"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder pbsim3-${PBSIM3_VER}/data/* /model/

ENV LC_ALL=C

CMD ["/bin/bash", "-c", "echo 'DATA: quality score and error models are located at /model' && pbsim" ]

WORKDIR /data

## Test ##
FROM app AS test 

ARG PBSIM3_VER

COPY --from=builder pbsim3-${PBSIM3_VER}/sample/sample.fasta /data/

RUN pbsim --strategy wgs \
    --method qshmm \
    --qshmm /model/QSHMM-RSII.model \
    --depth 5 \
    --genome sample.fasta


