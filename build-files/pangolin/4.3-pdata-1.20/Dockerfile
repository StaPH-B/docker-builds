FROM mambaorg/micromamba:1.4.3 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags.
# using pangolin-data github tag, NOT what is in the GH release title "v1.2.133"
ARG PANGOLIN_VER="v4.3"
ARG PANGOLIN_DATA_VER="v1.20"
ARG SCORPIO_VER="v0.3.17"
ARG CONSTELLATIONS_VER="v0.1.10"
ARG USHER_VER="0.6.2"

# metadata labels
LABEL base.image="mambaorg/micromamba:1.4.3"
LABEL dockerfile.version="1"
LABEL software="pangolin"
LABEL software.version=${PANGOLIN_VER}
LABEL description="Conda environment for Pangolin. Pangolin: Software package for assigning SARS-CoV-2 genome sequences to global lineages."
LABEL website="https://github.com/cov-lineages/pangolin"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/cov-lineages/pangolin/blob/master/LICENSE.txt"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 git \
 procps \
 bsdmainutils && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get the pangolin repo
RUN wget "https://github.com/cov-lineages/pangolin/archive/${PANGOLIN_VER}.tar.gz" && \
 tar -xf ${PANGOLIN_VER}.tar.gz && \
 rm -v ${PANGOLIN_VER}.tar.gz && \
 mv -v pangolin-* pangolin

# set the environment; PATH is unnecessary here, but leaving anyways. It's reset later in dockerfile
ENV PATH="$PATH" \
 LC_ALL=C.UTF-8

# modify environment.yml to pin specific versions during install
# create the conda environment using modified environment.yml
RUN sed -i "s|usher.*|usher=${USHER_VER}|" /pangolin/environment.yml && \
 sed -i "s|scorpio.git|scorpio.git@${SCORPIO_VER}|" /pangolin/environment.yml && \
 sed -i "s|pangolin-data.git|pangolin-data.git@${PANGOLIN_DATA_VER}|" /pangolin/environment.yml && \
 sed -i "s|constellations.git|constellations.git@${CONSTELLATIONS_VER}|" /pangolin/environment.yml && \
 micromamba create -n pangolin -y -f /pangolin/environment.yml

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /pangolin

# run pip install step; download optional pre-computed assignment hashes for UShER (useful for running on large batches of samples)
# best to skip using the assigment-cache if running on one sample for speed
# print versions
RUN pip install . && \
 pangolin --add-assignment-cache && \
 micromamba clean -a -y && \
 mkdir /data && \
 pangolin --all-versions && \
 usher --version

WORKDIR /data

# hardcode pangolin executable into the PATH variable
ENV PATH="${PATH}:/opt/conda/envs/pangolin/bin/"

# default command is to pull up help options for virulencefinder; can be overridden of course
CMD ["pangolin", "-h"]

# new base for testing
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# test on test sequences supplied with Pangolin code
RUN pangolin /pangolin/pangolin/test/test_seqs.fasta --analysis-mode usher -o /data/test_seqs-output-pusher && \
 column -t -s, /data/test_seqs-output-pusher/lineage_report.csv 

# test functionality of assignment-cache option
RUN pangolin --use-assignment-cache /pangolin/pangolin/test/test_seqs.fasta

# download B.1.1.7 genome from Utah
ADD https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa /test-data/SRR13957123.consensus.fa

# test on a B.1.1.7 genome
RUN pangolin /test-data/SRR13957123.consensus.fa --analysis-mode usher -o /test-data/SRR13957123-pusher && \
 column -t -s, /test-data/SRR13957123-pusher/lineage_report.csv

 # install unzip for unzipping zip archive from NCBI
RUN apt-get update && apt-get install -y --no-install-recommends unzip

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

# download assembly for a BA.1 from Florida (https://www.ncbi.nlm.nih.gov/biosample?term=SAMN29506515 and https://www.ncbi.nlm.nih.gov/nuccore/ON924087)
# run pangolin in usher analysis mode
RUN datasets download virus genome accession ON924087.1 --filename ON924087.1.zip && \
 unzip ON924087.1.zip && rm ON924087.1.zip && \
 mv -v ncbi_dataset/data/genomic.fna ON924087.1.genomic.fna && \
 rm -vr ncbi_dataset/ README.md && \
 pangolin ON924087.1.genomic.fna --analysis-mode usher -o ON924087.1-usher && \
 column -t -s, ON924087.1-usher/lineage_report.csv

# test specific for new lineage, XBB.1.16, introduced in pangolin-data v1.19
# using this assembly: https://www.ncbi.nlm.nih.gov/nuccore/2440446687
# biosample here: https://www.ncbi.nlm.nih.gov/biosample?term=SAMN33060589
# one of the sample included in initial pango-designation here: https://github.com/cov-lineages/pango-designation/issues/1723
RUN datasets download virus genome accession OQ381818.1 --filename OQ381818.1.zip && \
 unzip OQ381818.1.zip && rm OQ381818.1.zip && \
 mv -v ncbi_dataset/data/genomic.fna OQ381818.1.genomic.fna && \
 rm -vr ncbi_dataset/ README.md && \
 pangolin OQ381818.1.genomic.fna --analysis-mode usher -o OQ381818.1-usher && \
 column -t -s, OQ381818.1-usher/lineage_report.csv
