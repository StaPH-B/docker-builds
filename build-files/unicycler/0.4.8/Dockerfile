FROM ubuntu:xenial

# for easy upgrade later. ARG variables only persist during image build time
ARG unicyclerVer="0.4.8"
ARG blastVer="2.10.0"
ARG spadesVer="3.13.0"
ARG samtoolsVer="1.9"
ARG bcftoolsVer="1.9"
ARG raconVer="1.3.1"
ARG miniasmVer="0.3"

LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="Unicycler"
LABEL software.version="0.4.8"
LABEL description="Unicycler is an assembly pipeline for bacterial genomes."
LABEL website="https://github.com/rrwick/Unicycler"
LABEL license="https://github.com/rrwick/Unicycler#license"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install prerequisites including openjdk-11. Cleanup apt garbage
RUN apt-get update && apt-get install -y software-properties-common &&\
 add-apt-repository -y ppa:openjdk-r/ppa && apt-get update && apt-get install -y \
 python3 \
 python3-pip \
 libz-dev \
 bowtie2 \
 openjdk-11-jre \
 wget \
 bzip2 \
 libncurses5-dev \
 libncursesw5-dev \
 libbz2-dev \
 liblzma-dev \
 cmake && \
 rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get autoclean

# ncbi-blast+
# apt version of blast is very old (2.2.31)
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${blastVer}/ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-${blastVer}+-x64-linux.tar.gz && \
 rm ncbi-blast-${blastVer}+-x64-linux.tar.gz

# get unicycler
RUN wget https://github.com/rrwick/Unicycler/archive/v${unicyclerVer}.tar.gz && \
 mkdir unicycler && \
 tar -xzvf v${unicyclerVer}.tar.gz -C unicycler --strip-components 1 && \
 rm v${unicyclerVer}.tar.gz

# get pilon
RUN wget https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar -P /pilon

# get spades
RUN wget https://github.com/ablab/spades/releases/download/v3.13.0/SPAdes-${spadesVer}-Linux.tar.gz && \
 mkdir spades && \
 tar -xzvf SPAdes-${spadesVer}-Linux.tar.gz -C spades --strip-components 1 &&\
 rm SPAdes-${spadesVer}-Linux.tar.gz

# get samtools and bcftools
RUN wget https://github.com/samtools/samtools/releases/download/${samtoolsVer}/samtools-${samtoolsVer}.tar.bz2 && \
 wget https://github.com/samtools/bcftools/releases/download/${bcftoolsVer}/bcftools-${bcftoolsVer}.tar.bz2 && \
 mkdir samtools && \
 tar -vxjf samtools-${samtoolsVer}.tar.bz2 -C samtools --strip-components 1 && \
 rm samtools-${samtoolsVer}.tar.bz2 && \
 mkdir bcftools && \
 tar -vxjf bcftools-${bcftoolsVer}.tar.bz2 -C bcftools --strip-components 1 && \
 rm bcftools-${bcftoolsVer}.tar.bz2 && \
 cd samtools && \
 make && \
 make install && \
 cd ../bcftools && \
 make && \
 make install

# get racon
RUN wget https://github.com/isovic/racon/releases/download/${raconVer}/racon-v${raconVer}.tar.gz && \
 mkdir racon && \
 tar -xzvf racon-v${raconVer}.tar.gz -C racon --strip-components 1 && \
 rm racon-v${raconVer}.tar.gz && \
 cd racon && \
 mkdir build && \
 cd build && \
 cmake -DCMAKE_BUILD_TYPE=Release ../ && \
 make && \
 make install

# get miniasm
RUN wget https://github.com/lh3/miniasm/archive/v${miniasmVer}.tar.gz && \
 mkdir miniasm && \
 tar -xzvf v${miniasmVer}.tar.gz -C miniasm --strip-components 1 && \
 rm v${miniasmVer}.tar.gz && \
 cd miniasm && \
 make

# set PATH and LC_ALL for singularity compatibility
ENV PATH="/pilon:\
/spades/bin:\
/miniasm:\
/ncbi-blast-${blastVer}+/bin/:\
${PATH}"\
 LC_ALL=C

# build unicycler (which checks for dependencies) and create /data
RUN python3 /unicycler/setup.py install && \
 mkdir /data

# set working directory
WORKDIR /data
