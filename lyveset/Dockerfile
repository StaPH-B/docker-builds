#Use ubuntu as base image
FROM ubuntu:xenial

#install python
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

#get lyveset files
RUN git clone https://github.com/lskatz/lyve-SET.git

#setup the lyveset filesystem
RUN cpan Test::Most
RUN cpan Bio::FeatureIO
RUN cpan String::Escape
RUN make -C /lyve-SET install -e PREFIX=/lyve-SET
RUN make -C /lyve-SET env -e PREFIX=/lyve-SET


ENV PATH="/lyve-SET:\
/lyve-SET/scripts:\
${PATH}"
