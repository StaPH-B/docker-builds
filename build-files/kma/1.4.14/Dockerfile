ARG KMA_VER="1.4.14"

## Builder ##
FROM ubuntu:jammy as builder

ARG KMA_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  libz-dev \
  make \
  ca-certificates \
  git && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN git clone -b ${KMA_VER} --single-branch https://bitbucket.org/genomicepidemiology/kma.git &&\
  cd kma &&\
  make &&\
  mv kma kma_index kma_shm kma_update /usr/local/bin/

## App ##
FROM ubuntu:jammy as app

ARG KMA_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="kma"
LABEL software.version="$KMA_VER"
LABEL description="K-mer alignment of raw reads against a database"
LABEL website="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/kma/src/master/"
LABEL license.type="Apache License, V2.0"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/* /usr/local/bin/

ENV LC_ALL=C

CMD ["kma", "-h"]

WORKDIR /data

## Test ## 
FROM app as test 

RUN apt-get update && apt-get install -y --no-install-recommends wget

# Downloads E.coli genome and runs kma index on it
RUN wget -q --no-check-certificate https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/224/845/GCA_012224845.2_ASM1222484v2/GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
  gunzip GCA_012224845.2_ASM1222484v2_genomic.fna.gz && \
  kma index -i GCA_012224845.2_ASM1222484v2_genomic.fna -o database

# Downloads read files and uses them for kma mapping against database; print kma version
RUN wget -q --no-check-certificate ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_1.fastq.gz && \
  wget -q --no-check-certificate ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR690/006/SRR6903006/SRR6903006_2.fastq.gz && \
  kma -ipe SRR6903006_1.fastq.gz SRR6903006_2.fastq.gz -o test_output -t_db database -tmp /tmp/ && \
  kma -v
