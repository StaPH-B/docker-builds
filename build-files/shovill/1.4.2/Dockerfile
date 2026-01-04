### versions were checked against this conda yml that is provided w shovill code: https://github.com/tseemann/shovill/blob/master/environment.yml
ARG SHOVILL_VER="1.4.2"
# previously used bwa 0.7.17, needs to be 0.7.17 or higher
ARG BWA_VER="0.7.19"
# csvtk version not specified in conda yml, so going with most recent release as of Dec 2025
ARG CSVTK_VER="0.36.0"
# flash should be 1.2 or higher
ARG FLASH_VER="1.2.11"
# guessing again for kmc since its not pinned, just 3.2 or higher
ARG KMC_VER="3.2.4"
# should be 1.1 or higher
ARG LIGHTER_VER="1.1.3"
# megahit needs to be 1.2.9 or higher
ARG MEGAHIT_VER="1.2.9"
# not sure if this upgraded pilon version is compatible, previously used 1.22. Should be 1.22 or higher
ARG PILON_VER="1.24"
# not sure if a more recent samtools is compatible or not, conda yml says higher than 1.10, sticking with 1.16.1 since it worked previously
ARG SAMTOOLS_VER="1.16.1"
# just guessing on seqkit version as this is not pinned
ARG SEQKIT_VER="2.12.0"
# SKESA needs to be 2.5 or higher
# Opting not to use SKESA_VER since the binaries on Github change names frequently and are not versioned well
# spades should be 3.11 or higher, but less than 4.0.0
ARG SPADES_VER="3.15.5"
# should be 0.36 or higher
ARG TRIMMOMATIC_VER="0.40"
# should be 1.2.10 or higher
ARG VELVET_VER="1.2.10"

### BUILDER STAGE ###
FROM ubuntu:jammy AS builder

# a lot of the builder stage code is from samtools 1.22.1 dockerfile
ARG BWA_VER
ARG CSVTK_VER
ARG FLASH_VER
ARG MEGAHIT_VER
ARG LIGHTER_VER
ARG PILON_VER
ARG SAMTOOLS_VER
ARG SEQKIT_VER
ARG SPADES_VER
ARG TRIMMOMATIC_VER
ARG VELVET_VER

# install dependencies required for compiling various tools
# requirements for spades: cmake, build-essential
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
cmake \
build-essential \
perl \
bzip2 \
gnuplot \
ca-certificates \
unzip

# bwa
RUN echo "Installing BWA version ${BWA_VER}..." && \
wget -q https://github.com/lh3/bwa/archive/refs/tags/v${BWA_VER}.tar.gz && \
tar -xzf v${BWA_VER}.tar.gz && \
rm -v v${BWA_VER}.tar.gz && \
cd bwa-${BWA_VER} && \
make && \
mv -v bwa /usr/local/bin/bwa

# csvtk
RUN echo "Installing csvtk version ${CSVTK_VER}..." && \
wget -q https://github.com/shenwei356/csvtk/releases/download/v${CSVTK_VER}/csvtk_linux_amd64.tar.gz && \
tar -zxf csvtk_linux_amd64.tar.gz && \
rm -v csvtk_linux_amd64.tar.gz && \
mv -v csvtk /usr/local/bin/csvtk

# Flash
RUN echo "Installing FLASH version ${FLASH_VER}..." && \
wget -q https://sourceforge.net/projects/flashpage/files/FLASH-${FLASH_VER}.tar.gz && \
tar -zxf FLASH-${FLASH_VER}.tar.gz && \
rm -vrf FLASH-${FLASH_VER}.tar.gz && \
cd FLASH-${FLASH_VER} && \
make && \
mv -v flash /usr/local/bin/flash

# Lighter
RUN echo "Installing Lighter version ${LIGHTER_VER}..." && \
wget -q https://github.com/mourisl/Lighter/archive/v${LIGHTER_VER}.tar.gz && \
tar -zxf v${LIGHTER_VER}.tar.gz && \
rm -rvf v${LIGHTER_VER}.tar.gz && \
cd Lighter-${LIGHTER_VER} && \
make && \
mv -v lighter /usr/local/bin/lighter

