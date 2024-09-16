FROM python:3.9.17-slim as app

ARG PYGENOMEVIZ_VER="0.4.3"

LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="pyGenomeViz"
LABEL software.version=$PYGENOMEVIZ_VER
LABEL description="genome visualization python package for comparative genomics"
LABEL website="https://moshi4.github.io/pyGenomeViz/"
LABEL license="MIT License"
LABEL license.url="https://github.com/moshi4/pyGenomeViz/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

#mmseqs2=14-7e284+ds-1+b2
#mummer=3.23+dfsg-8
#progressivemauve=1.2.0+4713+dfsg-5+b1
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    procps \
    mmseqs2 \
    mummer \
    progressivemauve && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pygenomeviz==$PYGENOMEVIZ_VER 

ENV LC_ALL=C.UTF-8

CMD pgv-simpleplot --help && pgv-mmseqs --help && pgv-mummer --help && pgv-pmauve --help

WORKDIR /data

FROM app as test

WORKDIR /test

RUN pgv-simpleplot --help && pgv-mmseqs --help && pgv-mummer --help && pgv-pmauve --help

RUN pgv-download-dataset -n erwinia_phage && \
    pgv-mummer --gbk_resources MT939486.gbk MT939487.gbk MT939488.gbk LT960552.gbk -o mummer_test --tick_style axis --align_type left --feature_plotstyle arrow && \
    pgv-mmseqs --gbk_resources MT939486.gbk MT939487.gbk MT939488.gbk LT960552.gbk -o mmseqs_test --tick_style axis --align_type left --feature_plotstyle arrow && \
    pgv-download-dataset -n escherichia_coli && \
    pgv-pmauve --seq_files NC_000913.gbk NC_002695.gbk NC_011751.gbk NC_011750.gbk -o pmauve_test --tick_style bar && \
    ls mummer_test/result.png mmseqs_test/result.png pmauve_test/result.png 
