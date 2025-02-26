# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="OrthoFinder"
LABEL software.version="2.17"
LABEL description="Accurate inference of orthologous gene groups made easy"
LABEL website="https://github.com/davidemms/OrthoFinder"
LABEL license="https://github.com/davidemms/OrthoFinder/blob/master/License.md"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update && \
    apt-get -y install build-essential\
    wget \
    zip \
    unzip \
    mafft && \
    apt-get clean

# install fasttree
RUN wget http://www.microbesonline.org/fasttree/FastTree && \
  chmod +x FastTree && \
  mkdir fasttree && \
  mv FastTree fasttree/

# install iqtree
RUN wget https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz && \
  tar -xvf iqtree-1.6.12-Linux.tar.gz && \
  rm -rf iqtree-1.6.12-Linux.tar.gz

# install orthofinder
RUN wget https://github.com/davidemms/OrthoFinder/releases/download/2.3.7/OrthoFinder_glibc-2.17.tar.gz && \
  tar -xvf OrthoFinder_glibc-2.17.tar.gz && \
  rm -rf OrthoFinder_glibc-2.17.tar.gz

# install raxml HPC AVX
RUN wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz && \
  tar -xvf v8.2.12.tar.gz && \
  rm -rf v8.2.12.tar.gz && \
  cd standard-RAxML-8.2.12/ && \
  make -f Makefile.AVX.gcc && \
  rm *.o

# install raxml-ng
RUN wget https://github.com/amkozlov/raxml-ng/releases/download/0.9.0/raxml-ng_v0.9.0_linux_x86_64.zip && \
  unzip raxml-ng_v0.9.0_linux_x86_64.zip && \
  mkdir raxml_ng && \
  mv raxml-ng raxml_ng/ && \
  rm -rf raxml-ng_v0.9.0_linux_x86_64.zip

# install muscle
RUN wget http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz && \
  tar -xvf muscle3.8.31_i86linux64.tar.gz && \
  mkdir muscle && \
  mv muscle3.8.31_i86linux64 muscle/ && \
  rm -rf iqtree-1.6.12-Linux.tar.gz

# install mmseqs
RUN wget https://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz && \
  tar -xvf mmseqs-linux-avx2.tar.gz && \
  rm -rf mmseqs-linux-avx2.tar.gz && \
  /bin/bash -c "source /mmseqs/util/bash-completion.sh"

# add programs to path
ENV PATH="${PATH}:/fasttree:/iqtree-1.6.12-Linux/bin:standard-RAxML-8.2.12:/muscle:/raxml_ng:/mmseqs/bin:/mmseqs/util:/OrthoFinder:/OrthoFinder/bin"

WORKDIR /data
