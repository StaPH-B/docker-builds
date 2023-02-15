# base image
FROM ubuntu:bionic as app

# add ARG here
ARG fasttree_ver="2.1.11"

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="Fasttree"
LABEL software.version="2.1.11"
LABEL description="Infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide or protein sequences"
LABEL website="http://www.microbesonline.org/fasttree/"
LABEL license="http://www.microbesonline.org/fasttree/"
LABEL dockerfile.version="1"
LABEL maintainer="Daniel Evans"
LABEL maintainer.email="evansdr95@gmail.com"

# install ubuntu dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install fasttree
RUN wget http://www.microbesonline.org/fasttree/FastTree && \
  chmod +x FastTree && \
  mkdir fasttree && \
  mv FastTree /fasttree/

# add to path
ENV PATH="${PATH}:/fasttree"

RUN mkdir /data

WORKDIR /data

# test layer
# run FastTree on a two-genome alignment, then print the tree

FROM app as test

ARG fasttree_ver="2.1.11"

COPY covid_alignment.fasta /data/covid_alignment.fasta

RUN echo "Running command: $ FastTree -log fasttree_test_log -nt /data/covid_alignment.fasta > fasttree_test_tree.nwk" && \
FastTree -log fasttree_test_log -nt /data/covid_alignment.fasta > fasttree_test_tree.nwk && \
echo "Printing FastTree output tree..." && \
cat fasttree_test_tree.nwk && \
echo "Dockerfile test complete!"
