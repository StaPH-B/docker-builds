FROM mambaorg/micromamba:0.27.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
ARG MYKROBE_VER="0.12.1"
ARG SONNEITYPING_VER="20210201"
# see below for why we aren't using this. Keeping as a comment for when we can switch to versioned releases
#ARG GENOTYPHI_VER="1.9.1"

# metadata labels
LABEL base.image="mambaorg/micromamba:0.27.0"
LABEL dockerfile.version="1"
LABEL software="Mykrobe & Genotyphi & Sonneityping"
LABEL software.version=${MYKROBE_VER}
LABEL description="Conda environment for Mykrobe, particularly for Genotyphi"
LABEL website1="https://github.com/Mykrobe-tools/mykrobe"
LABEL license1="MIT"
LABEL license1.url="https://github.com/Mykrobe-tools/mykrobe/blob/master/LICENSE"
LABEL website2="https://github.com/katholt/genotyphi"
LABEL license2="GNU General Public License v3.0"
LABEL license2.url="https://github.com/katholt/genotyphi/blob/main/LICENSE"
LABEL website3="https://github.com/katholt/sonneityping/"
LABEL license3="GNU General Public License v3.0"
LABEL license3.url="https://github.com/katholt/sonneityping/blob/master/LICENSE.txt"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 git \
 procps \
 jq && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the genotyphi code; make /data
# cloning this commit: 98a6e9ccdf069bb86fcf41035b8c5fa92952aa9e
# url: https://github.com/katholt/genotyphi/commit/98a6e9ccdf069bb86fcf41035b8c5fa92952aa9e
# because genotyphi v1.9.1 does NOT include parse_typhi_mykrobe.py script for parsing mykrobe results
RUN git clone https://github.com/katholt/genotyphi.git && \
 cd genotyphi && \
 git checkout 98a6e9ccdf069bb86fcf41035b8c5fa92952aa9e && \
 chmod +x /genotyphi/parse_typhi_mykrobe.py && \
 mkdir -v /data

# Get the sonneityping code
RUN wget https://github.com/katholt/sonneityping/archive/refs/tags/v${SONNEITYPING_VER}.tar.gz && \
 tar -xzf v${SONNEITYPING_VER}.tar.gz && \
 rm -vf v${SONNEITYPING_VER}.tar.gz && \
 mv -v sonneityping-${SONNEITYPING_VER}/ /sonneityping/ && \
 chmod +x /sonneityping/parse_mykrobe_predict.py

# set the PATH and LC_ALL for singularity compatibility
ENV PATH="${PATH}:/opt/conda/envs/mykrobe/bin/:/genotyphi:/sonneityping" \
 LC_ALL=C.UTF-8

# create the conda environment, install mykrobe via bioconda package; cleanup conda garbage
# INSTALL PANDAS HERE INSTEAD
RUN micromamba create -n mykrobe -y -c conda-forge -c bioconda -c defaults \
 mykrobe=${MYKROBE_VER} \
 python \ 
 pip \
 pandas && \
 micromamba clean -a -y

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="mykrobe"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# get the latest databases (AKA "panels")
RUN mykrobe panels update_metadata && \
 mykrobe panels update_species all && \
 mykrobe panels describe

WORKDIR /data

# new base for testing
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="mykrobe"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# test with TB FASTQs
RUN wget -O test_reads.fq.gz https://ndownloader.figshare.com/files/21059229 && \
 mykrobe predict -s SAMPLE -S tb -o out.json --format json -i test_reads.fq.gz && \
 cat out.json && \
 mykrobe panels describe && \
 mykrobe --version

 ### OUTPUT FROM mykrobe panels describe run on 2022-11-01: ###
# Species summary:

# Species Update_available        Installed_version       Installed_url   Latest_version  Latest_url
# sonnei  no      20210201        https://ndownloader.figshare.com/files/26274424 20210201        https://ndownloader.figshare.com/files/26274424
# staph   no      20201001        https://ndownloader.figshare.com/files/24914930 20201001        https://ndownloader.figshare.com/files/24914930
# tb      no      20201014        https://ndownloader.figshare.com/files/25103438 20201014        https://ndownloader.figshare.com/files/25103438
# typhi   no      20210323        https://ndownloader.figshare.com/files/28533549 20210323        https://ndownloader.figshare.com/files/28533549

# sonnei default panel: 20210201
# sonnei panels:
# Panel   Reference       Description
# 20201012        NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC
# 20210201        NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC (same as 20201012, but with lineage3.7.30 added)

# staph default panel: 20170217
# staph panels:
# Panel   Reference       Description
# 20170217        BX571856.1      AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)

# tb default panel: 202010
# tb panels:
# Panel   Reference       Description
# 201901  NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), and second line drugs from Walker 2015 panel
# 202010  NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), second line drugs from Walker 2015 panel, and lineage scheme from Chiner-Oms 2020
# bradley-2015    NC_000962.3     AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
# walker-2015     NC_000962.3     AMR panel described in Walker, Timothy M et al. Whole-genome sequencing for prediction of Mycobacterium tuberculosis drug susceptibility and resistance: a retrospective cohort study. The Lancet Infectious Diseases , Volume 15 , Issue 10 , 1193 - 1202

# typhi default panel: 20210323
# typhi panels:
# Panel   Reference       Description
# 20210323        AL513382.1      GenoTyphi genotyping scheme and AMR calling using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766)