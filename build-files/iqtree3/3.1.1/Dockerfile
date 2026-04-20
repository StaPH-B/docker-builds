ARG IQTREE3_VER="3.1.1"

FROM ubuntu:noble AS app

# for easy upgrade later. ARG variables only persist during build time.
ARG IQTREE3_VER

# metadata
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="IQ-TREE 3"
LABEL software.version="${IQTREE3_VER}"
LABEL description="Efficient and versatile phylogenomic software by maximum likelihood"
LABEL website="http://www.iqtree.org/"
LABEL source.code.website="https://github.com/iqtree/iqtree3"
LABEL license="https://github.com/iqtree/iqtree3/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"


#install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget ca-certificates procps && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

# download and uncompress iqtree3 tarball
RUN wget -q https://github.com/iqtree/iqtree3/releases/download/v${IQTREE3_VER}/iqtree-${IQTREE3_VER}-Linux-intel.tar.gz && \
    tar -xvf iqtree-${IQTREE3_VER}-Linux-intel.tar.gz && \
    rm -v iqtree-${IQTREE3_VER}-Linux-intel.tar.gz

# set PATH and locale settings for singularity compatibility
ENV PATH="/iqtree-${IQTREE3_VER}-Linux-intel/bin:${PATH}"\
    LC_ALL=C

# final working directory is /data
WORKDIR /data

# default command is to pull up help options
CMD [ "iqtree3", "--help" ]

FROM app AS test

ARG IQTREE3_VER

# print version and help
RUN iqtree3 --version && iqtree3 --help

###TEST TREE TOPOLOGY
RUN iqtree3 -s /iqtree-${IQTREE3_VER}-Linux-intel/example.phy --rate
