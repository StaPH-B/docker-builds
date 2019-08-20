FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1.0.0"
LABEL software="Abricate"
LABEL software.version="0.8.13"
LABEL description="Mass screening of contigs for AMR or virulence genes"
LABEL website="https://github.com/tseemann/abricate"
LABEL license="https://github.com/tseemann/abricate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install dependencies
RUN apt-get update && apt-get install -y \
  bzip2 \
  emboss \
  bioperl \
  ncbi-blast+ \
  gzip \
  unzip \
  libjson-perl \
  libtext-csv-perl \
  libfile-slurp-perl \
  liblwp-protocol-https-perl \
  libwww-perl \
  git \
  wget && apt-get clean && apt-get autoclean

# edirect needed for updating dbs
RUN wget ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz &&\
    tar -xzvf edirect.tar.gz &&\
    rm edirect.tar.gz &&\
    cd edirect &&\
    ./setup.sh

RUN wget https://github.com/tseemann/abricate/archive/v0.8.13.tar.gz &&\
    tar -zxvf v0.8.13.tar.gz &&\
    rm -rf v0.8.13.tar.gz
ENV PATH="/abricate-0.8.13/bin:/edirect:$PATH"

RUN abricate --check &&\
    abricate --setupdb &&\
    mkdir /data

RUN abricate-get_db --db plasmidfinder --force &&\
abricate-get_db --db vfdb --force &&\
abricate-get_db --db ecoh --force &&\
abricate-get_db --db card --force &&\
abricate-get_db --db ecoli_vf --force &&\
abricate-get_db --db ncbi --force &&\
abricate-get_db --db resfinder --force 
## commented out because the argannot link is broken, Torsten hasn't put the fix in a release yet
#abricate-get_db --db argannot --force 


# set perl locale settings
ENV LC_ALL=C

WORKDIR /data
