ARG USHER_VER="0.6.3"

FROM mambaorg/micromamba:2.0.5-ubuntu22.04 AS app

ARG USHER_VER

USER root
WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:2.0.5-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="UShER"
LABEL software.version="${USHER_VER}"
LABEL description="Ultrafast Sample Placement on Existing Trees."
LABEL website="https://github.com/yatisht/usher"
LABEL license="https://github.com/yatisht/usher/blob/master/LICENSE"
LABEL documentation="https://usher-wiki.readthedocs.io/en/latest/QuickStart.html"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda -c defaults usher=${USHER_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "usher", "--help" ]

WORKDIR /data

FROM app AS test

ARG USHER_VER

RUN usher --help && \
    usher --version

WORKDIR /test

RUN wget -q https://github.com/yatisht/usher/archive/refs/tags/v${USHER_VER}.tar.gz && \
    tar -xvf v${USHER_VER}.tar.gz

WORKDIR /test/usher-${USHER_VER}

#RUN ls  && whatever 
# https://usher-wiki.readthedocs.io/en/latest/UShER.html
RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -d output/

RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -c -d output2/

RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -c -u -d output3/

RUN usher -i global_assignments.pb -v test/new_samples.vcf -u -d output4/

RUN usher -i global_assignments.pb -v test/new_samples.vcf -u -k 20 -d output5/

RUN usher -i global_assignments.pb -v test/new_samples.vcf -u -o new_global_assignments.pb -d output6/