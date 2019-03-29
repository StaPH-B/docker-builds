FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1.1.0"
LABEL software="Serotypefinder"
LABEL software.version="1.1"
LABEL description="Tool for identifying the serotype of E. coli from reads or assemblies"
LABEL website="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# install dependencies
RUN apt-get update && apt-get install -y expat \
 apache2 \
 make \
 python \
 bzip2 \
 gcc \
 libextutils-pkgconfig-perl \
 libgd-perl \
 cpanminus \
 wget

# install legacy blast
RUN wget 'ftp://ftp.ncbi.nlm.nih.gov/blast/executables/legacy.NOTSUPPORTED/2.2.26/blast-2.2.26-x64-linux.tar.gz' &&\
  tar -xzf blast-2.2.26-x64-linux.tar.gz &&\
  rm blast-2.2.26-x64-linux.tar.gz

# download serotypefinder from git repo
COPY serotypefinder /serotypefinder

# install perl modules
RUN cpanm inc::latest \
 Module::Build \
 Data::Dumper \
 Getopt::Long \
 Try::Tiny::Retry \
 File::Temp \
 Clone \
 Convert::Binary::C \
 HTML::Entities \
 Data::Stag \
 Test::Most \
 CJFIELDS/BioPerl-1.6.924.tar.gz --force

# serotypefinder database is copied from local directory,
# since DL'ing from bitbucket requires ssh-key login and is ANNOYING
COPY database/ /serotypefinder/database
ENV PATH="${PATH}:/serotypefinder:/blast-2.2.26/bin"
RUN mkdir /data
# change working directory to /data so that it's not running in root / directory
WORKDIR /data

###### Path to legacy blast: /blast-2.2.26
###### Path to serotypefinder database: /serotypefinder/database
