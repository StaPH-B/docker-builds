# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="4"
LABEL description="An r environment and script for generating a genome cluster report"
LABEL website="https://github.com/AbigailShockey/reports"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"

# install ubuntu dependencies
RUN apt-get update && \
  apt-get -y install software-properties-common \
  apt-transport-https \
  ca-certificates \
  gnupg \
  curl \
  libcurl4-openssl-dev \
  libssl-dev \
  libxml2 \
  libxml2-dev \
  pandoc \
  pandoc-citeproc \
  wget \
  git \
  imagemagick \
  libmagick++-dev \
  texlive-latex-base \
  texlive-fonts-recommended \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-xetex \
  fonts-roboto \
  build-essential \
  libpcre2-dev \
  pcre2-utils

# add keys and ppa; update sources; build R dependencies
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9 && \
  add-apt-repository ppa:marutter/c2d4u3.5 && \
  echo "deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/" >> /etc/apt/sources.list && \
  cp /etc/apt/sources.list /etc/apt/sources.list~ && \
  sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list && \
  apt-get update && apt-get -y upgrade && apt-get -y build-dep r-base

#Install R 4.0.1 from source
RUN wget https://cran.r-project.org/src/base/R-4/R-4.0.1.tar.gz && \
  tar -xvf R-4.0.1.tar.gz && \
  cd R-4.0.1 && \
  ./configure --prefix=/bin/R/4.0.1 --enable-R-shlib && \
  make && \
  make install

ENV PATH "$PATH:/bin/R/4.0.1/bin"

# install R packages
RUN R -e "install.packages(c('knitr',\
  'rmarkdown',\
  'tidyverse',\
  'devtools',\
  'mnormt',\
  'phytools',\
  'viridisLite',\
  'viridis'), repos = 'http://cran.us.r-project.org')" && \
  R -e "devtools::install_github('AbigailShockey/ggtree')" && \
  R -e "tinytex::install_tinytex()"

# install report repository
RUN git clone -n https://github.com/AbigailShockey/reports.git && \
  cd reports/ && \
  git checkout 90ec4a0

WORKDIR /data
ENV PATH "$PATH:/bin/R/4.0.1/bin:/reports"
