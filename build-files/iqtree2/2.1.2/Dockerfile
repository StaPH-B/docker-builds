FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during build time.
ARG IQTREE2_VER="2.1.2"

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="IQ-Tree2"
LABEL software.version="2.1.2"
LABEL description="Efficient software for phylogenomic inference"
LABEL website="http://www.iqtree.org/"
LABEL source.code.website="https://github.com/iqtree/iqtree2"
LABEL license="https://github.com/iqtree/iqtree2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

#install dependencies
RUN apt-get update && apt-get install -y \
 wget

# download, uncompress iqtree2 tarball; make /data
RUN wget https://github.com/iqtree/iqtree2/releases/download/v${IQTREE2_VER}/iqtree-${IQTREE2_VER}-Linux.tar.gz && \
 tar -xzvf iqtree-${IQTREE2_VER}-Linux.tar.gz && \
 rm -v iqtree-${IQTREE2_VER}-Linux.tar.gz && \
 mkdir /data

# set PATH and locale settings for singularity compatibility
ENV PATH="/iqtree-${IQTREE2_VER}-Linux/bin:${PATH}"\
 LC_ALL=C
WORKDIR /data
