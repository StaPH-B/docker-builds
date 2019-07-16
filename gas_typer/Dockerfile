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
  python-scipy \
  prodigal

RUN cd /samtools &&\
  wget https://github.com/samtools/samtools/archive/0.1.18.tar.gz &&\
  tar -xzf 0.1.18.tar.gz &&\
  rm 0.1.18.tar.gz &&\
  cd samtools-0.1.18 &&\
  make


# install an ancient freebayes version 
#install freebayes
RUN git clone --recursive https://github.com/ekg/freebayes.git
RUN cd freebayes/;git checkout v0.9.21 && git submodule update --recursive;make; make install

# install blast
RUN wget 'ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.29/ncbi-blast-2.2.29+-x64-linux.tar.gz' &&\
tar -xzf ncbi-blast-2.2.29+-x64-linux.tar.gz &&\
rm ncbi-blast-2.2.29+-x64-linux.tar.gz 

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

# install srst2
RUN wget https://github.com/katholt/srst2/archive/v0.2.0.tar.gz
RUN tar -xzvf v0.2.0.tar.gz;rm v0.2.0.tar.gz;pip install srst2-0.2.0/

# get GAS_Scripts_Reference v1.0
RUN cd / &&\
  git clone https://github.com/kevinlibuit/GAS_Scripts_Reference.git &&\
  chmod +x /GAS_Scripts_Reference/*

ENV PATH = "${PATH}:/GAS_Scripts_Reference/"


WORKDIR /data
