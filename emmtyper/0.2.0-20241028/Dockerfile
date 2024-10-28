FROM mambaorg/micromamba:1.5.8 as app

ARG EMMTYPER_VER="0.2.0"
ARG SCRIPT_HASH="c0d1c26625cfe9ac458306089358dc26edad06f0"

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building
WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="emmtyper"
LABEL software.version=${EMMTYPER_VER}
LABEL description="Conda environment for emmtyper. emmtyper is a command line tool for emm-typing of Streptococcus pyogenes using a de novo or complete assembly."
LABEL website="https://github.com/MDU-PHL/emmtyper"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/MDU-PHL/emmtyper/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    unzip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

#install emmtyper and dependencies
RUN micromamba create -n emmtyper -c conda-forge -c bioconda -c defaults emmtyper=${EMMTYPER_VER} pip && \
    micromamba clean -a -y -f

# install script for downloading emmtyper database
RUN wget -q https://github.com/Daniel-VM/cdc-utilities/archive/${SCRIPT_HASH}.zip && \
    unzip ${SCRIPT_HASH}.zip && \
    echo '#!/usr/bin/env python3' > /usr/local/bin/emm_download_makedb.py && \
    cat cdc-utilities*/emm_download_makedb.py >> /usr/local/bin/emm_download_makedb.py && \
    rm -rf ${SCRIPT_HASH}.zip cdc-utilities* && \
    chmod +x /usr/local/bin/emm_download_makedb.py

# set the environment, put new conda env in PATH by default
ENV PATH="/opt/conda/envs/emmtyper/bin:/opt/conda/envs/env/bin:${PATH}" \
    LC_ALL=C.UTF-8

RUN pip install --no-cache-dir requests beautifulsoup4

CMD emmtyper --help && emm_download_makedb.py -h

WORKDIR /cdc_emm_database

# get latest emmtyper database 
RUN emm_download_makedb.py \
    --ftp_url 'https://ftp.cdc.gov/' \
    --remote_path 'pub/infectious_diseases/biotech/tsemm/' \
    --local_path /cdc_emm_database

# create a blast database without a date in the filename
RUN makeblastdb -in /cdc_emm_database/cdc_emm_database*fasta -dbtype nucl -out /cdc_emm_database/cdc_emm

WORKDIR /data

FROM app as test

RUN emmtyper --help && emm_download_makedb.py -h

RUN wget -q ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/006/785/GCA_000006785.2_ASM678v2/GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	gunzip GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	mv GCA_000006785.2_ASM678v2_genomic.fna test_data.fasta

RUN emmtyper test_data.fasta && \
	emmtyper -w pcr test_data.fasta -o test_out && \
	head -10 test_out

# testing new database
RUN emmtyper --blast_db /cdc_emm_database/cdc_emm test_data.fasta -o test3 && \
	head -10 test3 

    RUN emmtyper --version