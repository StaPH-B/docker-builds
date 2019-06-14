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

MAINTAINER Kelsey Florek <kelsey.florek@slh.wisc.edu>

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


#install canu
RUN wget https://github.com/marbl/canu/archive/v1.7.1.tar.gz
RUN tar -xzvf v1.7.1.tar.gz;rm v1.7.1.tar.gz;cd canu-1.7.1/src;make -j 8

#install racon
RUN wget https://github.com/isovic/racon/releases/download/1.3.1/racon-v1.3.1.tar.gz
RUN mkdir racon; tar -xzvf racon-v1.3.1.tar.gz -C racon --strip-components 1; rm racon-v1.3.1.tar.gz
RUN cd racon; mkdir build; cd build; cmake -DCMAKE_BUILD_TYPE=Release ../
RUN cd racon/build/; make; make install

#install minimap2
RUN git clone https://github.com/lh3/minimap2; cd minimap2; git checkout v2.13; make

ENV PATH="/canu-1.7.1/Linux-amd64/bin/:/racon/build/bin:/minimap2:${PATH}"
