#Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Lyve-SET"
LABEL software.version="2.0.1"
LABEL description="LYVE-SET, a method of using hqSNPs to create a phylogeny, especially for outbreak investigations"
LABEL website="https://github.com/lskatz/lyve-SET"
LABEL license="https://github.com/lskatz/lyve-SET/blob/master/LICENSE"

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>

#install dependencies
RUN apt-get update && apt-get install -y\
 perl\
 libfile-slurp-perl\
 openjdk-9-jre\
 bioperl\
 wget\
 libz-dev\
 git\
 libncurses5-dev\
 libncursesw5-dev\
 build-essential\
 ncbi-blast+\
 libsvn-perl\
 subversion\
 libsvn1\
 automake1.11\
 libpthread-stubs0-dev

#install edirect
RUN wget ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
RUN tar -xzvf edirect.tar.gz; rm edirect.tar.gz; cd edirect; ./setup.sh

#install smalt (at the time of this build lyve-SET was not building correctly)
RUN wget --max-redirect 50 --continue 'https://downloads.sourceforge.net/project/smalt/smalt-0.7.6-static.tar.gz' -O smalt-0.7.6-static.tar.gz
RUN tar -zxvf smalt-0.7.6-static.tar.gz; rm smalt-0.7.6-static.tar.gz;cd smalt-0.7.6; ./configure; make; make install

#get lyveset files
RUN wget https://github.com/lskatz/lyve-SET/archive/v2.0.1.tar.gz
RUN tar -xzvf v2.0.1.tar.gz;rm v2.0.1.tar.gz;mv lyve-SET-2.0.1 lyve-SET

#setup the lyveset filesystem
RUN cpan Test::Most\
         Bio::FeatureIO\
         String::Escape\
         Math::Round
RUN make -C /lyve-SET install -e PREFIX=/lyve-SET
RUN make -C /lyve-SET env -e PREFIX=/lyve-SET && \
    mkdir /data


ENV PATH="/lyve-SET:\
/lyve-SET/scripts:\
/edirect:\
${PATH}"

# set perl locale settings
ENV LC_ALL=C
WORKDIR /data
