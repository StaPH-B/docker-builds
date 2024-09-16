ARG IQTREE2_VER="2.3.4"

FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during build time.
ARG IQTREE2_VER

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="IQ-Tree2"
LABEL software.version="${IQTREE2_VER}"
LABEL description="Efficient software for phylogenomic inference"
LABEL website="http://www.iqtree.org/"
LABEL source.code.website="https://github.com/iqtree/iqtree2"
LABEL license="https://github.com/iqtree/iqtree2/blob/master/LICENSE"
LABEL maintainer="Jade Wang"
LABEL maintainer.email="jwang7@health.nyc.gov"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

#install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget ca-certificates procps && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

# download, uncompress iqtree2 tarball; make /data
RUN wget -q https://github.com/iqtree/iqtree2/releases/download/v${IQTREE2_VER}/iqtree-${IQTREE2_VER}-Linux-intel.tar.gz && \
    tar -xvf iqtree-${IQTREE2_VER}-Linux-intel.tar.gz && \
    rm -v iqtree-${IQTREE2_VER}-Linux-intel.tar.gz && \
    mkdir /data

# set PATH and locale settings for singularity compatibility
ENV PATH="/iqtree-${IQTREE2_VER}-Linux-intel/bin:${PATH}"\
    LC_ALL=C

# final working directory is /data
WORKDIR /data

# default command is to pull up help options
CMD [ "iqtree2", "--help" ]

FROM app as test

ARG IQTREE2_VER

# print version and help
RUN iqtree2 --version && iqtree2 --help

###TEST TREE TOPOLOGY
RUN iqtree2 -s /iqtree-${IQTREE2_VER}-Linux-intel/example.phy --rate
