FROM ubuntu:focal as app

ARG BUSCO_VER="5.4.7"
ARG BBMAP_VER="39.01"
ARG BLAST_VER="2.14.0"
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="BUSCO"
LABEL software.version="${BUSCO_VER}"
LABEL description="Assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs"
LABEL website="https://busco.ezlab.org/"
LABEL license="https://gitlab.com/ezlab/busco/-/raw/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    python3-biopython \
    python3-pandas \
    python3-setuptools\ 
    hmmer \   
    prodigal \    
    augustus \
    r-cran-ggplot2 \      
    gcc-x86-64-linux-gnu \
    default-jre \ 
    libjenkins-json-java \
    libgoogle-gson-java \
    libjson-java \
    && rm -rf /var/lib/apt/lists/* && apt-get autoclean \
    && ln -s /usr/bin/python3 /usr/bin/python

# install other necessary tools 
# blast
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.14.0/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz &&\
    tar -xvf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz
# sepp (greengenes version)
RUN wget https://raw.githubusercontent.com/smirarab/sepp-refs/54415e8905c5fa26cdd631c526b21f2bcdba95b5/gg/sepp-package.tar.bz &&\  
    tar xvfj sepp-package.tar.bz && rm sepp-package.tar.bz &&\
    cd sepp-package/sepp &&\
    python setup.py config -c && chmod 755 run_*
# bbtools
RUN wget https://sourceforge.net/projects/bbmap/files/BBMap_${BBMAP_VER}.tar.gz &&\
    tar -xvf BBMap_${BBMAP_VER}.tar.gz && rm BBMap_${BBMAP_VER}.tar.gz &&\    
    mv /bbmap/* /usr/local/bin/
# metaeuk
RUN wget https://github.com/soedinglab/metaeuk/releases/download/6-a5d39d9/metaeuk-linux-sse41.tar.gz &&\
    tar -xvf metaeuk-linux-sse41.tar.gz && rm metaeuk-linux-sse41.tar.gz &&\
    mv  /metaeuk/bin/* /usr/local/bin/

# and finally busco
RUN wget https://gitlab.com/ezlab/busco/-/archive/${BUSCO_VER}/busco-${BUSCO_VER}.tar.gz &&\
    tar -xvf busco-${BUSCO_VER}.tar.gz && \
    rm busco-${BUSCO_VER}.tar.gz &&\
    cd busco-${BUSCO_VER} && \
    python3 setup.py install

ENV AUGUSTUS_CONFIG_PATH="/usr/share/augustus/config/"
ENV PATH="${PATH}:/ncbi-blast-${BLAST_VER}+/bin:/sepp-package/sepp:/usr/share/augustus/scripts"
ENV LC_ALL=C

WORKDIR /data

CMD busco -h

## Tests ##
FROM app as test
# run tests for bacteria and eukaryota
RUN busco -i /busco-5.4.7/test_data/bacteria/genome.fna -c 8 -m geno -f --out test_bacteria
RUN busco -i /busco-5.4.7/test_data/eukaryota/genome.fna -c 8 -m geno -f --out test_eukaryota
RUN busco -i /busco-5.4.7/test_data/eukaryota/genome.fna -l eukaryota_odb10 -c 8 -m geno -f --out test_eukaryota_augustus --augustus

# generate plot
RUN mkdir my_summaries &&\
    find . -name "short_summary.*.txt" -exec cp {} my_summaries \; &&\
    python3 /busco-5.4.7/scripts/generate_plot.py -wd my_summaries

# using actual data (Salmonella genome)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
    gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz && \
    busco -m genome -i GCA_010941835.1_PDT000052640.3_genomic.fna -o busco_GCA_010941835.1 --cpu 4 --auto-lineage-prok && \
    head busco_GCA_010941835.1/short_summary*.txt