# MEGAHIT
RUN echo "Installing MEGAHIT version ${MEGAHIT_VER}..." && \
wget -q https://github.com/voutcn/megahit/releases/download/v${MEGAHIT_VER}/MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static.tar.gz && \
tar -xzf MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static.tar.gz && \
rm -v MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static.tar.gz && \
mv -v MEGAHIT-${MEGAHIT_VER}-Linux-x86_64-static/bin/* /usr/local/bin/ && \
chmod -v +x /usr/local/bin/megahit

# pilon
# put both the .jar and the wrapper bash script in /usr/local/bin/
RUN echo "Installing pilon version ${PILON_VER}..." && \
wget -q https://github.com/broadinstitute/pilon/releases/download/v${PILON_VER}/pilon-${PILON_VER}.jar && \
chmod -v +x pilon-${PILON_VER}.jar && \
mv -v pilon-${PILON_VER}.jar /usr/local/bin/pilon-${PILON_VER}.jar && \
echo "#!/bin/bash" >> /usr/local/bin/pilon && \
echo "exec java -jar /usr/local/bin/pilon-${PILON_VER}.jar """"$""@"""" " >> /usr/local/bin/pilon && \
chmod -v +x /usr/local/bin/pilon

# Samclip (not going to pin a version, this is the recommended way of installing and there have not been updates since March 2020)
RUN echo "Installing samclip..." && \
wget -q https://raw.githubusercontent.com/tseemann/samclip/master/samclip && \
mv -v samclip /usr/local/bin/samclip && \
chmod -v +x /usr/local/bin/samclip

# download, compile, and install samtools
RUN echo "Installing SAMtools version ${SAMTOOLS_VER}..." && \
wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
cd samtools-${SAMTOOLS_VER} && \
./configure && \
make && \
make install && \
make test

# seqkit
RUN echo "Installing seqkit version ${SEQKIT_VER}..." && \
wget -q https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VER}/seqkit_linux_amd64.tar.gz && \
tar -zxf seqkit_linux_amd64.tar.gz && \
rm -v seqkit_linux_amd64.tar.gz && \
mv -v seqkit /usr/local/bin/seqkit

# skesa
# This installs SKESA v2.5.1 binary. Version in CPP code does not match Github release version tag. https://github.com/ncbi/SKESA/blob/skesa.2.4.0_saute.1.3.0_2/skesa.cpp#L397
RUN echo "Installing SKESA version 2.5.1 and gfa_connector..." && \
wget -q https://github.com/ncbi/SKESA/releases/download/skesa.2.4.0_saute.1.3.0_2/skesa.centos.7.9.2009 && \
wget -q https://github.com/ncbi/SKESA/releases/download/skesa.2.4.0_saute.1.3.0_2/gfa_connector.centos.7.9.2009 && \
mv -v gfa_connector.centos.7.9.2009 /usr/local/bin/gfa_connector && \
mv -v skesa.centos.7.9.2009 /usr/local/bin/skesa && \
chmod -v +x /usr/local/bin/skesa /usr/local/bin/gfa_connector

# SPAdes install from source and compile
# This route of installation takes longer but at least SPAdes runs successfully. Apparently there are some issues with pre-compiled binaries and the "OS: -11 spades-hammer" error I was receiving is a sign of this known issue.
RUN echo "Installing SPAdes version ${SPADES_VER} from source..." && \
wget -q https://github.com/ablab/spades/archive/refs/tags/v${SPADES_VER}.tar.gz && \
tar -xzf v${SPADES_VER}.tar.gz && \
rm -v v${SPADES_VER}.tar.gz && \
cd spades-${SPADES_VER}/assembler && \
PREFIX=/usr/local ./spades_compile.sh

# trimmomatic install
# put both the .jar and the wrapper bash script in /usr/local/bin/
RUN echo "Installing Trimmomatic version ${TRIMMOMATIC_VER}..." && \
wget -q https://github.com/usadellab/Trimmomatic/releases/download/v${TRIMMOMATIC_VER}/Trimmomatic-${TRIMMOMATIC_VER}.zip && \
unzip Trimmomatic-${TRIMMOMATIC_VER}.zip && \
rm -fv Trimmomatic-${TRIMMOMATIC_VER}.zip && \
chmod -v +x trimmomatic-${TRIMMOMATIC_VER}.jar && \
mv -v trimmomatic-${TRIMMOMATIC_VER}.jar /usr/local/bin/ && \
echo "#!/bin/bash" >> trimmomatic && \
echo "exec java -jar /usr/local/bin/trimmomatic-${TRIMMOMATIC_VER}.jar """"$""@"""" " >> /usr/local/bin/trimmomatic && \
chmod -v +x /usr/local/bin/trimmomatic

# Velvet
RUN echo "Installing VELVET version ${VELVET_VER}..." && \
wget -q https://github.com/dzerbino/velvet/archive/v${VELVET_VER}.tar.gz && \
tar -xzf v${VELVET_VER}.tar.gz && \
rm -vrf v${VELVET_VER}.tar.gz && \
cd velvet-${VELVET_VER} && \
make && \
mv -v velveth /usr/local/bin/velveth && \
mv -v velvetg /usr/local/bin/velvetg

### APP STAGE ###
FROM ubuntu:jammy AS app

# reinstantiating variables so they are available in app stage
ARG KMC_VER
ARG SHOVILL_VER

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
# required for samtools: libdeflate-dev, zlib1g, libncurses5, bzip2, liblzma5, libcurl3-gnutls (trying with libcurl4-gnutls), gnuplot
# Needed for spades.py: update-alternatives (for python3), python3-distutils, cmake, libgomp1 (blast also requires this)
# Needed perl module for shovill: libfindbin-libs-perl
RUN apt-get update && apt-get install -y --no-install-recommends \
python3 \
python3-distutils \
libgomp1 \
wget \
ca-certificates \
zlib1g \
libpthread-stubs0-dev \
openjdk-25-jre-headless \
bzip2 \
libncurses5 \
libbz2-dev \
liblzma5 \
libcurl4-gnutls-dev \
libssl-dev \
libfindbin-libs-perl \
libdeflate-dev \
gnuplot && \
apt-get clean && apt-get autoclean && \
rm -rfv /var/lib/apt/lists/* && \
update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# kmc
RUN echo "Installing KMC version ${KMC_VER}..." && \
mkdir kmc && \
cd kmc && \
wget -q https://github.com/refresh-bio/KMC/releases/download/v${KMC_VER}/KMC${KMC_VER}.linux.x64.tar.gz && \
tar -xzf KMC${KMC_VER}.linux.x64.tar.gz && \
rm -v KMC${KMC_VER}.linux.x64.tar.gz && \
echo "Contents of /kmc/bin:" && \
ls -lah /kmc/bin

# copy in bwa, csvtk, flash, lighter, MEGAHIT, pilon, samclip, samtools, seqkit, skesa, spades, trimmomatic, and velvet executables into app stage from builder stage
COPY --from=builder /usr/local/bin/* /usr/local/bin/

# copy over stuff from /usr/local/share/spades/ in builder stage to here so "spades.py --version" works
COPY --from=builder /usr/local/share/spades/ /usr/local/share/spades/

# aaannnddd finally install Shovill itself
# create /data for working directory
RUN echo "Installing shovill version ${SHOVILL_VER}..." && \
wget -q https://github.com/tseemann/shovill/archive/v${SHOVILL_VER}.tar.gz && \
tar -xzf v${SHOVILL_VER}.tar.gz && \
rm -v v${SHOVILL_VER}.tar.gz && \
mkdir /data

# set /data as final working directory
WORKDIR /data

# set $PATH's and LC_ALL for singularity compatibility
# most installed programs are in /usr/local/bin which is already in $PATH
ENV PATH="${PATH}:\
/kmc/bin:\
/shovill-${SHOVILL_VER}/bin" \
LC_ALL=C

# set default command to show shovill help options
CMD ["shovill", "--help"]

### TEST STAGE ###
FROM app AS test

# reinstantiating variable so it's available for cd cmd below
ARG SHOVILL_VER

# so that the below commands are run with /bin/bash shell and not /bin/sh - needed for bash-specific tricks below
SHELL ["/bin/bash", "-c"]

# the free github actions runners should have 16 GB, so leaving some overhead
# shovill seems to behave with max number of CPUs available as long as RAM is limited (mainly used for java-based programs like pilon and trimmomatic)
ARG RAM=14

# test shamelessly stolen & modified from: https://github.com/tseemann/shovill/blob/master/.github/workflows/CI.yml
RUN set -eu && \
echo "Testing shovill installation..." && \
cd /shovill-${SHOVILL_VER}/ && \
! shovill --doesnotexist && \
SHOVILL="shovill --ram ${RAM} --cpus $(nproc) --R1 test/R1.fq.gz --R2 test/R2.fq.gz" && \
for ASM in spades skesa megahit velvet ; do echo "TESTING SHOVILL + ${ASM}..."; ${SHOVILL} --outdir ${ASM} --assembler ${ASM} ; seqkit stats $ASM/contigs.fa; done

# test SKESA options combos
# these bash for loops are WILD!
RUN set -eu && \
echo "Testing shovill + SKESA options combinations..." && \
cd /shovill-${SHOVILL_VER}/ && \
SHOVILL="shovill --ram ${RAM} --cpus $(nproc) --R1 test/R1.fq.gz --R2 test/R2.fq.gz --assembler skesa --kmer 41" && \
DIR=1 && \
for TRIM in '' '--trim' ; do for RCORR in '' '--noreadcorr' ; do for STITCH in '' '--nostitch' ; do for ACORR in '' '--nocorr' ; do echo "Testing SKESA cmd and options: ${SHOVILL} --outdir ${DIR} ${TRIM} ${RCORR} ${STITCH} ${ACORR}"; ${SHOVILL} --outdir ${DIR} ${TRIM} ${RCORR} ${STITCH} ${ACORR}; echo; echo "Here's seqkit stats on the output assembly:"; seqkit stats ${DIR}/contigs.fa; echo; ((DIR++)) ; done; done; done; done

# Check final assembly stats
RUN cd /shovill-${SHOVILL_VER}/ && \
for FASTA in */contigs.fa ; do echo "Running seqkit stats ${FASTA}..."; seqkit stats ${FASTA}; done && \
grep -F 'size was' */shovill.log && \
shovill --version
