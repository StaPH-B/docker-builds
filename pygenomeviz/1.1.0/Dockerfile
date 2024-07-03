FROM python:3.9.17-slim as app

ARG PYGENOMEVIZ_VER="1.1.0"

LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="pyGenomeViz"
LABEL software.version=$PYGENOMEVIZ_VER
LABEL description="genome visualization python package for comparative genomics"
LABEL website="https://moshi4.github.io/pyGenomeViz"
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
    ncbi-blast+ \
    mmseqs2 \
    mummer \
    progressivemauve && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pygenomeviz==$PYGENOMEVIZ_VER 

ENV LC_ALL=C.UTF-8

CMD pgv-mmseqs --help && pgv-mummer --help && pgv-pmauve --help && pgv-blast --help

WORKDIR /data

FROM app as test

WORKDIR /test

RUN pgv-mmseqs --help && pgv-mummer --help && pgv-pmauve --help && pgv-blast --help

RUN \
    # Download example dataset
    pgv-download yersinia_phage && \
    # Run BLAST CLI workflow
    pgv-blast NC_070914.gbk NC_070915.gbk NC_070916.gbk NC_070918.gbk \
        -o pgv-blast_example --seqtype protein --show_scale_bar --curve \
        --feature_linewidth 0.3 --length_thr 100 --identity_thr 30 && \
    # Download example dataset
    pgv-download mycoplasma_mycoides && \
    # Run MUMmer CLI workflow
    pgv-mummer GCF_000023685.1.gbff GCF_000800785.1.gbff GCF_000959055.1.gbff GCF_000959065.1.gbff \
        -o pgv-mummer_example --show_scale_bar --curve \
        --feature_type2color CDS:blue rRNA:lime tRNA:magenta && \
    # Download example dataset
    pgv-download enterobacteria_phage && \
    # Run MMseqs CLI workflow
    pgv-mmseqs NC_013600.gbk NC_016566.gbk NC_019724.gbk NC_024783.gbk NC_028901.gbk NC_031081.gbk \
        -o pgv-mmseqs_example --show_scale_bar --curve --feature_linewidth 0.3 \
        --feature_type2color CDS:skyblue --normal_link_color chocolate --inverted_link_color limegreen && \
    # Download example dataset
    pgv-download escherichia_coli && \
    # Run progressiveMauve CLI workflow
    pgv-pmauve NC_000913.gbk.gz NC_002695.gbk.gz NC_011751.gbk.gz NC_011750.gbk.gz \
        -o pgv-pmauve_example --show_scale_bar && \
    # Check final files
    ls pgv-blast_example/result.png pgv-mummer_example/result.png pgv-mmseqs_example/result.png pgv-pmauve_example/result.png
