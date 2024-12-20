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
LABEL maintainer.email="holly.halstead@doh.wa.gov"
LABEL maintainer2="Inês Mendes"
LABEL maintainer2.email="ines.mendes@theiagen.com"

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
locate \
python-pip \
python-setuptools && \
apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download samtools source code; unzip; compile; put executable in /usr/local/bin
RUN curl -O -L https://sourceforge.net/projects/samtools/files/samtools/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
rm samtools-${SAMTOOLS_VER}.tar.bz2 && \
cd samtools-${SAMTOOLS_VER} && \
make && \
cp -v samtools /usr/local/bin 

# Install SRST2; make /data
RUN pip install biopython git+https://github.com/katholt/srst2.git@v${SRST2_VER} && \
mkdir /data

# add custom database to /vibrio-cholerae-db directory, make readable to all
ADD vibrio_230224.fasta /vibrio-cholerae-db/

# index custom database in /vibrio-cholerae-db directory; ensure files are readable to all users
RUN bowtie2-build /vibrio-cholerae-db/vibrio_230224.fasta /vibrio-cholerae-db/vibrio_230224.fasta && \
  samtools faidx /vibrio-cholerae-db/vibrio_230224.fasta && \
  chmod -R 755 /vibrio-cholerae-db

# set final working directory
WORKDIR /data

# test layer
FROM app as test

# check help options
RUN srst2 --version && \
getmlst.py -h && \
slurm_srst2.py -h

# test getmlst.py script as well as usage of srst2 for calling the ST on a Shigella sonnei isolate
# https://www.ebi.ac.uk/ena/browser/view/ERR024070
RUN getmlst.py --species "Escherichia coli#1" && \
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR024/ERR024070/ERR024070_1.fastq.gz && \
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR024/ERR024070/ERR024070_2.fastq.gz && \
srst2 --input_pe ERR024070*.fastq.gz --output shigella1 --log --save_scores --mlst_db Escherichia_coli#1.fasta --mlst_definitions profiles_csv  --mlst_delimiter '_'  && \
ls shigella1__ERR024070.Escherichia_coli#1.pileup \
shigella1__ERR024070.Escherichia_coli#1.scores \
shigella1__ERR024070.Escherichia_coli#1.sorted.bam \
shigella1__mlst__Escherichia_coli#1__results.txt 

# test for vibrio custom DB, print output summary
# https://www.ebi.ac.uk/ena/browser/view/SRR7062495
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR706/005/SRR7062495/SRR7062495_1.fastq.gz && \
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR706/005/SRR7062495/SRR7062495_2.fastq.gz && \
srst2 --input_pe SRR7062495*.fastq.gz --gene_db /vibrio-cholerae-db/vibrio_230224.fasta --output SRR7062495 && \
ls SRR7062495__genes__vibrio_230224__results.txt && \
cat SRR7062495__genes__vibrio_230224__results.txt
