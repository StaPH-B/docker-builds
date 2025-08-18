ARG SAMTOOLSVER=1.21
ARG HTSLIB_VER=${SAMTOOLSVER}
ARG IVARVER=1.4.4
ARG MINIMAP2_VER=2.30
ARG BWA_VER=0.7.19

FROM ubuntu:jammy AS builder

ARG SAMTOOLSVER
ARG HTSLIB_VER
ARG IVARVER
ARG MINIMAP2_VER
ARG BWA_VER

# installing htslib
RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  wget \
  ca-certificates \
  make \
  bzip2 \
  autoconf \
  automake \
  make \
  gcc \
  perl \
  zlib1g-dev \
  libbz2-dev \
  liblzma-dev \
  libcurl4-gnutls-dev \
  libssl-dev \
  libncurses5-dev \
  procps

# get htslib, compile, install, run test suite
RUN wget -q https://github.com/samtools/htslib/releases/download/${HTSLIB_VER}/htslib-${HTSLIB_VER}.tar.bz2 && \
    tar -vxjf htslib-${HTSLIB_VER}.tar.bz2 && \
    rm -v htslib-${HTSLIB_VER}.tar.bz2 && \
    cd htslib-${HTSLIB_VER} && \
    make && \
    make install && \
    make test

# download, compile, and install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLSVER}/samtools-${SAMTOOLSVER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLSVER}.tar.bz2 && \
  cd samtools-${SAMTOOLSVER} && \
  ./configure && \
  make && \
  make install && \
  make test
  
# install iVar
RUN wget -q https://github.com/andersen-lab/ivar/archive/v${IVARVER}.tar.gz && \
  tar -xf v${IVARVER}.tar.gz && \
  rm -rf v${IVARVER}.tar.gz && \
  cd ivar-${IVARVER} && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install

# install minimap2 binary
RUN wget --no-check-certificate https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 &&\
  tar --no-same-owner --strip-components=1 -C /usr/local/bin/ -jxvf minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2

#install bwa
RUN wget https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz &&\
    tar -xvf v${BWA_VER}.tar.gz &&\
    cd bwa-${BWA_VER} &&\
    make &&\
    mv bwa /usr/local/bin/

FROM ubuntu:jammy AS app

ARG IVARVER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="iVar"
LABEL software.version=${IVARVER}
LABEL description="Computational package that contains functions broadly useful for viral amplicon-based sequencing."
LABEL website="https://github.com/andersen-lab/ivar"
LABEL license="https://github.com/andersen-lab/ivar/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL modified.from="https://github.com/andersen-lab/ivar/blob/master/Dockerfile"
LABEL original.maintainer="Kathik G"
LABEL original.maintainer.email="gkarthik@scripps.edu"

# install dependencies, cleanup apt garbage.
RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  procps \
  libcurl3-gnutls && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/ /usr/local/lib/
COPY --from=builder /usr/local/include/ /usr/local/include/

WORKDIR /data

ENV LD_LIBRARY_PATH="/usr/local/lib"

CMD ["ivar", "help"]

FROM app AS test

WORKDIR /test

RUN ivar version && samtools --version && minimap2 --version

RUN apt-get update && apt-get install -y \
  wget \
  git

# getting files
RUN wget -q https://github.com/StaPH-B/docker-builds/blob/master/tests/SARS-CoV-2/SRR13957123.sorted.bam?raw=true -O SRR13957123.sorted.bam && \
  samtools view -s 0.25 -b SRR13957123.sorted.bam | samtools sort -o SRR13957123.subsampled.bam - && samtools index SRR13957123.subsampled.bam && \
  wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.reference.fasta -O MN908947.3.fasta && \
  wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.primer.bed && \
  wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_1.fastq.gz?raw=true -O SRR13957123_1.fastq.gz && \
  wget -q https://github.com/StaPH-B/docker-builds/blob/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_2.fastq.gz?raw=true -O SRR13957123_2.fastq.gz && \
  wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/943/119/195/GCA_943119195.1_2015LSAL00020/GCA_943119195.1_2015LSAL00020_genomic.fna.gz && \
  gzip -d GCA_943119195.1_2015LSAL00020_genomic.fna.gz && \
  wget -q https://zenodo.org/records/10733190/files/df_test_files.tar.gz && \
  tar -xvf df_test_files.tar.gz && \
  wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_1.fastq.gz -O r1.fq.gz && \ 
  wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_2.fastq.gz -O r2.fq.gz && \
  wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz && \
  gunzip -c GCF_000006945.2_ASM694v2_genomic.fna.gz > ref.fa

# primer trimming
RUN ivar trim -e -i SRR13957123.subsampled.bam -b nCoV-2019.primer.bed -p SRR13957123.primertrim && \
  samtools sort SRR13957123.primertrim.bam -o SRR13957123.primertrim.sorted.bam

# creating a consensus - using smaller -d for github actions
RUN samtools mpileup -A -d 40 -B -Q 0 --reference MN908947.3.fasta SRR13957123.primertrim.sorted.bam | \
  ivar consensus -q 20 -t 0.6 -n N -m 20 -p SRR13957123.consensus && \
  wc -c SRR13957123.consensus*

# align with minimap2
RUN minimap2 -x lr:hq -a GCA_943119195.1_2015LSAL00020_genomic.fna test_files/test.fastq.gz > lrhq_test.sam

# align with bwa
RUN bwa index ref.fa && \
  bwa mem ref.fa r1.fq.gz r2.fq.gz > aln.sam && \
  head aln.sam