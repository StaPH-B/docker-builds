#Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="2"
LABEL software="Lyve-SET"
LABEL software.version="1.1.4f"
LABEL description="LYVE-SET, a method of using hqSNPs to create a phylogeny, especially for outbreak investigations"
LABEL website="https://github.com/lskatz/lyve-SET"
LABEL license="https://github.com/lskatz/lyve-SET/blob/master/LICENSE"

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

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
 libpthread-stubs0-dev\
 cpanminus\
 mpich

#install edirect
RUN wget ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz &&\
    tar -xzvf edirect.tar.gz &&\
    rm edirect.tar.gz &&\
    cd edirect &&\
    ./setup.sh

#install smalt (at the time of this build lyve-SET was not building correctly)
RUN wget --max-redirect 50 --continue 'https://downloads.sourceforge.net/project/smalt/smalt-0.7.6-static.tar.gz' -O smalt-0.7.6-static.tar.gz &&\
    tar -zxvf smalt-0.7.6-static.tar.gz &&\
    rm smalt-0.7.6-static.tar.gz &&\
    cd smalt-0.7.6 &&\
    ./configure &&\
    make &&\
    make install

#get lyveset files
RUN wget https://github.com/lskatz/lyve-SET/archive/v1.1.4f.tar.gz &&\
    tar -xzvf v1.1.4f.tar.gz &&\
    rm v1.1.4f.tar.gz &&\
    mv lyve-SET-1.1.4f lyve-SET

# download perl modules, setup the lyveset filesystem
RUN cpanm Test::Most Bio::FeatureIO String::Escape File::Slurp URI::Escape Math::Round
RUN make -C /lyve-SET install -e PREFIX=/lyve-SET &&\
    make -C /lyve-SET env -e PREFIX=/lyve-SET


ENV PATH="/lyve-SET:\
/lyve-SET/scripts:\
/edirect:\
${PATH}"

# set perl locale settings for singularity
ENV LC_ALL=C
