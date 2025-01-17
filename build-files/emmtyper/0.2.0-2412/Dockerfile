FROM mambaorg/micromamba:1.5.8 AS app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building
WORKDIR /

ARG EMMTYPER_VER="0.2.0"

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="emmtyper"
LABEL software.version=${EMMTYPER_VER}
LABEL description="Conda environment for emmtyper. emmtyper is a command line tool for emm-typing of Streptococcus pyogenes using a de novo or complete assembly."
LABEL website="https://github.com/MDU-PHL/emmtyper"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/MDU-PHL/emmtyper/blob/master/LICENSE"
LABEL maintainer="Henry Kunerth"
LABEL maintainer.email="henrykunerth@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

#install emmtyper and dependencies
RUN micromamba create -n emmtyper -y -c conda-forge -c defaults -c bioconda emmtyper=${EMMTYPER_VER} && \
    micromamba clean -a -f -y

# set the environment
ENV PATH="/opt/conda/envs/emmtyper/bin:/opt/conda/envs/env/bin:${PATH}" \
    LC_ALL=C.UTF-8

# overwriting the emmtyper database
WORKDIR /opt/conda/envs/emmtyper/lib/python3.13/site-packages/emmtyper/db

# removing original files and replacing with most-current fasta file
RUN rm * && \
    wget -q https://ftp.cdc.gov/pub/infectious_diseases/biotech/tsemm/alltrimmed.tfa && \
    makeblastdb -in alltrimmed.tfa -dbtype nucl -out emm.fna

CMD ["emmtyper",  "--help"]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN emmtyper --help && emmtyper --version

RUN wget -q ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/006/785/GCA_000006785.2_ASM678v2/GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	gunzip GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	mv GCA_000006785.2_ASM678v2_genomic.fna test_data.fasta

RUN emmtyper test_data.fasta && \
	emmtyper -w pcr test_data.fasta -o test_out && \
	head test_out
