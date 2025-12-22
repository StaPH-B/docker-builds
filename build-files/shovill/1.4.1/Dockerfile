# versions were checked against this conda yml that is provided w shovill code: https://github.com/tseemann/shovill/blob/master/environment.yml
ARG SHOVILL_VER="1.4.1"
ARG SPADES_VER="3.15.5"
# just guessing on seqkit version as this is not pinned
ARG SEQKIT_VER="2.12.0"
# guessing again for kmc since its not pinned, just 3.2 or higher
ARG KMC_VER="3.2.4"
ARG LIGHTER_VER="1.1.1"
ARG TRIMMOMATIC_VER="0.39"
ARG BWA_VER="0.7.17"
# not sure if a more recent samtools is compatible or not, conda yml says higher than 1.10
ARG SAMTOOLS_VER="1.16.1"
# SKESA needs to be 2.5 or higher
# Opting not to use SKESA_VER since the binaries on Github change names frequently and are not versioned well
#ARG SKESA_VER="2.5"
# megahit needs to be 1.2.9 or higher
ARG MEGAHIT_VER="1.1.4"
ARG VELVET_VER="1.2.10"
ARG FLASH_VER="1.2.11"
# also not sure if this upgraded pilon version is compatible, previously used 1.22
ARG PILON_VER="1.24"

FROM ubuntu:jammy AS builder

# a lot of the builder stage code is from samtools 1.22.1 dockerfile
ARG SAMTOOLS_VER

RUN apt-get update && apt-get install --no-install-recommends -y \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    zlib1g-dev \
    libssl-dev \
    libdeflate-dev \
    gcc \
    wget \
    make \
    perl \
    bzip2 \
    gnuplot \
    ca-certificates

# download, compile, and install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
    tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
    cd samtools-${SAMTOOLS_VER} && \
    ./configure && \
    make && \
    make install && \
    make test


# just praying that jammy will work
FROM ubuntu:jammy AS app

