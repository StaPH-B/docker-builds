#use ubuntu as base image
FROM ubuntu:xenial

#install java jre
RUN apt-get update && apt-get install -y\
 libz-dev\
 autoconf\
 automake\
 libtool\
 git\
 g++\
 make\
 libgsl-dev\
 libgsl2\
 curl

#RUN curl -O https://capnproto.org/capnproto-c++-0.7.0.tar.gz;\
RUN curl -O https://capnproto.org/capnproto-c++-0.6.1.tar.gz;\
 tar zxf capnproto-c++-0.6.1.tar.gz;\
 cd capnproto-c++-0.6.1;\
 ./configure;\
 make -j6 check;\
 make install

RUN git clone https://github.com/marbl/Mash.git

RUN cd /Mash; \
 ./bootstrap.sh; \
 ./configure; \
 make; \
 make install

COPY RefSeqSketchesDefaults.msh /RefSeqSketchesDefaults.msh
