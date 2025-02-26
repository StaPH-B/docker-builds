FROM ubuntu:jammy as app

ARG IRMA_VER="1.1.4"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="IRMA"
LABEL software.version=$IRMA_VER
LABEL description="IRMA was designed for the robust assembly, variant calling, and phasing of highly variable RNA viruses. Currently IRMA is deployed with modules for influenza, ebolavirus and coronavirus."
LABEL website="https://wonder.cdc.gov/amd/flu/irma/"
LABEL license="https://wonder.cdc.gov/amd/flu/irma/disclaimer.html"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    perl \
    r-base \
    unzip \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install IRMA
RUN wget https://wonder.cdc.gov/amd/flu/irma/flu-amd-202402.zip &&\
    unzip flu-amd-202402.zip &&\
    rm flu-amd-202402.zip

ENV PATH="${PATH}:/flu-amd" \
    LC_ALL=C

CMD ["IRMA"]

WORKDIR /data

## Test ##
FROM app as test

RUN cd /flu-amd/tests && \
    ./test_run.sh

RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR179/072/SRR17940172/SRR17940172_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR179/072/SRR17940172/SRR17940172_2.fastq.gz 

RUN IRMA FLU SRR17940172_1.fastq.gz SRR17940172_2.fastq.gz SRR17940172
