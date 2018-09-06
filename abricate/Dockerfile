FROM ubuntu:xenial

# install dependencies
RUN apt-get update && apt-get install -y \
  emboss \
  bioperl \
  ncbi-blast+ \
  gzip \ 
  unzip \ 
  libjson-perl \
  libtext-csv-perl \
  libfile-slurp-perl \
  liblwp-protocol-https-perl \
  libwww-perl \
  git && apt-get clean

RUN git clone https://github.com/tseemann/abricate.git
ENV PATH="/abricate/bin:$PATH"

RUN abricate --check
RUN abricate --setupdb
