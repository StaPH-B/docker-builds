FROM mambaorg/micromamba:2.0.5-ubuntu22.04 AS app

ARG VIRSORTER2_VER="2.2.4"

USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.0.5-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="virsorter2"
LABEL software.version="${VIRSORTER2_VER}"
LABEL description="VirSorter2 applies a multi-classifier, expert-guided approach to detect diverse DNA and RNA virus genomes."
LABEL website="https://github.com/jiarong/VirSorter2"
LABEL license="https://github.com/jiarong/VirSorter2/blob/master/LICENSE"
LABEL maintainer="Joachim Johansen"
LABEL maintainer.email="joacjohansen@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda virsorter=${VIRSORTER2_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "virsorter", "--help" ]

# set final working directory to /data
WORKDIR /data

# A second FROM insruction creates a new stage
# new base for testing
FROM app AS test

RUN virsorter --help

WORKDIR /test

# virsorter setup -d db -j 4 results in permissions errors
RUN wget -O db.tgz https://osf.io/v46sc/download && \
    tar -xzf db.tgz --no-same-owner && \
    rm db.tgz && \
    virsorter config --init-source --db-dir=./db && \
    # from https://github.com/jiarong/VirSorter2?tab=readme-ov-file#quick-run
    wget -O test.fa https://raw.githubusercontent.com/jiarong/VirSorter2/master/test/8seq.fa && \
    virsorter run -w test.out -i test.fa --min-length 1500 -j 4 all && \
    ls test.out && \
    # to reduce size for GA testing
    rm -rf db

RUN micromamba list
