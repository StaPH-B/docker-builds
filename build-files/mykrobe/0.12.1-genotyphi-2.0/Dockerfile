FROM mambaorg/micromamba:1.4.1 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
ARG MYKROBE_VER="0.12.1"
ARG SONNEITYPING_VER="20210201"
ARG GENOTYPHI_VER="2.0"

# metadata labels
LABEL base.image="mambaorg/micromamba:1.4.1"
LABEL dockerfile.version="1"
LABEL software="Mykrobe & Genotyphi & Sonneityping"
LABEL software.version="${MYKROBE_VER}"
LABEL description="Conda environment for Mykrobe, particularly for Genotyphi & Sonneityping"
LABEL website="https://github.com/Mykrobe-tools/mykrobe"
LABEL license1="MIT"
LABEL license1.url="https://github.com/Mykrobe-tools/mykrobe/blob/master/LICENSE"
LABEL website2="https://github.com/katholt/genotyphi"
LABEL license2="GNU General Public License v3.0"
LABEL license2.url="https://github.com/katholt/genotyphi/blob/main/LICENSE"
LABEL website3="https://github.com/katholt/sonneityping/"
LABEL license3="GNU General Public License v3.0"
LABEL license3.url="https://github.com/katholt/sonneityping/blob/master/LICENSE.txt"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps \
 jq && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the genotyphi code; make /data
RUN wget https://github.com/typhoidgenomics/genotyphi/archive/refs/tags/v${GENOTYPHI_VER}.tar.gz && \
 tar -xzf v${GENOTYPHI_VER}.tar.gz && \
 rm -v v${GENOTYPHI_VER}.tar.gz && \
 mv -v genotyphi-${GENOTYPHI_VER} /genotyphi && \
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

# set final working directory as /data
WORKDIR /data

# new stage for downloading test FASTQs
FROM ncbi/sra-tools:3.0.1 as fastq

# set working directory to /test
WORKDIR /test

# SRR3277297 is Salmonella enterica serovar Typhi: https://www.ncbi.nlm.nih.gov/sra/?term=SRR3277297
# SRR3441855 is Shigella sonnei from CDPH: https://www.ncbi.nlm.nih.gov/sra/?term=SRR3441855
RUN fasterq-dump --progress --split-files --threads 2 -A SRR3277297 --skip-technical && \
 fasterq-dump --progress --split-files --threads 2 -A SRR3441855 --skip-technical && \
 gzip *.fastq

# new base for testing
FROM app as test

# set working directory to /test
WORKDIR /test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="mykrobe"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# so I can use 'column' to make outputs pretty & nice to read
RUN apt-get update && apt-get install -y --no-install-recommends bsdmainutils

# test with TB FASTQs as mentioned in mykrobe instructions
RUN wget -O test_reads.fq.gz https://ndownloader.figshare.com/files/21059229 && \
 mykrobe predict -t 2 -s SAMPLE -S tb -o out.json --format json -i test_reads.fq.gz && \
 cat out.json

# Copy the test FASTQs from "fastq" stage to /test
COPY --from=fastq /test/*fastq.gz /test/

# so that the below commands are run with /bin/bash shell and not /bin/sh - needed for bash-specific tricks below
SHELL ["/bin/bash", "-c"]

# test mykrobe and genotyphi with Salmonella enterica serovar Typhi FASTQs
RUN mykrobe predict -t 2 --sample SRR3277297 --species typhi --format json --out SRR3277297.genotyphi.json --seq SRR3277297_1.fastq.gz SRR3277297_2.fastq.gz && \
python /genotyphi/parse_typhi_mykrobe.py --jsons SRR3277297.genotyphi.json --prefix mykrobe_out && \
column -t -s $'\t' mykrobe_out_predictResults.tsv

# test mykrobe and sonneityping with Shigella sonnei FASTQs
RUN mykrobe predict --sample Ssonnei --species sonnei --format json_and_csv --out Ssonnei --seq SRR3441855_1.fastq.gz SRR3441855_2.fastq.gz && \
 python /sonneityping/parse_mykrobe_predict.py --jsons Ssonnei.json --alleles /sonneityping/alleles.txt --prefix sonneityping && \
 column -t -s $'\t' sonneityping_predictResults.tsv

# final version check
RUN mykrobe --version

### OUTPUT FROM mykrobe panels describe run on 2023-03-30: ###
# Species summary:

# Species Update_available        Installed_version       Installed_url   Latest_version  Latest_url
# sonnei  no      20210201        https://ndownloader.figshare.com/files/26274424 20210201        https://ndownloader.figshare.com/files/26274424
# staph   no      20201001        https://ndownloader.figshare.com/files/24914930 20201001        https://ndownloader.figshare.com/files/24914930
# tb      no      20220705        https://ndownloader.figshare.com/files/36197349 20220705        https://ndownloader.figshare.com/files/36197349
# typhi   no      20221208        https://ndownloader.figshare.com/files/38478086 20221208        https://ndownloader.figshare.com/files/38478086

# sonnei default panel: 20210201
# sonnei panels:
# Panel   Reference       Description
# 20201012        NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC
# 20210201        NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC (same as 20201012, but with lineage3.7.30 added)

# staph default panel: 20170217
# staph panels:
# Panel   Reference       Description
# 20170217        BX571856.1      AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)

# tb default panel: 202206
# tb panels:
# Panel   Reference       Description
# 201901  NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), and second line drugs from Walker 2015 panel
# 202010  NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), second line drugs from Walker 2015 panel, and lineage scheme from Chiner-Oms 2020
# 202206  NC_000962.3     AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), and lineage scheme from Chiner-Oms 2020
# bradley-2015    NC_000962.3     AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
# walker-2015     NC_000962.3     AMR panel described in Walker, Timothy M et al. Whole-genome sequencing for prediction of Mycobacterium tuberculosis drug susceptibility and resistance: a retrospective cohort study. The Lancet Infectious Diseases , Volume 15 , Issue 10 , 1193 - 1202

# typhi default panel: 20221207
# typhi panels:
# Panel   Reference       Description
# 20210323        AL513382.1      GenoTyphi genotyping scheme and AMR calling using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766)
# 20221207        AL513382.1      v20220712 of GenoTyphi genotyping scheme and AMR calling for Salmonella Typhi, using Wong et al 2016 (https://doi.org/10.1038/ncomms12827) and updates as described in Dyson & Holt 2021 (https://doi.org/10.1101/2021.04.28.441766), Sikorski et al 2022 (https://doi.org/10.1128/mbio.01920-22) and the technical report at https://doi.org/10.5281/zenodo.7407985.
