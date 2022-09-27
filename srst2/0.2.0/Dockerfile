FROM ubuntu:xenial as app

# for easy upgrade later. ARG variables only persist at build time
# Main package version
ARG SRST2_VER=0.2.0

# Dependency versions
ARG BOWTIE2_VER=2.2.6-2
ARG SAMTOOLS_VER=0.1.18



LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="SRST2"
LABEL software.version="v0.2.0"
LABEL description="Short Read Sequence Typing for Bacterial Pathogens"
LABEL website="https://github.com/katholt/srst2"
LABEL license="https://github.com/katholt/srst2/blob/master/LICENSE.txt"
LABEL maintainer="Holly Halstead"
LABEL maintainer1.email="holly.halstead@doh.wa.gov"


# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
python2.7 \
python-scipy \
python-biopython \
make \
libc6-dev \
g++ \
zlib1g-dev \
build-essential \
git \
libx11-dev \
xutils-dev \
zlib1g-dev \
bowtie2=${BOWTIE2_VER} \
curl \
libncurses5-dev \
unzip \
wget  \
locate && \
apt-get install -y \
python-pip && \
apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download pre-compiled binary; unzip; put binary in /usr/bin; make /data
RUN curl -O -L https://sourceforge.net/projects/samtools/files/samtools/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
tar xvfj samtools-${SAMTOOLS_VER}.tar.bz2 && \
cd samtools-${SAMTOOLS_VER} && \
make && \
cp samtools /usr/local/bin && \
cd

# Install SRST2
RUN pip install biopython git+https://github.com/katholt/srst2.git@v${SRST2_VER} && \
mkdir /data

# set working directory
WORKDIR /data

FROM app as test

RUN srst2 --version && \
getmlst.py -h && \
slurm_srst2.py -h

RUN getmlst.py --species "Escherichia coli#1" && \
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR024/ERR024070/ERR024070_1.fastq.gz && \
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR024/ERR024070/ERR024070_2.fastq.gz && \
srst2 --input_pe ERR024070*.fastq.gz --output shigella1 --log --save_scores --mlst_db Escherichia_coli#1.fasta --mlst_definitions profiles_csv  --mlst_delimiter '_'  && \
ls shigella1__ERR024070.Escherichia_coli#1.pileup \
shigella1__ERR024070.Escherichia_coli#1.scores \
shigella1__ERR024070.Escherichia_coli#1.sorted.bam \
shigella1__mlst__Escherichia_coli#1__results.txt \
