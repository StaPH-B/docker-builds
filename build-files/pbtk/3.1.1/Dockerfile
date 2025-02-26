FROM ubuntu:jammy as app 

ARG PBTK_VER="3.1.1"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pbtk"
LABEL software.version="${PBTK_VER}"
LABEL description="PacBio BAM toolkit"
LABEL website="https://github.com/PacificBiosciences/pbtk"
LABEL license="https://github.com/PacificBiosciences/pbtk/blob/main/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends  -y \
    wget &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/PacificBiosciences/pbtk/releases/download/v${PBTK_VER}/pbtk.tar.gz &&\
    tar -C /usr/local/bin/ -xvf pbtk.tar.gz &&\
    rm pbtk.tar.gz

ENV LC_ALL=C

CMD bam2fasta -h;\
    bam2fastq -h;\ 
    ccs-kinetics-bystrandify -h;\
    extracthifi -h;\
    pbindex -h;\
    pbindexdump -h;\
    pbmerge -h;\
    zmwfilter -h

WORKDIR /data

## Test ##
FROM app as test

RUN wget -q --no-check-certificate https://downloads.pacbcloud.com/public/dataset/HiFiViral/Nov_2021/m64012_210821_095651.hifi_reads.bam
    
RUN pbindex m64012_210821_095651.hifi_reads.bam &&\
    zmwfilter --include 1,2,4,8,16 m64012_210821_095651.hifi_reads.bam test.bam &&\
    zmwfilter --include 18,19,22,24,33 m64012_210821_095651.hifi_reads.bam test2.bam &&\
    pbindex test.bam &&\
    pbindexdump test.bam.pbi > test.json &&\
    bam2fasta -o test test.bam &&\
    bam2fastq -o test test.bam &&\
    extracthifi test.bam test.hifi.bam &&\
    ccs-kinetics-bystrandify test.bam test.bystrand.bam &&\
    pbmerge test.bam test2.bam > test.merged.bam &&\
    echo $(ls | grep test)