# base image
FROM ubuntu:focal as app

ARG STARAMR_VER="0.8.0"
# trying out the most up-to-date version of mlst. Might have to roll back a few versions if this does not work? 2.19.0 was used w/ staramr 0.7.1
# mlst 2.22.1 seemingly works (based on my limited testing)
ARG MLST_VER="2.22.1"

# metadata, optional but highly recommended 
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="staramr"
LABEL software.version="${STARAMR_VER}"
LABEL description="staramr scans bacterial genome contigs for AMR genes and plasmids"
LABEL website="https://github.com/phac-nml/staramr"
LABEL license="https://github.com/phac-nml/staramr/blob/master/LICENSE"
LABEL maintainer1="Rachael St. Jacques"
LABEL maintainer1.email="rachael.stjacques@dgs.virginia.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"

# install dependencies via apt; cleanup apt garbage
# ncbi-blast+ is v2.9.0 in ubuntu:focal (as of August 2022)
RUN apt-get update && apt-get install -y --no-install-recommends \
 python3 \
 python3-pip \
 git \
 wget \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 gzip \
 file \
 ncbi-blast+ && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# any2fasta
RUN cd /usr/local/bin && \
 wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
 chmod +x any2fasta

# mlst 
# apt dependencies: wget libmoo-perl liblist-moreutils-perl libjson-perl gzip file
# also requires blast 2.9.0 or greater
RUN wget https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz && \
 tar -xzf v${MLST_VER}.tar.gz && \
 rm v${MLST_VER}.tar.gz

# staramr; make /data 
RUN pip3 install staramr==${STARAMR_VER} pandas && \
 mkdir /data

# set $PATH and locale settings for singularity
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin" \
    LC_ALL=C 

# update staramr default databases and print db info
RUN staramr db update -d && staramr db info

WORKDIR /data

##### staramr db information in container at time of docker image build #####
# resfinder_db_dir              = /usr/local/lib/python3.8/dist-packages/staramr/databases/data/update/resfinder
# resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
# resfinder_db_commit           = a4cc8bc1e969b3829ad0f0bd4a6cadf615ac9f21
# resfinder_db_date             = Tue, 19 Jul 2022 07:16
# pointfinder_db_dir            = /usr/local/lib/python3.8/dist-packages/staramr/databases/data/update/pointfinder
# pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
# pointfinder_db_commit         = bfa17543d776faf3962ba1e824dec5f55a66d73b
# pointfinder_db_date           = Fri, 22 Apr 2022 08:27
# pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
# pointfinder_organisms_valid   = campylobacter, salmonella
# plasmidfinder_db_dir          = /usr/local/lib/python3.8/dist-packages/staramr/databases/data/update/plasmidfinder
# plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
# plasmidfinder_db_commit       = 9002e7282dd0599b9247f4f700368b8fa64fbaa8
# plasmidfinder_db_date         = Wed, 30 Mar 2022 09:20
# mlst_version                  = 2.22.1
# pointfinder_gene_drug_version = 072621
# resfinder_gene_drug_version   = 072621

FROM app as test

RUN staramr --help && staramr --version

# download the FASTA file for ${GENBANK_ACCESSION} 
# Salmonella Enterica isolate from PHE-UK: https://www.ncbi.nlm.nih.gov/assembly/GCA_010941835.1/
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz

# run staramr on the second genome mentioned on staramr's documentation; print resulting TSVs
RUN staramr search -o /data/staramr-test-Salmonella \
  --pointfinder-organism salmonella \
  --plasmidfinder-database-type enterobacteriales \
  /data/GCA_010941835.1_PDT000052640.3_genomic.fna

# installing bsdmainutils for installing "column" command
RUN apt-get update && apt-get install -y --no-install-recommends bsdmainutils

# neatly print out resulting/output TSVs
RUN column -t /data/staramr-test-Salmonella/mlst.tsv && echo && \
    column -t /data/staramr-test-Salmonella/pointfinder.tsv && echo && \
    column -t /data/staramr-test-Salmonella/plasmidfinder.tsv && echo && \
    column -t /data/staramr-test-Salmonella/resfinder.tsv && echo && \
    column -t /data/staramr-test-Salmonella/detailed_summary.tsv && echo && \
    column -t /data/staramr-test-Salmonella/summary.tsv
