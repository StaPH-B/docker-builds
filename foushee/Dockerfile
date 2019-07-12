FROM staphb/shovill:1.0.4
 
# metadata
LABEL base.image="staphb/shovill:1.0.4"
LABEL version="1"
LABEL software="GAS_Typer"
LABEL software.version="1.0"
LABEL description="GAS isolate typing system developed by Metcalf laboratory (CDC) with slight modifications by Kevin G Libuit (DCLS)"
LABEL website="https://github.com/BenJamesMetcalf/GAS_Scripts_Reference"

MAINTAINER Kevin Libuit <kevin.libuit@dgs.virginia.gov>

RUN apt-get update && apt-get install -y \
  perl \
  git \
  cmake \
  build-essential \
  bowtie2 \
  bedtools \
  pkg-config \
  python-pip \
  prodigal

# install an ancient samtools version
RUN mkdir samtools &&\
  cd samtools &&\
  wget https://github.com/samtools/samtools/archive/0.1.18.tar.gz &&\
  tar -xzf 0.1.18.tar.gz &&\
  rm 0.1.18.tar.gz &&\
  cd samtools-0.1.18 &&\
  make

ENV PATH ="${PATH}:/samtools/samtools-0.1.18/"

# install an ancient freebayes version 
#install freebayes
RUN git clone --recursive https://github.com/ekg/freebayes.git
RUN cd freebayes/;git checkout v0.9.21 && git submodule update --recursive;make; make install

# install vcf tools
RUN wget https://github.com/vcftools/vcftools/releases/download/v0.1.15//vcftools-0.1.15.tar.gz -O /tmp/vcftools-0.1.15.tar.gz && \
  tar xvf /tmp/vcftools-0.1.15.tar.gz -C /tmp && \
  rm /tmp/vcftools-0.1.15.tar.gz && \
  cd /tmp/vcftools-0.1.15 && \
  ./configure && \
  make && \
  make install && \
  cd / && \
  rm -rf /tmp/vcftools-0.1.15

# install cutadapt 1.8.3
RUN pip install cutadapt==1.8.3



WORKDIR /data
