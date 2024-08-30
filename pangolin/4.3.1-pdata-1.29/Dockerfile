FROM mambaorg/micromamba:1.5.8 AS app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags.
# using pangolin-data github tag, NOT what is in the GH release title "v1.2.133"
ARG PANGOLIN_VER="v4.3.1"
ARG PANGOLIN_DATA_VER="v1.29"
ARG SCORPIO_VER="v0.3.19"
ARG CONSTELLATIONS_VER="v0.1.12"
ARG USHER_VER="0.6.3"

# metadata labels
LABEL base.image="mambaorg/micromamba:1.5.8"
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
RUN sed -i "s|usher.*|usher=${USHER_VER}|" /pangolin/environment.yml && \
 sed -i "s|scorpio.git|scorpio.git@${SCORPIO_VER}|" /pangolin/environment.yml && \
 sed -i "s|pangolin-data.git|pangolin-data.git@${PANGOLIN_DATA_VER}|" /pangolin/environment.yml && \
 sed -i "s|constellations.git|constellations.git@${CONSTELLATIONS_VER}|" /pangolin/environment.yml && \
 sed -i "12 a\  - pulp=2.7.0" /pangolin/environment.yml && \
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

# download assembly for a BA.1 from Florida (https://www.ncbi.nlm.nih.gov/biosample?term=SAMN29506515 and https://www.ncbi.nlm.nih.gov/nuccore/ON924087)
# run pangolin in usher analysis mode
RUN datasets download virus genome accession ON924087.1 --filename ON924087.1.zip && \
 unzip ON924087.1.zip && rm ON924087.1.zip && \
 mv -v ncbi_dataset/data/genomic.fna ON924087.1.genomic.fna && \
 rm -vr ncbi_dataset/ README.md && \
 pangolin ON924087.1.genomic.fna -o ON924087.1-usher && \
 column -t -s, ON924087.1-usher/lineage_report.csv

# test specific for new lineage, XBB.1.16, introduced in pangolin-data v1.19
# using this assembly: https://www.ncbi.nlm.nih.gov/nuccore/2440446687
# biosample here: https://www.ncbi.nlm.nih.gov/biosample?term=SAMN33060589
# one of the sample included in initial pango-designation here: https://github.com/cov-lineages/pango-designation/issues/1723
RUN datasets download virus genome accession OQ381818.1 --filename OQ381818.1.zip && \
 unzip OQ381818.1.zip && rm OQ381818.1.zip && \
 mv -v ncbi_dataset/data/genomic.fna OQ381818.1.genomic.fna && \
 rm -vr ncbi_dataset/ README.md && \
 pangolin OQ381818.1.genomic.fna -o OQ381818.1-usher && \
 column -t -s, OQ381818.1-usher/lineage_report.csv

# testing another XBB.1.16, trying to test scorpio functionality. Want pangolin to NOT assign lineage based on pango hash match.
# this test runs as expected, uses scorpio to check for constellation of mutations, then assign using PUSHER placement
RUN datasets download virus genome accession OR177999.1 --filename OR177999.1.zip && \
unzip OR177999.1.zip && rm OR177999.1.zip && \
mv -v ncbi_dataset/data/genomic.fna OR177999.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin OR177999.1.genomic.fna -o OR177999.1-usher && \
column -t -s, OR177999.1-usher/lineage_report.csv

 ## test for BA.2.86
 # virus identified in MI: https://www.ncbi.nlm.nih.gov/nuccore/OR461132.1
RUN datasets download virus genome accession OR461132.1 --filename OR461132.1.zip && \
unzip OR461132.1.zip && rm OR461132.1.zip && \
mv -v ncbi_dataset/data/genomic.fna OR461132.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin OR461132.1.genomic.fna -o OR461132.1-usher && \
column -t -s, OR461132.1-usher/lineage_report.csv

 ## test for JN.2 (BA.2.86 sublineage) JN.2 is an alias of B.1.1.529.2.86.1.2
 # NY CDC Quest sample: https://www.ncbi.nlm.nih.gov/nuccore/OR598183
