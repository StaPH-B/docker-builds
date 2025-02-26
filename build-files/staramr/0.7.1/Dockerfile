# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="staramr"
LABEL software.version="0.7.1"
LABEL description="staramr scans bacterial genome contigs for AMR genes and plasmids"
LABEL website="https://github.com/phac-nml/staramr"
LABEL license="https://github.com/phac-nml/staramr/blob/master/LICENSE"
LABEL maintainer1="Rachael St. Jacques"
LABEL maintainer1.email="rachael.stjacques@dgs.virginia.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get install -y \
 python3 \
 python3-pip \
 git \
 wget \
 libmoo-perl \
 liblist-moreutils-perl \
 libjson-perl \
 gzip \
 file

# blast 2.9.0 (blast in apt for ubuntu:bionic is v2.6.0 from 2017)
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.9.0/ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-2.9.0+-x64-linux.tar.gz && \
 rm ncbi-blast-2.9.0+-x64-linux.tar.gz 

# any2fasta
RUN cd /usr/local/bin && \
 wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
 chmod +x any2fasta

# mlst 2.19.0
# apt dependencies: wget libmoo-perl liblist-moreutils-perl libjson-perl gzip file
# also requires blast 2.9.0 or greater
RUN wget https://github.com/tseemann/mlst/archive/v2.19.0.tar.gz && \
 tar -xzf v2.19.0.tar.gz && \
 rm v2.19.0.tar.gz

# staramr 0.7.1
# pandas 0.25.3 is a hard requirement at the moment. see here for more info: https://github.com/phac-nml/staramr/issues/115
RUN pip3 install staramr==0.7.1 pandas==0.25.3 && \
 mkdir /data

# set $PATH and locale settings for singularity
ENV PATH="${PATH}:/mlst-2.19.0/bin:\
/ncbi-blast-2.9.0+/bin" \
    LC_ALL=C 

# update staramr default databases and print db info
RUN staramr db update -d && staramr db info

WORKDIR /data

##### staramr db information in container at time of docker image build #####
#resfinder_db_dir              = /usr/local/lib/python3.6/dist-packages/staramr/databases/data/update/resfinder
#resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
#resfinder_db_commit           = 7e1135b184abddea642fa2fd7c9322a33cb84810
#resfinder_db_date             = Fri, 24 Apr 2020 11:11
#pointfinder_db_dir            = /usr/local/lib/python3.6/dist-packages/staramr/databases/data/update/pointfinder
#pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
#pointfinder_db_commit         = 6323b5cfa383805938672a60988a597544cf9914
#pointfinder_db_date           = Fri, 30 Aug 2019 18:32
#plasmidfinder_db_dir          = /usr/local/lib/python3.6/dist-packages/staramr/databases/data/update/plasmidfinder
#plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
#plasmidfinder_db_commit       = acfd0096c01a4b03693b4a11374450f664d8d585
#plasmidfinder_db_date         = Thu, 02 Apr 2020 11:42
#mlst_version                  = 2.19.0
#pointfinder_gene_drug_version = 050218
#resfinder_gene_drug_version   = 050218.1
