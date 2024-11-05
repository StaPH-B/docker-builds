ARG BUSCO_VER="5.8.0"

FROM ubuntu:jammy AS app

ARG BUSCO_VER
ARG BBMAP_VER="39.10"
ARG SEPP_VER="4.5.5"
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="BUSCO"
LABEL software.version="${BUSCO_VER}"
LABEL description="Slim version of BUSCO for prokaryotes only"
LABEL website="https://busco.ezlab.org/"
LABEL license="https://gitlab.com/ezlab/busco/-/raw/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python3-pip \
    python3-setuptools \
    python3-requests \
    python3-pandas \
    hmmer \   
    prodigal \
    lbzip2 \ 
    openjdk-8-jre-headless \ 
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean \
    && ln -s /usr/bin/python3 /usr/bin/python

# BioPython (python3-biopython installs 1.73. It causes python error in this version)
RUN pip install --no-cache-dir biopython

# bbtools
RUN wget -q https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VER}.tar.gz &&\
    tar -xvf BBMap_${BBMAP_VER}.tar.gz && rm BBMap_${BBMAP_VER}.tar.gz &&\    
    mv /bbmap/* /usr/local/bin/

# sepp 
RUN wget https://github.com/smirarab/sepp/archive/refs/tags/v${SEPP_VER}.tar.gz &&\
    tar -xvf v${SEPP_VER}.tar.gz && rm v${SEPP_VER}.tar.gz &&\
    cd sepp-${SEPP_VER} &&\
    python setup.py config -c && python setup.py install

# busco
RUN wget -q https://gitlab.com/ezlab/busco/-/archive/${BUSCO_VER}/busco-${BUSCO_VER}.tar.gz &&\
    tar -xvf busco-${BUSCO_VER}.tar.gz && \
    rm busco-${BUSCO_VER}.tar.gz &&\
    cd busco-${BUSCO_VER} && \
    python3 setup.py install

# download bacteria_odb10
RUN busco --download bacteria_odb10    

ENV LC_ALL=C

WORKDIR /data

CMD busco -h

## Tests ##
FROM app AS test

RUN busco -h

# offline test
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
    gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz && \
    busco --offline -l /busco_downloads/lineages/bacteria_odb10 -m genome -i GCA_010941835.1_PDT000052640.3_genomic.fna -o offline --cpu 4 && \
    head offline/short_summary*.txt

# auto-lineage-prok
RUN busco -m genome -i GCA_010941835.1_PDT000052640.3_genomic.fna -o auto --cpu 4 --auto-lineage-prok && \
    head auto/short_summary*.txt