RUN datasets download virus genome accession OR598183.1 --filename OR598183.1.zip && \
unzip OR598183.1.zip && rm OR598183.1.zip && \
mv -v ncbi_dataset/data/genomic.fna OR598183.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin OR598183.1.genomic.fna -o OR598183.1-usher && \
column -t -s, OR598183.1-usher/lineage_report.csv

## test for JQ.1 (BA.2.86.3 sublineage); JQ.1 is an alias of B.1.1.529.2.86.3.1
# THANK YOU ERIN AND UPHL!! https://www.ncbi.nlm.nih.gov/nuccore/OR716684
# this test is important due to the fact that this lineage was included in the UShER tree, despite being designated after the pangolin-designation 1.23 release
# it previously caused and error/bug in pangolin, but now is fixed
RUN datasets download virus genome accession OR716684.1 --filename OR716684.1.zip && \
unzip OR716684.1.zip && rm OR716684.1.zip && \
mv -v ncbi_dataset/data/genomic.fna OR716684.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin OR716684.1.genomic.fna -o OR716684.1-usher && \
column -t -s, OR716684.1-usher/lineage_report.csv

## test for JN.1.22 (BA.2.86.x sublineage; full unaliased lineage is B.1.1.529.2.86.1.1.22)
# see here for commit where it was designated https://github.com/cov-lineages/pango-designation/commit/a90c8e31c154621ed86c985debfea09e17541cda
# Here's the genome on NCBI, which was used to designate JN.1.22 lineage
RUN datasets download virus genome accession PP189069.1 --filename PP189069.1.zip && \
unzip PP189069.1.zip && rm PP189069.1.zip && \
mv -v ncbi_dataset/data/genomic.fna PP189069.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin PP189069.1.genomic.fna -o PP189069.1-usher && \
column -t -s, PP189069.1-usher/lineage_report.csv

## test for JN.1.48 (BA.2.86.x sublineage; full unaliased lineage is B.1.1.529.2.86.1.1.48) 
# this lineages which was designated in pango-designation v1.27: https://github.com/cov-lineages/pango-designation/releases/tag/v1.27
# see here for commit where it was designated https://github.com/cov-lineages/pango-designation/commit/67f48bf24283999f1940f3aee8159f404124ff3f
# Here's the genome on NCBI: https://www.ncbi.nlm.nih.gov/nuccore/PP218754
RUN datasets download virus genome accession PP218754.1 --filename PP218754.1.zip && \
unzip PP218754.1.zip && rm PP218754.1.zip && \
mv -v ncbi_dataset/data/genomic.fna PP218754.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin PP218754.1.genomic.fna -o PP218754.1-usher && \
column -t -s, PP218754.1-usher/lineage_report.csv

# new lineage LK.1 that was introduced in pango-designation v1.28: https://github.com/cov-lineages/pango-designation/commit/922795c90de355e67200cf4d379e8e5ff22472e4
# thank you Luis, Lorraine, Marcos & team from PR Sci Trust for sharing your data!
# genome on NCBI: https://www.ncbi.nlm.nih.gov/nuccore/2728145425
RUN datasets download virus genome accession PP770375.1 --filename PP770375.1.zip && \
unzip PP770375.1.zip && rm PP770375.1.zip && \
mv -v ncbi_dataset/data/genomic.fna PP770375.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin PP770375.1.genomic.fna -o PP770375.1-usher && \
column -t -s, PP770375.1-usher/lineage_report.csv

# new lineage KP.3.3.2 that was introduced in pango-designation v1.29: https://github.com/cov-lineages/pango-designation/commit/7125e606818312b78f0756d7fcab6dba92dd0a9e
# genome on NCBI: https://www.ncbi.nlm.nih.gov/nuccore/PQ073669
RUN datasets download virus genome accession PQ073669.1 --filename PQ073669.1.zip && \
unzip PQ073669.1.zip && rm PQ073669.1.zip && \
mv -v ncbi_dataset/data/genomic.fna PQ073669.1.genomic.fna && \
rm -vr ncbi_dataset/ README.md && \
pangolin PQ073669.1.genomic.fna -o PQ073669.1-usher && \
column -t -s, PQ073669.1-usher/lineage_report.csv