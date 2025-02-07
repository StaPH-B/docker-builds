FROM mambaorg/micromamba:1.5.8 AS app

ARG CHECKM2_VERSION="1.0.2"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="CHECKM2"
LABEL software.version="${CHECKM2_VERSION}"
LABEL description="Rapid assessment of genome bin quality using machine learning."
LABEL website="https://github.com/chklovski/CheckM2"
LABEL license="https://github.com/chklovski/CheckM2/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda checkm2=${CHECKM2_VERSION} && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "checkm2", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test 

RUN checkm2 database --download &&\
    checkm2 testrun --threads 4