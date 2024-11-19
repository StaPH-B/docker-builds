FROM ubuntu:jammy AS app

# for easy upgrade later. ARG variables only persist during image build time
ARG KLEBORATE_VER="3.1.2"
ARG MINIMAP2_VER="2.28"
ARG MASH_VER="2.3"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Kleborate"
LABEL software.version="${KLEBORATE_VER}"
LABEL description="tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC)"
LABEL website="https://github.com/katholt/Kleborate"
LABEL license="https://github.com/katholt/Kleborate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Frank Ambrosio"
LABEL maintainer2.email="frank.ambrosio@theiagen.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

# install prerequisites. Cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        wget \
        ca-certificates \
        bzip2 \
        procps \
        curl && \
        rm -rf /var/lib/apt/lists/* && apt-get autoclean

# mash; update UID and GID of mash files; make /data
# UID and GID changes because the original owner is UID: 1081147385 and GID: 1360859114 which does NOT play well with systems that limits GIDs and UIDs
RUN wget -q https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
        tar -xvf mash-Linux64-v${MASH_VER}.tar --no-same-owner && \
        rm -rf mash-Linux64-v${MASH_VER}.tar && \
        chown root:root /mash-Linux64-v${MASH_VER}/* 

# install minimap2 binary
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | \
        tar -jxvf - --no-same-owner

# set PATH
ENV PATH="/mash-Linux64-v${MASH_VER}:/minimap2-${MINIMAP2_VER}_x64-linux:${PATH}"

# install kleborate; uninstall mash (that comes with kleborate via pypi, see: https://github.com/klebgenomics/Kleborate/issues/90); make /data
RUN pip install --no-cache-dir kleborate==${KLEBORATE_VER} && \
        pip uninstall mash -y && \
        mkdir /data

# set working directory
WORKDIR /data

CMD [ "kleborate", "--help" ]

FROM app AS test

WORKDIR /test

# from https://kleborate.readthedocs.io/en/latest/Installation.html
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/813/595/GCF_002813595.1_ASM281359v1/GCF_002813595.1_ASM281359v1_genomic.fna.gz && \
        kleborate -a GCF_002813595.1_ASM281359v1_genomic.fna.gz -o kleborate_test -p kpsc && \
        head kleborate_test/klebsiella_pneumo_complex_output.txt

# print help and version info
RUN kleborate --help && kleborate --version && kleborate --list_modules