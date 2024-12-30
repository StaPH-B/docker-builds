# base image
FROM ubuntu:bionic

# metadata
LABEL base.image="ubuntu:bionic"
LABEL container.version="1"
LABEL software="VIBRANT"
LABEL software.version="v1.2.1"
LABEL description=" a tool for automated recovery and annotation of bacterial and archaeal viruses, determination of genome completeness, and characterization of viral community function from metagenomic assemblies"
LABEL website="https://github.com/AnantharamanLab/VIBRANT"
LABEL license="https://github.com/AnantharamanLab/VIBRANT/blob/master/LICENSE"
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"

# install dependencies
RUN apt-get update && apt-get -y --no-install-recommends install \
    wget \
    gzip \
    unzip \
    tar \
    prodigal \
    hmmer \
    python3-pip \
    python3-setuptools \
    python3-biopython \
    python3-matplotlib && \
    #python3-numpy  \
    apt-get clean

#install more dependencies
RUN pip3 install seaborn==0.10.0 numpy==1.18.4 scikit-learn==0.21.3 pickle-mixin

#install the software
RUN wget https://github.com/AnantharamanLab/VIBRANT/archive/8a01435694ff016157a7e2a345ae353c8812d9cb.zip && \
    unzip 8a01435694ff016157a7e2a345ae353c8812d9cb.zip && \
    mv VIBRANT-8a01435694ff016157a7e2a345ae353c8812d9cb VIBRANT && \
    rm -rf 8a01435694ff016157a7e2a345ae353c8812d9cb.zip && \
    mkdir /data

#set path
ENV PATH="${PATH}:/VIBRANT" \
    LC_ALL=C

#install the databases
RUN chmod -R 777 VIBRANT/scripts && \
    chmod 777 VIBRANT/VIBRANT_run.py && \
    chmod 777 VIBRANT/databases/VIBRANT_setup.py && \
    cd VIBRANT/databases && \
    python3 VIBRANT_setup.py

WORKDIR /data
