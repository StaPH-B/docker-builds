FROM mambaorg/micromamba:2.0.3-ubuntu22.04 AS app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags.
# using pangolin-data github tag, NOT what is in the GH release title "v1.2.133"
ARG PANGOLIN_VER="v4.3.1"
ARG PANGOLIN_DATA_VER="v1.31"
ARG SCORPIO_VER="v0.3.19"
ARG CONSTELLATIONS_VER="v0.1.12"
ARG USHER_VER="0.6.3"

# metadata labels
LABEL base.image="mambaorg/micromamba:2.0.3-ubuntu22.04"
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
# pin specific versions of usher, scorpio, pangolin-data, constellations, and pulp
# create the conda environment using modified environment.yml
# line to remove "defaults" channel to ensure that it isn't used due to Anaconda's recent ToS changes
RUN sed -i "s|usher.*|usher=${USHER_VER}|" /pangolin/environment.yml && \
 sed -i "s|scorpio.git|scorpio.git@${SCORPIO_VER}|" /pangolin/environment.yml && \
 sed -i "s|pangolin-data.git|pangolin-data.git@${PANGOLIN_DATA_VER}|" /pangolin/environment.yml && \
 sed -i "s|constellations.git|constellations.git@${CONSTELLATIONS_VER}|" /pangolin/environment.yml && \
 sed -i "12 a\  - pulp=2.7.0" /pangolin/environment.yml && \
 sed -i '/.*defaults/d' /pangolin/environment.yml && \
 micromamba create -n pangolin -y -f /pangolin/environment.yml && \
 micromamba clean -a -y -f

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

WORKDIR /pangolin

# run pip install step; download optional pre-computed assignment hashes for UShER (useful for running on large batches of samples)
# best to skip using the assigment-cache if running on one sample for speed
# print versions
RUN pip install . && \
 pangolin --add-assignment-cache && \
 mkdir /data && \
 pangolin --all-versions && \
 usher --version

# final working directory in "app" layer is /data for passing data in/out of container
WORKDIR /data

# hardcode pangolin executable into the PATH variable
ENV PATH="${PATH}:/opt/conda/envs/pangolin/bin/" XDG_CACHE_HOME=/tmp

# default command is to pull up help options for pangolin; can be overridden of course
CMD ["pangolin", "-h"]

# new base for testing
FROM app AS test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="pangolin"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# test on test sequences supplied with Pangolin code
RUN pangolin /pangolin/pangolin/test/test_seqs.fasta -o /data/test_seqs-output-pusher && \
 column -t -s, /data/test_seqs-output-pusher/lineage_report.csv 

# test functionality of assignment-cache option
RUN pangolin --use-assignment-cache /pangolin/pangolin/test/test_seqs.fasta

# download B.1.1.7 genome from Utah
ADD https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa /test-data/SRR13957123.consensus.fa

# test on a B.1.1.7 genome
RUN pangolin /test-data/SRR13957123.consensus.fa -o /test-data/SRR13957123-pusher && \
 column -t -s, /test-data/SRR13957123-pusher/lineage_report.csv

 # install unzip for unzipping zip archive from NCBI
RUN apt-get update && apt-get install -y --no-install-recommends unzip

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

# testing the following lineages:
# BA.1 | ON924087.1 | from Florida https://www.ncbi.nlm.nih.gov/biosample?term=SAMN29506515 and https://www.ncbi.nlm.nih.gov/nuccore/ON924087
# XBB.1.16 | OQ381818.1 | introduced in p-data 1.19, https://www.ncbi.nlm.nih.gov/nuccore/2440446687 and https://www.ncbi.nlm.nih.gov/biosample?term=SAMN33060589 and https://github.com/cov-lineages/pango-designation/issues/1723
# another XBB.1.16 | OR177999.1 | https://www.ncbi.nlm.nih.gov/nuccore/OR177999.1
# BA.2.86 | OR461132.1 | from Michigan https://www.ncbi.nlm.nih.gov/nuccore/OR461132.1
# JN.2 (BA.2.86 sublineage) JN.2 is an alias of B.1.1.529.2.86.1.2 | OR598183.1 | NY CDC Quest sample https://www.ncbi.nlm.nih.gov/nuccore/OR598183
# JQ.1 (BA.2.86.3 sublineage); JQ.1 is an alias of B.1.1.529.2.86.3.1 | OR716684.1 | THANK YOU ERIN AND UPHL!! https://www.ncbi.nlm.nih.gov/nuccore/OR716684 this test is important due to the fact that this lineage was included in the UShER tree, despite being designated after the pangolin-designation 1.23 release it previously caused and error/bug in pangolin, but now is fixed
# JN.1.22 (BA.2.86.x sublineage; full unaliased lineage is B.1.1.529.2.86.1.1.22) | PP189069.1 | https://github.com/cov-lineages/pango-designation/commit/a90c8e31c154621ed86c985debfea09e17541cda
# JN.1.48 (BA.2.86.x sublineage; full unaliased lineage is B.1.1.529.2.86.1.1.48) | PP218754.1 | https://github.com/cov-lineages/pango-designation/releases/tag/v1.27 and https://github.com/cov-lineages/pango-designation/commit/67f48bf24283999f1940f3aee8159f404124ff3f and https://www.ncbi.nlm.nih.gov/nuccore/PP218754
# LK.1 | PP770375.1 | introduced in pango-designation 1.28 https://github.com/cov-lineages/pango-designation/commit/922795c90de355e67200cf4d379e8e5ff22472e4 and https://www.ncbi.nlm.nih.gov/nuccore/2728145425 thank you Luis, Lorraine, Marcos & team from PR Sci Trust for sharing your data!
# KP.3.3.2 | PQ073669.1 | introduced in pango-designation 1.29 https://github.com/cov-lineages/pango-designation/commit/7125e606818312b78f0756d7fcab6dba92dd0a9e and https://www.ncbi.nlm.nih.gov/nuccore/PQ073669
# MC.2 | PQ034842.1 | introduced in pango-designation 1.30 https://github.com/cov-lineages/pango-designation/commit/c64dbc47fbfbfd7f4da011deeb1a88dd6baa45f1#diff-a121ea4b8cbeb4c0020511b5535bf24489f0223cc83511df7b8209953115d329R2564181 and https://www.ncbi.nlm.nih.gov/nuccore/PQ034842
# XEC.3 | PQ277908.1 | introduced in pango-designation 1.31 https://github.com/cov-lineages/pango-designation/commit/ba3711a5615956ed97150288eb68356aa0fe7cdd#diff-a121ea4b8cbeb4c0020511b5535bf24489f0223cc83511df7b8209953115d329R2572545 and https://www.ncbi.nlm.nih.gov/nuccore/PQ277908.1
RUN datasets download virus genome accession ON924087.1,OQ381818.1,OR177999.1,OR461132.1,OR598183.1,OR716684.1,PP189069.1,PP218754.1,PP770375.1,PQ073669.1,PQ034842.1,PQ277908.1 && \
unzip -o ncbi_dataset.zip && \
rm -v ncbi_dataset.zip && \
pangolin ncbi_dataset/data/genomic.fna && \
column -t -s, lineage_report.csv