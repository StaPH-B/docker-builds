# base ubuntu image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="SRA Toolkit"
LABEL software.version="2.9.2"
LABEL description="collection of tools and libraries for using data in the INSDC Sequence Read Archives"
LABEL website="https://github.com/ncbi/sra-tools"
LABEL license="https://github.com/ncbi/sra-tools/blob/master/LICENSE"

# Maintainer
MAINTAINER Curtis Kapsak <pjx8@cdc.gov>

# run update and install wget
RUN apt-get update && apt-get install -y wget && apt-get clean

# download sra-toolkit
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz &&\
   tar -xzf sratoolkit.2.9.2-ubuntu64.tar.gz &&\
   rm -r sratoolkit.2.9.2-ubuntu64.tar.gz &&\
   mkdir /data

ENV PATH="$PATH:/sratoolkit.2.9.2-ubuntu64/bin"
WORKDIR /data
