ARG USHER_VER="0.6.6"

FROM mambaorg/micromamba:2.3.0-ubuntu22.04 AS app

ARG USHER_VER

USER root
WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="UShER"
LABEL software.version="${USHER_VER}"
LABEL description="Ultrafast Sample Placement on Existing Trees."
LABEL website="https://github.com/yatisht/usher"
LABEL license="https://github.com/yatisht/usher/blob/master/LICENSE"
LABEL documentation="https://usher-wiki.readthedocs.io/en/latest/QuickStart.html"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN micromamba install --name base -c conda-forge -c bioconda usher=${USHER_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "usher", "--help" ]

WORKDIR /data

FROM app AS test

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

ARG USHER_VER

RUN usher --help && \
    usher --version

WORKDIR /test

RUN wget -q https://github.com/yatisht/usher/archive/refs/tags/v${USHER_VER}.tar.gz && \
    tar -xvf v${USHER_VER}.tar.gz

WORKDIR /test/usher-${USHER_VER}

# https://usher-wiki.readthedocs.io/en/latest/UShER.html
RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -d output/ && \
    usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -c -d output2/ && \
    usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -c -u -d output3/ && \
    usher -i global_assignments.pb -v test/new_samples.vcf -u -d output4/ && \
    usher -i global_assignments.pb -v test/new_samples.vcf -u -k 20 -d output5/ && \
    usher -i global_assignments.pb -v test/new_samples.vcf -u -o new_global_assignments.pb -d output6/

# testing the other executables
RUN matUtils summary -i global_assignments.pb > summary.txt &&\
    matOptimize -i global_assignments.pb -o optimized_tree.pb

RUN micromamba list -n base