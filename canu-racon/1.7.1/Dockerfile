#Use ubuntu as base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Canu, Minimap2, Racon"
LABEL software.version="1.7.1"
LABEL description="Long read assembly and polishing tools"
LABEL website="https://github.com/marbl/canu;https://github.com/lh3/minimap2;https://github.com/isovic/racon"
LABEL license="See program repositories"

MAINTAINER Nicholas Florek <nicholas.florek@slh.wisc.edu>

#install python
RUN apt-get update && apt-get install -y\
 perl\
 default-jre\
 gnuplot\
 libgcc-5-dev\
 libgomp1\
 maven\
 git\
 wget\
 python3\
 build-essential\
 cmake\
 zlib1g-dev
 

#install software
RUN wget https://github.com/marbl/canu/archive/v1.7.1.tar.gz
RUN tar -xzvf v1.7.1.tar.gz;rm v1.7.1.tar.gz;cd canu-1.7.1/src;make -j 8
RUN git clone --recursive https://github.com/isovic/racon.git racon
RUN cd racon; mkdir build;cd build; cmake -DCMAKE_BUILD_TYPE=Release -Dracon_build_wrapper=ON .. ; make
RUN git clone https://github.com/lh3/minimap2; cd minimap2; make

ENV PATH="/canu-1.7.1/Linux-amd64/bin/:/racon/build/bin:/minimap2:${PATH}"