# reinstantiating variables so they are available in app FROM layer
ARG SHOVILL_VER
ARG SPADES_VER
ARG SEQKIT_VER
ARG KMC_VER
ARG LIGHTER_VER
ARG TRIMMOMATIC_VER
ARG BWA_VER
ARG SAMTOOLS_VER
ARG SKESA_VER
ARG MEGAHIT_VER
ARG VELVET_VER
ARG FLASH_VER
ARG PILON_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Shovill"
LABEL software.version="${SHOVILL_VER}"
LABEL description="faster than SPAdes de novo DBG genome assembler (with assembler options!)"
LABEL website="https://github.com/tseemann/shovill"
LABEL lisence="https://github.com/tseemann/shovill/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies, cleanup apt garbage
# TODO - check if any can be removed after install (like gcc, g++, make, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
python3 \
wget \
ca-certificates \
pigz \
zlib1g-dev \
make \
gcc \
g++ \
libpthread-stubs0-dev \
openjdk-25-jre-headless \
unzip \
bzip2 \
libncurses5-dev \
libbz2-dev \
liblzma-dev \
libcurl4-gnutls-dev \
libssl-dev \
libfindbin-libs-perl && \
apt-get clean && apt-get autoclean && \
rm -rfv /var/lib/apt/lists/*

# SPAdes
RUN echo "Downloading SPAdes version ${SPADES_VER} linux binaries..." && \
wget -q https://github.com/ablab/spades/releases/download/v${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
rm -v SPAdes-${SPADES_VER}-Linux.tar.gz

# seqkit install
RUN echo "Installing seqkit version ${SEQKIT_VER}..." && \
wget -q https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VER}/seqkit_linux_amd64.tar.gz && \
tar -zxf seqkit_linux_amd64.tar.gz && \
rm -v seqkit_linux_amd64.tar.gz && \
mv -v seqkit /usr/local/bin/seqkit

# kmc
RUN echo "Installing KMC version ${KMC_VER}..." && \
mkdir kmc && \
cd kmc && \
wget https://github.com/refresh-bio/KMC/releases/download/v${KMC_VER}/KMC${KMC_VER}.linux.x64.tar.gz && \
tar -xzf KMC${KMC_VER}.linux.x64.tar.gz && \
rm -v KMC${KMC_VER}.linux.x64.tar.gz  

# lighter
RUN wget https://github.com/mourisl/Lighter/archive/v${LIGHTER_VER}.tar.gz && \
tar -zxf v${LIGHTER_VER}.tar.gz && \
rm -rvf v${LIGHTER_VER}.tar.gz && \
cd Lighter-${LIGHTER_VER} && \
make

# trimmomatic
RUN echo "Installing Trimmomatic version ${TRIMMOMATIC_VER}..." && \
mkdir trimmomatic && \
cd trimmomatic && \
wget -q http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-${TRIMMOMATIC_VER}.zip && \
unzip Trimmomatic-${TRIMMOMATIC_VER}.zip && \
rm -rfv Trimmomatic-${TRIMMOMATIC_VER}.zip && \
chmod +x Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar && \
echo "#!/bin/bash" >> trimmomatic && \
echo "exec java -jar /trimmomatic/Trimmomatic-${TRIMMOMATIC_VER}/trimmomatic-${TRIMMOMATIC_VER}.jar """"$""@"""" " >> trimmomatic && \
chmod +x trimmomatic

# bwa (mem) install
# TODO - move to builder stage
RUN echo "Installing BWA version ${BWA_VER}..." && \
mkdir bwa && \
cd bwa && \
wget -q https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 && \
tar -xjf bwa-${BWA_VER}.tar.bz2 && \
rm -v bwa-${BWA_VER}.tar.bz2 && \
cd bwa-${BWA_VER} && \
make

# samtools install
# TODO - look at samtools 1.23 dockerfile to see if any optimizations can be made here, additional dependencies etc
# copy in samtools executables from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/
RUN echo "Last step copied in samtools from builder stage. Here is contents of /usr/local/bin/:" && \
ls -lah /usr/local/bin/

# skesa 2.3.0 binary (skesa 2.4.0 binary works better on ubuntu:bionic, so not upgrading here)
# This installs SKESA v2.5.1 binary. Version in CPP code does not match Github release version tag. https://github.com/ncbi/SKESA/blob/skesa.2.4.0_saute.1.3.0_2/skesa.cpp#L397
RUN echo "Installing SKESA version 2.5.1..." && \
mkdir skesa && \
cd skesa && \
wget -q https://github.com/ncbi/SKESA/releases/download/skesa.2.4.0_saute.1.3.0_2/skesa.centos.7.9.2009 && \
mv -v skesa.centos.7.9.2009 skesa && \
chmod +x skesa

# MEGAHIT 1.1.4 binary (I'm pretty sure these are binaries at this point)
RUN echo "Installing MEGAHIT version ${MEGAHIT_VER}..." && \
mkdir megahit && \
cd megahit && \
wget -q https://github.com/voutcn/megahit/releases/download/v${MEGAHIT_VER}/megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin.tar.gz && \
tar -xzf megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin.tar.gz && \
rm -v megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin.tar.gz

# Velvet 1.2.10
RUN echo "Installing VELVET version ${VELVET_VER}..." && \
mkdir velvet && \
cd velvet && \
wget -q https://github.com/dzerbino/velvet/archive/v${VELVET_VER}.tar.gz && \
tar -xzf v${VELVET_VER}.tar.gz && \
rm -vrf v${VELVET_VER}.tar.gz && \
cd velvet-${VELVET_VER} && \
make

# Flash 1.2.11
RUN echo "Installing FLASH version ${FLASH_VER}..." && \
mkdir flash && \
cd flash && \
wget -q https://sourceforge.net/projects/flashpage/files/FLASH-${FLASH_VER}.tar.gz && \
tar -zxf FLASH-${FLASH_VER}.tar.gz && \
rm -vrf FLASH-${FLASH_VER}.tar.gz && \
cd FLASH-${FLASH_VER} && \
make

# pilon
RUN echo "Installing pilon version ${PILON_VER}..." && \
mkdir pilon && \
cd pilon && \
wget -q https://github.com/broadinstitute/pilon/releases/download/v${PILON_VER}/pilon-${PILON_VER}.jar && \
chmod +x pilon-${PILON_VER}.jar && \
echo "#!/bin/bash" >> pilon && \
echo "exec java -jar /pilon/pilon-${PILON_VER}.jar """"$""@"""" " >> pilon && \
chmod +x pilon

# Samclip (not going to pin a version, this is the recommended way of installing and there have not been updates since March 2020)
RUN echo "Installing samclip..." && \
mkdir samclip && \
cd samclip && \
wget -q https://raw.githubusercontent.com/tseemann/samclip/master/samclip && \
chmod +x samclip

# aaannnddd finally install shovill itself
# extra perl module I had to install via apt-get: libfindbin-libs-perl
# create /data for working directory
RUN echo "Installing shovill version ${SHOVILL_VER}..." && \
wget -q https://github.com/tseemann/shovill/archive/v${SHOVILL_VER}.tar.gz && \
tar -xzf v${SHOVILL_VER}.tar.gz && \
rm -v v${SHOVILL_VER}.tar.gz && \
mkdir /data

# set /data as final working directory
WORKDIR /data

# set $PATH's
ENV PATH="${PATH}:\
/SPAdes-${SPADES_VER}-Linux/bin:\
/kmc:\
/Lighter-${LIGHTER_VER}:\
/trimmomatic:\
/bwa/bwa-${BWA_VER}:\
/skesa:\
/megahit/megahit_v${MEGAHIT_VER}_LINUX_CPUONLY_x86_64-bin:\
/velvet/velvet-${VELVET_VER}:\
/flash/FLASH-${FLASH_VER}:\
/shovill-${SHOVILL_VER}/bin:\
/pilon:\
/samclip" \
LC_ALL=C

# test layer
FROM app AS test

# reinstantiating variable so it's available for cd cmd below
ARG SHOVILL_VER

# so that the below commands are run with /bin/bash shell and not /bin/sh - needed for bash-specific tricks below
SHELL ["/bin/bash", "-c"]

# test shamelessly stolen & modified from this originally: https://github.com/tseemann/shovill/blob/master/.travis.yml
# TODO - update with v1.4.1 test commands from: https://github.com/tseemann/shovill/blob/master/.github/workflows/CI.yml
RUN cd /shovill-${SHOVILL_VER}/ && \
kmc && \
skesa --version && \
! shovill --doesnotexist && \
echo "TESTING SHOVILL + SPADES" && \
shovill --cpus $(nproc) --outdir out.spades --assembler spades --R1 test/R1.fq.gz --R2 test/R2.fq.gz --nostitch --noreadcorr --nocorr && \
grep '>' out.spades/contigs.fa && \
echo "TESTING SHOVILL + MEGAHIT" && \
shovill --cpus $(nproc) --outdir out.megahit --assembler megahit --R1 test/R1.fq.gz --R2 test/R2.fq.gz --trim && \
grep '>' out.megahit/contigs.fa && \
echo "TESTING SHOVILL + VELVET" && \
shovill --cpus $(nproc) --outdir out.velvet --assembler velvet --R1 test/R1.fq.gz --R2 test/R2.fq.gz --ram 4 --noreadcorr --nocorr && \
grep '>' out.velvet/contigs.fa && \
echo "TESTING SHOVILL + SKESA" && \
shovill --cpus $(nproc) --outdir out.skesa --assembler skesa --R1 test/R1.fq.gz --R2 test/R2.fq.gz --ram 4 --noreadcorr --nocorr && \
grep '>' out.velvet/contigs.fa

RUN shovill --help && shovill --check && shovill --version