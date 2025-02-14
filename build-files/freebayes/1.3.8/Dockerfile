FROM mambaorg/micromamba:2.0.5-ubuntu22.04 AS app

ARG FREEBAYES_VER="1.3.8"

USER root
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.0.5-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="FreeBayes"
LABEL software.version="${FREEBAYES_VER}"
LABEL description="FreeBayes is a haplotype-based variant detector and is a great tool for calling variants from a population."
LABEL website="https://github.com/freebayes/freebayes"
LABEL license="https://github.com/freebayes/freebayes/blob/master/LICENSE"
LABEL maintainer="Kitty Chase"
LABEL maintainer.email="kitty.chase@dhhs.nc.gov"
LABEL maintainer2="Jill Hagey"
LABEL maintainer2.email="jvhagey@gmail.com"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda -c defaults freebayes=${FREEBAYES_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "freebayes", "--help" ]

# set final working directory to /data
WORKDIR /data

FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN freebayes --help

RUN wget https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123.sorted.bam && \
    wget https://raw.githubusercontent.com/artic-network/primer-schemes/refs/heads/master/nCoV-2019/V5.3.2/SARS-CoV-2.reference.fasta && \
    freebayes -f SARS-CoV-2.reference.fasta SRR13957123.sorted.bam > var.vcf && \
    head var.vcf
