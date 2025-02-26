FROM mambaorg/micromamba:1.5.6 as app

ARG GUBBINS_VER="3.3.3"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.6"
LABEL dockerfile.version="1"
LABEL software="Gubbins"
LABEL software.version="${GUBBINS_VER}"
LABEL description="Genealogies Unbiased By recomBinations In Nucleotide Sequences"
LABEL website="https://github.com/nickjcroucher/gubbins"
LABEL license="https://github.com/nickjcroucher/gubbins/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    procps &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda gubbins=${GUBBINS_VER} && \
    micromamba clean -a -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD ["run_gubbins.py", "-h"]

WORKDIR /data

FROM app as test

ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /test

RUN curl -LJO https://github.com/nickjcroucher/gubbins/raw/master/tests/data/alignment_file_multiple_lines_per_sequence.aln &&\
    run_gubbins.py alignment_file_multiple_lines_per_sequence.aln

