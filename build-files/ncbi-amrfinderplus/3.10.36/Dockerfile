FROM ubuntu:jammy as app

ARG AMRFINDER_VER="3.10.36"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="NCBI AMRFinderPlus"
LABEL software.version="${AMRFINDER_VER}"
LABEL description="NCBI resistance gene detection tool"
LABEL website="https://github.com/ncbi/amr"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Anders Goncalves da Silva"
LABEL maintainer3.email="andersgs@gmail.com"
LABEL maintainer4="Erin Young"
LABEL maintainer4.meail="eriny@utah.gov"

# ncbi-blast+ installed via apt is v2.12.0
# hmmer installed via apt is v3.3.2
RUN apt-get update && apt-get install -y --no-install-recommends \
 ca-certificates \
 wget \ 
 curl \
 make \
 g++ \
 ncbi-blast+ \
 hmmer && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

RUN mkdir amrfinder && cd /amrfinder && \
 wget https://github.com/ncbi/amr/releases/download/amrfinder_v${AMRFINDER_VER}/amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
 tar zxf amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
 rm amrfinder_binaries_v${AMRFINDER_VER}.tar.gz && \
 mkdir /data

# set PATH and locale settings for singularity compatibiliity
ENV PATH="${PATH}:\
/amrfinder"\
 LC_ALL=C

# download databases
RUN cd /amrfinder && amrfinder -u

WORKDIR /data

FROM app as test

RUN amrfinder -l

# from amrfinder
RUN amrfinder --plus -p /amrfinder/test_prot.fa -g  /amrfinder/test_prot.gff -O Escherichia > test_prot.got && \
  diff /amrfinder/test_prot.expected test_prot.got && \
  amrfinder --plus -n /amrfinder/test_dna.fa -O Escherichia > test_dna.got && \
  diff /amrfinder/test_dna.expected test_dna.got && \
  amrfinder --plus -n /amrfinder/test_dna.fa -p /amrfinder/test_prot.fa -g /amrfinder/test_prot.gff -O Escherichia > test_both.got && \
  diff /amrfinder/test_both.expected test_both.got

# external file
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
  gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz && \
  amrfinder --plus --nucleotide GCA_010941835.1_PDT000052640.3_genomic.fna --output test1.txt && \
  amrfinder --plus --nucleotide GCA_010941835.1_PDT000052640.3_genomic.fna --organism Salmonella --output test2.txt && \
  cat test1.txt test2.txt


