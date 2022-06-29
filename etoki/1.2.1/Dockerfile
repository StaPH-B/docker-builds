# FYI this is a multistage build, which can get very complicated

ARG ETOKI_VER="1.2.1"
ARG SKESA_VER=2.4.0
ARG SPADES_VER=3.15.4
ARG SHOVILL_VER=1.1.0
ARG KRAKEN2_VER=2.1.2-no-db
ARG BOWTIE_VER=2.4.4
ARG LYVESET_VER=1.1.4f
#ARG VSEARCH_VER=2.21.1
ARG BBTOOLS_VER=38.96
#ARG MLST_VER=2.19.0
ARG ORTHOFINDER_VER=2.17
ARG CFSAN_VER=2.0.2
ARG FLYE_VER=2.9
ARG SAMTOOLS_VER=1.15
ARG DIAMOND_VER="v2.0.15"
ARG RAXML_VER="8.2.12"

FROM staphb/shovill:${SHOVILL_VER}          AS shovill
FROM staphb/kraken2:${KRAKEN2_VER}          AS kraken2
FROM staphb/bowtie2:${BOWTIE_VER}           AS bowtie2
FROM staphb/lyveset:${LYVESET_VER}          AS lyveset
FROM staphb/bbtools:${BBTOOLS_VER}          AS bbtools
#FROM staphb/mlst:${MLST_VER}                AS mlst
#FROM staphb/orthofinder:${ORTHOFINDER_VER}  AS orthofinder
FROM staphb/cfsan-snp-pipeline:${CFSAN_VER} AS cfsan
FROM staphb/flye:${FLYE_VER}                AS flye
FROM staphb/samtools:${SAMTOOLS_VER}        AS samtools
FROM staphb/raxml:${RAXML_VER}              AS raxml

