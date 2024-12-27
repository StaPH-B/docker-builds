FROM mambaorg/micromamba:0.24.0 as app

USER root

WORKDIR /

ARG PYGENOMEVIZ_VER="0.2.2"
ARG MMSEQ2_VER="13.45111"
ARG MUMMER_VER="3.23"
ARG PROGRESSIVEMAUVE_VER="snapshot_2015_02_13"

LABEL base.image="mambaorg/micromamba:0.24.0"
LABEL dockerfile.version="1"
LABEL software="pyGenomeViz"
LABEL software.version=$PYGENOMEVIZ_VER
LABEL description="genome visualization python package for comparative genomics"
LABEL website="https://github.com/moshi4/pyGenomeViz"
LABEL license="MIT License"
LABEL license.url="https://github.com/moshi4/pyGenomeViz/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba create -n pygenomeviz-env \
    -c conda-forge -c bioconda -c defaults \
    pygenomeviz=$PYGENOMEVIZ_VER \
    mmseqs2=$MMSEQ2_VER \
    mummer=$MUMMER_VER \
    progressivemauve=$PROGRESSIVEMAUVE_VER && \
    micromamba clean -a -y

ENV PATH="/opt/conda/envs/pygenomeviz-env/bin:${PATH}" \
    LC_ALL=C.UTF-8 \
    ENV_NAME="pygenomeviz-env"

ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /data

FROM app as test

ENV ENV_NAME="pygenomeviz-env"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /test

RUN pgv-download-dataset -n erwinia_phage && \
    pgv-mummer --gbk_resources MT939486.gbk MT939487.gbk MT939488.gbk LT960552.gbk -o mummer_test --tick_style axis --align_type left --feature_plotstyle arrow && \
    pgv-mmseqs --gbk_resources MT939486.gbk MT939487.gbk MT939488.gbk LT960552.gbk -o mmseqs_test --tick_style axis --align_type left --feature_plotstyle arrow && \
    pgv-download-dataset -n escherichia_coli && \
    pgv-pmauve --seq_files NC_000913.gbk NC_002695.gbk NC_011751.gbk NC_011750.gbk -o pmauve_test --tick_style bar && \
    ls mummer_test/result.png mmseqs_test/result.png pmauve_test/result.png 
