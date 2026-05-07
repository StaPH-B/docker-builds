# Use ubuntu as base image
FROM ubuntu:noble AS app

# metadata
LABEL base.image="ubuntu:noble"
LABEL version="2585414"
LABEL software="cdc-spn"
LABEL dockerfile.version="1"
LABEL software.version="0.1"
LABEL description="Scripts and reference files to type streptococcus pneumoniae"
LABEL website="https://github.com/BenJamesMetcalf/Spn_Scripts_Reference"
LABEL license="https://github.com/BenJamesMetcalf/Spn_Scripts_Reference"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"

# install dependencies
RUN apt-get update && apt-get install -y \
  perl \
  wget \
  git \
  ncbi-blast+ \
  bedtools \
  prodigal \
  python3 \
  python3-pip \
  python3-scipy \
  cutadapt \
  bowtie2 \
  zlib1g-dev \
  libbz2-dev \
  liblzma-dev \
  build-essential \
  libncurses5-dev \
  libcurl4-openssl-dev \
  autoconf \
  meson \
  ninja-build \
  pkg-config \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install samtools 1.19 but rename it so srst2 uses conda's samtools 0.1.18
RUN wget https://github.com/samtools/samtools/releases/download/1.19/samtools-1.19.tar.bz2 \
  && tar -xjf samtools-1.19.tar.bz2 \
  && rm samtools-1.19.tar.bz2 \
  && cd samtools-1.19 \
  && ./configure --prefix=/usr/local \
  && make \
  && make install \
  && mv /usr/local/bin/samtools /usr/local/bin/samtools-1.19

# install miniforge
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O /miniforge.sh \
  && bash /miniforge.sh -b -p /opt/conda \
  && rm /miniforge.sh \
  && /opt/conda/bin/conda clean -a

# install srst2 in a Python 2.7 conda environment with compatible samtools
RUN /opt/conda/bin/conda create -y -n srst2_env python=2.7 \
  && /opt/conda/bin/conda install -y -n srst2_env -c bioconda -c conda-forge srst2 \
  && /opt/conda/bin/conda clean -a
  
ENV PATH="/opt/conda/envs/srst2_env/bin:/opt/conda/bin:${PATH}"

# install freebayes v1.3.6
RUN git clone --recursive https://github.com/freebayes/freebayes.git \
  && cd freebayes \
  && git checkout v1.3.6 \
  && git submodule update --init --recursive \
  && sed -i '1s/^/#include <limits>\n/' intervaltree/IntervalTree.h \
  && meson setup build/ --buildtype release \
  && cd build \
  && ninja \
  && ninja install

# add the spn scripts pinned to commit 2585414
RUN git clone https://github.com/BenJamesMetcalf/Spn_Scripts_Reference.git \
  && cd Spn_Scripts_Reference \
  && git checkout 2585414

WORKDIR /data

ENV PATH="/opt/conda/envs/srst2_env/bin:/opt/conda/bin:/Spn_Scripts_Reference:/usr/local/bin:${PATH}" \
  LC_ALL=C
  
  
# ---- test stage ----
FROM app AS test

WORKDIR /test_data

# install sra-toolkit for test data download
RUN apt-get update && apt-get install -y sra-toolkit \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# run test - ERR1795461 is Streptococcus pneumoniae, expected serotype 6B
RUN fasterq-dump ERR1795461 --split-files -O /test_data \
  && perl /Spn_Scripts_Reference/SPN_Serotyper.pl \
     -1 /test_data/ERR1795461_1.fastq \
     -2 /test_data/ERR1795461_2.fastq \
     -r /Spn_Scripts_Reference/SPN_Reference_DB/SPN_Sero_Gene-DB_Final.fasta \
     -o /test_output \
     -n ERR1795461 \
     2>&1 \
  && cat /test_output/OUT_SeroType_Results.txt \
  && grep -q "6B" /test_output/OUT_SeroType_Results.txt \
  && echo "PASS: Serotype 6B correctly called" \
  && rm -rf /test_data /test_output