FROM ubuntu:jammy as app

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="EToKi"
LABEL software.version=$ETOKI_VER
LABEL description="All methods related to Enterobase data analysis pipelines"
LABEL website="https://github.com/zheminzhou/EToKi"
LABEL license="https://github.com/zheminzhou/EToKi/blob/master/LICENSE"
LABEL maintainer="Lee Katz"
LABEL maintainer.email="gzu2@cdc.gov"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 perl-base \
 libcurl4-gnutls-dev \
 gcc \
 g++ \
 python-setuptools \
 zlib1g-dev \
 libbz2-dev \
 python-is-python3 \
 python3-pip \
 python3-dev \
 libgconf-2-4 \
 curl \
 unzip \
 build-essential \
 git \
 pigz \
 libcurl4 \
 ant \
 libssl-dev \
 python3-venv \
 autoconf \
 automake \
 make \
 wget \
 mmseqs2 \
 ncbi-blast+ && \
 apt-get autoclean && \
 rm -rf /var/lib/apt/lists/*

RUN pip3 install ete3 numba pandas scikit-learn psutil click scipy numpy==1.21.6

COPY --from=shovill     /skesa/skesa            /usr/local/bin/
COPY --from=shovill     /megahit                /megahit
COPY --from=shovill     /pilon                  /pilon
COPY --from=shovill     /SPAdes-*-Linux         /spades
COPY --from=kraken2     /kraken2-2*             /kraken2
COPY --from=kraken2     /kraken2-db             /kraken2-db
COPY --from=bowtie2     /opt/bowtie2-*          /opt/bowtie2
COPY --from=bbtools     /opt/bbmap              /opt/bbmap
#COPY --from=mlst        /ncbi-blast-2.9.0+      /ncbi-blast-2.9.0+
COPY --from=lyveset     /lyve-SET               /lyve-SET
#COPY --from=orthofinder /mmseqs                 /mmseqs
COPY --from=cfsan       /gatk                   /gatk
COPY --from=flye        /Flye-*                 /flye
COPY --from=samtools    /samtools-*             /samtools
COPY --from=raxml       /standard-RAxML-8.2.12  /standard-RAxML
COPY --from=raxml       /raxml_ng               /raxml_ng

ARG DIAMOND_VER
ARG ETOKI_VER
#ARG VSEARCH_VER

# Diamond
RUN wget https://github.com/bbuchfink/diamond/releases/download/${DIAMOND_VER}/diamond-linux64.tar.gz && \
 tar zxvf diamond-linux64.tar.gz && \
 mv -v diamond /usr/local/bin/diamond && \
 chmod +x /usr/local/bin/diamond && \
 rm diamond-linux64.tar.gz

# mmseqs
#RUN wget https://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz && \
#RUN wget --no-check-certificate --secure-protocol=TLSv1_2 --debug -v --auth-no-challenge http://mmseqs.com/latest/mmseqs-linux-avx2.tar.gz && \
#  tar -xvf mmseqs-linux-avx2.tar.gz && \
#  rm -rf mmseqs-linux-avx2.tar.gz && \
#  /bin/bash -c "source /mmseqs/util/bash-completion.sh"


ENV PATH="/usr/local/bin:/EToKi-${ETOKI_VER}:/flye/bin:/megahit:/pilon:/spades/bin:/kraken2:/opt/bowtie2:/opt/bbmap:/ncbi-blast-2.9.0+/bin:/megahit/megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin:/raxml_ng:/standard-RAxML:/lyve-SET:/lyve-SET/scripts:/mmseqs/bin:/mmseqs/util:$PATH" \
   LC_ALL=C

# Test many executables
#RUN mmseqs --version
#RUN flye --version
#RUN samtools --help
#RUN diamond --help && diamond --version

# Vsearch sort of copied from https://github.com/torognes/vsearch/blob/v2.21.1/Dockerfile
#WORKDIR /opt
#RUN git clone https://github.com/torognes/vsearch.git && cd vsearch && git checkout v${VSEARCH_VER}
#WORKDIR /opt/vsearch
#RUN ./autogen.sh && \
    #./configure CFLAGS="-O3" CXXFLAGS="-O3" && \
    #make clean && \
    #make && \
    #make install && \
    #make clean && \
    #cd .. && \
    #rm -rf /opt/vsearch

WORKDIR /

## EToKi itself ##
#RUN wget https://github.com/zheminzhou/EToKi/archive/refs/tags/${ETOKI_VER}.tar.gz && \
#  ls / && \
#  tar zxvf ${ETOKI_VER}.tar.gz && \
#  rm ${ETOKI_VER}.tar.gz
# TODO checkout a specific tag or hashtag
RUN wget https://github.com/lskatz/EToKi/archive/refs/tags/${ETOKI_VER}.tar.gz && \
 tar zxvf ${ETOKI_VER}.tar.gz

#RUN git clone https://github.com/lskatz/EToKi.git /EToKi-${ETOKI_VER} && \
# cd /EToKi-${ETOKI_VER} && \
# git checkout 1.2.1 && \
# cd -

WORKDIR /EToKi-${ETOKI_VER}

RUN EToKi.py configure --help

RUN EToKi.py configure --path bbduk=/opt/bbmap/bbduk.sh 
RUN EToKi.py configure --path bbmerge=$(which bbmerge.sh) 
RUN EToKi.py configure --path bbduk=/opt/bbmap/bbduk.sh 
RUN EToKi.py configure --path bbmerge=$(which bbmerge.sh) 
RUN EToKi.py configure --path repair=$(which repair.sh) 
RUN EToKi.py configure --path pilon=$(find /pilon -name 'pilon-*.jar' |  head -n 1) 
RUN EToKi.py configure --path flye=$(which flye) 
RUN EToKi.py configure --path kraken2=$(find /kraken2 -type f -name kraken2 | head -n 1) 
RUN EToKi.py configure --path bowtie2=$(which bowtie2) 
RUN EToKi.py configure --path bowtie2build=$(which bowtie2-build) 
RUN EToKi.py configure --path raxml=$(which raxmlHPC) 
RUN EToKi.py configure --path raxml_ng=$(which raxml-ng) 
RUN EToKi.py configure --path samtools=$(which samtools) 
RUN EToKi.py configure --path blastn=$(which blastn) 
RUN EToKi.py configure --path blastp=$(which blastp) 
RUN EToKi.py configure --path makeblastdb=$(which makeblastdb) 
RUN EToKi.py configure --path diamond=$(which diamond) 
RUN EToKi.py configure --path gatk=/gatk/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef/GenomeAnalysisTK.jar 
RUN EToKi.py configure --path mmseqs=$(which mmseqs) 
RUN EToKi.py configure --path megahit=$(which megahit) 
RUN EToKi.py configure --path spades=$(which spades.py) 
# In the LK version, we are emulating usearch with blastp
RUN EToKi.py configure --usearch $(which blastp)

WORKDIR /data

FROM app as test

ARG ETOKI_VER

WORKDIR /EToKi-${ETOKI_VER}
# Get the help menu up
RUN EToKi.py --help
# Show the configuration works
RUN EToKi.py configure  

ENV MLSTdb="/EToKi-${ETOKI_VER}/examples/Escherichia.Achtman.alleles.fasta"
ENV MLSTalleles="/EToKi-${ETOKI_VER}/examples/Escherichia.Achtman.alleles.fasta"
ENV MLSTtab="/EToKi-${ETOKI_VER}/examples/Escherichia.Achtman.convert.tab"
ENV ECOLI_assembly="/EToKi-${ETOKI_VER}/examples/GCF_000005845.2_ASM584v2_genomic.fna"
ENV ECOLI_assembly2="/EToKi-${ETOKI_VER}/examples/GCF_000214765.2_ASM21476v3_genomic.fna"
ENV ECOLI_assembly3="/EToKi-${ETOKI_VER}/examples/GCF_001566635.1_ASM156663v1_genomic.fna"
RUN gunzip -vf ${ECOLI_assembly} ${ECOLI_assembly2} ${ECOLI_assembly3}

# Try out MLST
RUN EToKi.py MLSTdb -i ${MLSTalleles} -r ${MLSTdb} -d ${MLSTtab}
# Show some results of the database creation
RUN ls -lh $MLSTdb $MLSTalleles $MLSTtab && head ${MLSTalleles} ${MLSTdb} ${MLSTtab}
# Run typing
RUN EToKi.py MLSType -i ${ECOLI_assembly3} -r ${MLSTdb} -k G749 -o stdout -d ${MLSTtab}

# Return the fasta files back to gzip status
RUN gzip -vf ${ECOLI_assembly} ${ECOLI_assembly2} ${ECOLI_assembly3}

# Just take the examples of unit tests that are most relevant to MLST
# from example.bash in the repo
#RUN python EToKi.py MLSTdb -i examples/Escherichia.Achtman.alleles.fasta -r examples/Escherichia.Achtman.references.fasta -d examples/Escherichia.Achtman.convert.tab
#RUN gzip -cd examples/GCF_001566635.1_ASM156663v1_genomic.fna.gz > examples/GCF_001566635.1_ASM156663v1_genomic.fna && \



