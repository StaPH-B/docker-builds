#Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="cdc-spn"
LABEL software.version="0.1"
LABEL description="Scripts and reference files to type streptococcus pneumoniae"
LABEL website="https://github.com/BenJamesMetcalf/Spn_Scripts_Reference"
LABEL license="https://github.com/BenJamesMetcalf/Spn_Scripts_Reference"

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>

#install dependencies
RUN apt-get update && apt-get install -y \
  perl\
  wget\
  git\
  ncbi-blast+\
  bedtools\
  prodigal\
  python\
  python-cutadapt\
  python-scipy\
  bowtie2\
  python-pip\
  environment-modules\
  velvet\
  zlib1g-dev\
  libbz2-dev\
  liblzma-dev\
  build-essential\
  libncurses5-dev

#install samtools version 0.1.18
RUN wget 'https://sourceforge.net/projects/samtools/files/samtools/0.1.18/samtools-0.1.18.tar.bz2'
RUN tar -xvf samtools-0.1.18.tar.bz2; rm samtools-0.1.18.tar.bz2;cd samtools-0.1.18; make

#install srst2
RUN wget https://github.com/katholt/srst2/archive/v0.2.0.tar.gz
RUN tar -xzvf v0.2.0.tar.gz;rm v0.2.0.tar.gz;pip install /srst2-0.2.0

#install freebayes
RUN git clone --recursive https://github.com/ekg/freebayes.git
RUN cd freebayes/;git checkout v1.2.0;make; make install

#Add the spn scripts
RUN git clone https://github.com/BenJamesMetcalf/Spn_Scripts_Reference.git
ENV PATH="/Spn_Scripts_Reference:/samtools-0.1.18:${PATH}"\
 MODULESHOME="/usr/share/modules"
