FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags.
# using pangolin-data github tag, NOT what is in the GH release title "v1.2.133"
ARG PANGOLIN_VER="v4.4"
ARG PANGOLIN_DATA_VER="v1.37.1"
ARG SCORPIO_VER="v0.3.19"
ARG CONSTELLATIONS_VER="v0.1.12"
ARG USHER_VER="0.6.3"

# metadata labels
LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
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
RUN echo "Downloading Pangolin version: ${PANGOLIN_VER}" && \
wget -q "https://github.com/cov-lineages/pangolin/archive/${PANGOLIN_VER}.tar.gz" && \
tar -xzf ${PANGOLIN_VER}.tar.gz && \
rm -v ${PANGOLIN_VER}.tar.gz && \
mv -v pangolin-* pangolin

# modify environment.yml to pin specific versions during install
# pin specific versions of usher, scorpio, pangolin-data, and constellations
# create the conda environment using modified environment.yml
# PIP_NO_BUILD_ISOLATION=0 is needed to avoid pip install step from trying to create its own temporary environment with setuptools >82.0.0 which does not contain pkg_resources since it's deprecated; pkg_resources is needed for the pip install portion of the environment.yml. Conda needs pkg_resources (installed via setuptools <82.0.0) when installing stuff via pip.
RUN sed -i "s|usher.*|usher=${USHER_VER}|" /pangolin/environment.yml && \
sed -i "s|scorpio.git|scorpio.git@${SCORPIO_VER}|" /pangolin/environment.yml && \
sed -i "s|pangolin-data.git|pangolin-data.git@${PANGOLIN_DATA_VER}|" /pangolin/environment.yml && \
sed -i "s|constellations.git|constellations.git@${CONSTELLATIONS_VER}|" /pangolin/environment.yml && \
sed -i "12 a\  - setuptools<82.0" /pangolin/environment.yml && \
cat /pangolin/environment.yml && \
export PIP_NO_BUILD_ISOLATION=0 && \
micromamba create -n pangolin -y -f /pangolin/environment.yml && \
micromamba clean -a -y -f

# hardcode pangolin executable into the PATH variable; LC_ALL for singularity compatibility
ENV PATH="${PATH}:/opt/conda/envs/pangolin/bin/" \
XDG_CACHE_HOME=/tmp \
LC_ALL=C.UTF-8

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

# default command is to pull up help options for pangolin; can be overridden of course
CMD ["pangolin", "-h"]

# new base for testing
FROM app AS test

RUN pangolin -h 

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
RUN echo "Downloading and installing NCBI datasets tool... " && \
wget -q https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
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
# XEC.2 | PQ277908.1 | introduced in pango-designation 1.31 https://github.com/cov-lineages/pango-designation/commit/ba3711a5615956ed97150288eb68356aa0fe7cdd#diff-a121ea4b8cbeb4c0020511b5535bf24489f0223cc83511df7b8209953115d329R2572545 and https://www.ncbi.nlm.nih.gov/nuccore/PQ277908.1
# NC.1.2 | PQ725776.1 | introduced in pango-designation 1.33 https://github.com/cov-lineages/pango-designation/commit/4e87876f825fbd932b614c791c5848ea7f3d7b83 and https://www.ncbi.nlm.nih.gov/biosample?term=SAMN45350159
# PQ.3 | PV666687.1 | introduced in pango-designation 1.34 https://github.com/cov-lineages/pango-designation/commit/5bebd58910e19ebb8058def5c22b67fc5b7a5959
# XFG.3.5 | PX025687.1 | introduced in pango-designation 1.35 https://github.com/cov-lineages/pango-designation/commit/cb430033b29f760b7f013ff7114790c5b4b6f9b4
# XFG.5.1.4 | PV979512.1 | introduced in pango-designation 1.36 https://github.com/cov-lineages/pango-designation/commit/9bc6a238df1bcda12f548b239a86c7ce7fbcf2a3
# PQ.17.11 | PX697933.1 | introduced in pango-designation 1.37 https://github.com/cov-lineages/pango-designation/commit/38e4ffc100689e8979c786623e62a1d2887f46e9
# sed is to make output more readable by removing extra text in sequence names
RUN datasets download virus genome accession ON924087.1,OQ381818.1,OR177999.1,OR461132.1,OR598183.1,OR716684.1,PP189069.1,PP218754.1,PQ073669.1,PP770375.1,PQ034842.1,PQ277908.1,PQ725776.1,PV666687.1,PX025687.1,PV979512.1,PX697933.1 && \
unzip -o ncbi_dataset.zip && \
rm -v ncbi_dataset.zip && \
pangolin ncbi_dataset/data/genomic.fna && \
sed -i -E -e 's|Severe acute respiratory syndrome coronavirus 2 isolate SARS-CoV-2/human/||g' -e 's/^("[^"]*[0-9]{4})[^"]*"/\1"/g' lineage_report.csv && \
column -s, -t lineage_report.csv

RUN micromamba list -n pangolin
