ARG BUSCO_VER="5.6.1"

FROM ubuntu:focal as app

ARG BUSCO_VER
ARG BBMAP_VER="39.01"
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
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
RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VER}.tar.gz &&\
    tar -xvf BBMap_${BBMAP_VER}.tar.gz && rm BBMap_${BBMAP_VER}.tar.gz &&\    
    mv /bbmap/* /usr/local/bin/

# sepp (greengenes version)
RUN wget https://raw.githubusercontent.com/smirarab/sepp-refs/54415e8905c5fa26cdd631c526b21f2bcdba95b5/gg/sepp-package.tar.bz &&\  
    tar xvfj sepp-package.tar.bz && rm sepp-package.tar.bz &&\
    cd sepp-package/sepp &&\
    python setup.py config -c && chmod 755 run_*

# busco
RUN wget https://gitlab.com/ezlab/busco/-/archive/${BUSCO_VER}/busco-${BUSCO_VER}.tar.gz &&\
    tar -xvf busco-${BUSCO_VER}.tar.gz && \
    rm busco-${BUSCO_VER}.tar.gz &&\
    cd busco-${BUSCO_VER} && \
    python3 setup.py install

# download bacteria_odb10
RUN busco --download bacteria_odb10    

ENV PATH="${PATH}:/sepp-package/sepp"
ENV LC_ALL=C

WORKDIR /data

CMD busco -h

## Tests ##
FROM app as test

# offline test
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
    gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz && \
    busco --offline -l /busco_downloads/lineages/bacteria_odb10 -m genome -i GCA_010941835.1_PDT000052640.3_genomic.fna -o offline --cpu 4 && \
    head offline/short_summary*.txt

# auto-lineage-prok
RUN busco -m genome -i GCA_010941835.1_PDT000052640.3_genomic.fna -o auto --cpu 4 --auto-lineage-prok && \
    head auto/short_summary*.txt
