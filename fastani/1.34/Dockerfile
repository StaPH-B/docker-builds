FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist at build time
ARG FASTANI_VER="v1.34"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="FastANI"
LABEL software.version=${FASTANI_VER}
LABEL description="Fast alignment-free computation of whole-genome Average Nucleotide Identity"
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL license="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Kutluhan Incekara"
LABEL maintainer3.email="kutluhan.incekara@ct.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
 wget \
 unzip \
 libgomp1 && \
 apt-get clean && rm -rf /var/lib/apt/lists/*

# download pre-compiled binary; unzip; put binary in /usr/local/bin
# apt dependencies: libgomp1 unzip wget
RUN wget --no-check-certificate https://github.com/ParBLiSS/FastANI/releases/download/${FASTANI_VER}/fastANI-Linux64-${FASTANI_VER}.zip && \
 unzip fastANI-Linux64-${FASTANI_VER}.zip -d /usr/local/bin && \
 rm fastANI-Linux64-${FASTANI_VER}.zip
 
# default run command
CMD fastANI -h

# singularity compatibility
ENV LC_ALL=C

# set working directory
WORKDIR /data

## Test ##
FROM app as test

# download 2 genomes from fastANI GitHub; compare the 2; cat the output file
RUN wget --no-check-certificate -P /data https://github.com/ParBLiSS/FastANI/raw/master/tests/data/Escherichia_coli_str_K12_MG1655.fna && \
 wget --no-check-certificate -P /data https://github.com/ParBLiSS/FastANI/raw/master/tests/data/Shigella_flexneri_2a_01.fna && \
 fastANI -q /data/Shigella_flexneri_2a_01.fna -r /data/Escherichia_coli_str_K12_MG1655.fna -o /data/fastANI-test-ShiglellaFlexneri-EcoliK12.tsv && \
 echo "output TSV from fastANI test:" && \
 cat fastANI-test-ShiglellaFlexneri-EcoliK12.tsv

