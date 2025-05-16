FROM mambaorg/micromamba:2.0.8-ubuntu22.04 AS app

# Version arguments
# ARG variables only persist during build time
# THIS ARG ONLY USED FOR A LABEL. VERSION SPECIFIED IN PANAROO-ENVIRONMENT.YML
ARG PANAROO_SOFTWARE_VERSION="1.5.2"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.0.8-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Panaroo"
LABEL software.version=${PANAROO_SOFTWARE_VERSION}
LABEL description="An updated pipeline for pangenome investigation"
LABEL website="https://github.com/gtonkinhill/panaroo"
LABEL license="https://github.com/gtonkinhill/panaroo/blob/master/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@theiagen.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# Install Panaroo conda environment into base environment
# clean up conda garbage
# conda environment includes optional tools prokka, prank, mafft, clustal, and mash
RUN micromamba install -y -n base -c conda-forge -c bioconda python=3.9 panaroo=${PANAROO_SOFTWARE_VERSION} && \
    micromamba clean -a -f -y

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/bin:/opt/conda/envs/base/bin:${PATH}" \
    LC_ALL=C.UTF-8

# set working directory to /data
WORKDIR /data

# set default command
CMD ["panaroo", "-h"]

# new base for testing
FROM app AS test

# checks to see if tool is in PATH
RUN panaroo --version && panaroo -h

WORKDIR /test

# Grab test data from 1.2.10
RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/panaroo/1.2.10/tests/ecoli_1.gff && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/panaroo/1.2.10/tests/ecoli_2.gff && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/panaroo/1.2.10/tests/gene_data.csv && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/panaroo/1.2.10/tests/summary_statistics.txt

# Run Panaroo
RUN panaroo --clean-mode strict -i *.gff -o panaroo_results/

RUN head panaroo_results/summary_statistics.txt && \
    head summary_statistics.txt && \
    cmp summary_statistics.txt panaroo_results/summary_statistics.txt

RUN panaroo --aligner mafft -i *.gff -o panaroo_mafft/ --clean-mode strict -a pan && \
    head panaroo_mafft/summary_statistics.txt

RUN micromamba list