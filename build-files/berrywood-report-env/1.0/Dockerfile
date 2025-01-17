# base image
FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL description="An r environment and script for generating a berrywood report"
LABEL website="N/A"
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"

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
  fonts-roboto

# add keys and ppa; update sources; install latest version of R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9 && \
  add-apt-repository ppa:marutter/c2d4u3.5 && \
  echo "deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/" >> /etc/apt/sources.list && \
  apt-get update && apt-get -y upgrade && apt-get -y install r-base \
  r-base-dev

# install R packages
RUN R -e "install.packages(c('cowplot',\
  'ggplot2',\
  'ggsci',\
  'grid',\
  'gridExtra',\
  'optparse',\
  'stringr',\
  'sjPlot',\
  'longtable',\
  'dplyr',\
  'xtable'), repos = 'http://cran.us.r-project.org')"

# install report repository
RUN mkdir data

WORKDIR /data
