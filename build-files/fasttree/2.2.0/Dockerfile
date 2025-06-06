# base image
FROM ubuntu:jammy AS app

# add ARG here
ARG fasttree_ver="2.2.0"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL version="1"
LABEL software="Fasttree"
LABEL software.version="${fasttree_ver}"
LABEL description="Infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences"
LABEL website="https://github.com/morgannprice/fasttree"
LABEL license="https://github.com/morgannprice/fasttree/blob/main/LICENSE"
LABEL dockerfile.version="1"
LABEL maintainer="Daniel Evans"
LABEL maintainer.email="evansdr95@gmail.com"
LABEL maintainer1="Erin Young"
LABEL maintainer1.email="eriny@utah.gov"

# install ubuntu dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  ca-certificates \
  procps && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install fasttree
RUN wget https://github.com/morgannprice/fasttree/archive/refs/tags/v${fasttree_ver}.tar.gz && \
  tar -vxf v${fasttree_ver}.tar.gz && \
  chmod +x */FastTree && \
  mv */FastTree /usr/local/bin/. && \
  rm -rf fasttree-* && \
  rm v${fasttree_ver}.tar.gz && \
  mkdir /data

# add to path
ENV PATH="${PATH}:/fasttree"

CMD ["FastTree", "-help"]

WORKDIR /data

# test layer
# run FastTree on a two-genome alignment, then print the tree

FROM app AS test

RUN FastTree -help

RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/refs/heads/master/build-files/fasttree/2.1.11/covid_alignment.fasta && \
  FastTree -log fasttree_test_log -nt /data/covid_alignment.fasta > fasttree_test_tree.nwk && \
  cat fasttree_test_tree.nwk