FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version="3.1.1b"
LABEL description="NCBI resistance gene detection tool"
LABEL website="https://github.com/ncbi/amr"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"

RUN apt-get update && apt-get install -y python \
  wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
  bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda && \
  rm Miniconda3-latest-Linux-x86_64.sh

RUN bash -c '/miniconda/bin/conda install -y -c bioconda blast hmmer libcurl'

RUN bash -c '/miniconda/bin/conda install -y https://anaconda.org/bioconda/ncbi-amrfinderplus/3.1.1b/download/linux-64/ncbi-amrfinderplus-3.1.1b-hf18293b_0.tar.bz2' &&\
  /miniconda/bin/amrfinder -u

ENV PATH="/miniconda/bin:${PATH}"
WORKDIR /data
