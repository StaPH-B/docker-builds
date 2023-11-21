FROM mambaorg/micromamba:1.4.1 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
ARG MYKROBE_VER="0.13.0"

# metadata labels
LABEL base.image="mambaorg/micromamba:1.4.1"
LABEL dockerfile.version="1"
LABEL software="Mykrobe"
LABEL software.version="${MYKROBE_VER}"
LABEL description="Antibiotic resistance prediction in minutes"
LABEL website="https://github.com/Mykrobe-tools/mykrobe"
LABEL license="https://github.com/Mykrobe-tools/mykrobe/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 procps \
 jq && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*


# set the PATH and LC_ALL for singularity compatibility
ENV PATH="${PATH}:/opt/conda/envs/mykrobe/bin/" \
 LC_ALL=C.UTF-8

# create the conda environment, install mykrobe via bioconda package; cleanup conda garbage
# an attempt to install this from source was made, but ran into issues with MCCORTEX
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

CMD mykrobe --help

# new base for testing
FROM app as test

# set working directory to /test
WORKDIR /test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="mykrobe"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN mykrobe --help && mykrobe --version

# test with TB FASTQs
RUN wget -O test_reads.fq.gz https://ndownloader.figshare.com/files/21059229 && \
    mykrobe predict -s SAMPLE -S tb -o out.json --format json -i test_reads.fq.gz && \
    cat out.json && \
    mykrobe panels describe

### OUTPUT FROM mykrobe panels describe run on 2023-11-09: ###
#0 12.57 Gathering data from /usr/local/lib/python3.9/site-packages/mykrobe/data
#0 12.57
#0 12.57 Species summary:
#0 12.57
#0 12.57 Species        Update_available        Installed_version       Installed_url   Latest_version  Latest_url
#0 12.57 sonnei no      20210201        https://ndownloader.figshare.com/files/26274424 20210201        https://ndownloader.figshare.com/files/26274424
#0 12.57 staph  no      20201001        https://ndownloader.figshare.com/files/24914930 20201001        https://ndownloader.figshare.com/files/24914930
#0 12.57 tb     no      20230928        https://figshare.com/ndownloader/files/42494211 20230928        https://figshare.com/ndownloader/files/42494211
#0 12.57 typhi  no      20221208        https://ndownloader.figshare.com/files/38478086 20221208        https://ndownloader.figshare.com/files/38478086
#0 12.57
#0 12.57 sonnei default panel: 20210201
#0 12.57 sonnei panels:
#0 12.57 Panel  Reference       Description
#0 12.57 20201012       NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC
#0 12.57 20210201       NC_016822.1     Genotyping panel for Shigella sonnei based on scheme defined in Hawkey 2020, and panel for variants in the quinolone resistance determining regions in gyrA and parC (same as 20201012, but with lineage3.7.30 added)
#0 12.57
#0 12.57 staph default panel: 20170217
#0 12.57 staph panels:
#0 12.57 Panel  Reference       Description
#0 12.57 20170217       BX571856.1      AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
#0 12.57
#0 12.57 tb default panel: 202309
#0 12.57 tb panels:
#0 12.57 Panel  Reference       Description
#0 12.57 201901 NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), and second line drugs from Walker 2015 panel
#0 12.57 202010 NC_000962.3     AMR panel based on first line drugs from NEJM-2018 variants (DOI 10.1056/NEJMoa1800474), second line drugs from Walker 2015 panel, and lineage scheme from Chiner-Oms 2020
#0 12.57 202206 NC_000962.3     AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), and lineage scheme from Chiner-Oms 2020
#0 12.57 202309 NC_000962.3     AMR panel '202010' combined with the WHO 2021 catalogue (doi:10/h298 and doi:10/h299), lineage scheme from Chiner-Oms 2020, and updated species based on GTDB r214 (doi:10.1093/nar/gkab776)
#0 12.57 bradley-2015   NC_000962.3     AMR panel described in Bradley, P et al. Rapid antibiotic-resistance predictions from genome sequence data for Staphylococcus aureus and Mycobacterium tuberculosis. Nat. Commun. 6:10063 doi: 10.1038/ncomms10063 (2015)
#0 12.57 walker-2015    NC_000962.3     AMR panel described in Walker, Timothy M et al. Whole-genome sequencing for prediction of Mycobacterium tuberculosis drug susceptibility and resistance: a retrospective cohort study. The Lancet Infectious Diseases , Volume 15 , Issue 10 , 1193 - 1202
