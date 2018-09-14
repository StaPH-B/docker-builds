FROM ubuntu:xenial

LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Serotypefinder"
LABEL software.version="1.1"
LABEL description="Tool for identifying the serotype of E. coli from reads or assemblies"
LABEL website="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/serotypefinder/src/master/"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# install dependencies
RUN apt-get update && apt-get install -y expat \
 apache2 \
 make \
 wget \
 curl \
 git \
 python \
 bzip2 \
 gcc \
 libextutils-pkgconfig-perl \
 libgd-perl 

# so that all install commands following this shell command are all done from a bash shell and not /bin/sh
SHELL ["/bin/bash", "-cl"]

# install perlbrew
RUN curl -L http://install.perlbrew.pl | bash; source /root/perl5/perlbrew/etc/bashrc; perlbrew init; sed -i '4isource ~/perl5/perlbrew/etc/bashrc' /root/.bashrc
RUN perlbrew install perl-5.23.0; perlbrew switch perl-5.23.0; perlbrew install-cpanm

# install legacy blast
# of course, on the day that I'm developing this container, NCBI decides to remove the old version of blast+
# I'm going to copy it over from my local machine and make the files available through the git repo.....sigh.
# RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.26/ncbi-blast-2.2.26+-x64-linux.tar.gz && tar -xzf ncbi-blast-2.2.26+-x64-linux.tar.gz && mv ncbi-blast-2.2.26+ /opt/ && rm ncbi-blast-2.2.26+-x64-linux.tar.gz
COPY blast-2.2.26/ /opt/blast-2.2.26
# download serotypefinder 
RUN git clone https://bitbucket.org/genomicepidemiology/serotypefinder.git && echo 'export PATH=/serotypefinder/:$PATH' >> ~/.bashrc
# install perl modules
RUN cpanm inc::latest Module::Build \
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
ENV PATH="/serotypefinder:${PATH}"

###### NOTE: Due to the way that serotypefinder was installed in this container,
###### and the way that Docker containers run, the following format must be used
###### to run the serotypefinder.pl script correctly:
###### docker run <docker flags> staphb/serotypefinder /bin/bash -cl "serotypefinder.pl <flags>"

###### Path to legacy blast: /opt/blast-2.2.26
###### Path to serotypefinder database: /serotypefinder/database
