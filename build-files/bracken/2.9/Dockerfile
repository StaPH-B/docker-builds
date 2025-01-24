ARG KRAKEN_VER="2.1.3"
ARG BRACKEN_VER="2.9"

## Builder ##
FROM ubuntu:jammy as builder

ARG KRAKEN_VER
ARG BRACKEN_VER

RUN apt-get update && apt-get install -y build-essential perl wget zlib1g-dev

# install Kraken2
RUN wget https://github.com/DerrickWood/kraken2/archive/refs/tags/v${KRAKEN_VER}.tar.gz &&\
    tar -xvf v${KRAKEN_VER}.tar.gz &&\
    cd kraken2-${KRAKEN_VER} &&\
    ./install_kraken2.sh /kraken2
# install Bracken
RUN wget https://github.com/jenniferlu717/Bracken/archive/refs/tags/v${BRACKEN_VER}.tar.gz &&\
    tar -xvf v${BRACKEN_VER}.tar.gz && rm v${BRACKEN_VER}.tar.gz &&\
    cd Bracken-${BRACKEN_VER} &&\
    chmod 755 install_bracken.sh && ./install_bracken.sh

## App ##
FROM ubuntu:jammy as app

ARG BRACKEN_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Bracken"
LABEL software.version=${BRACKEN_VER}
LABEL description="Bracken: estimating species abundance in metagenomics data"
LABEL website="https://github.com/jenniferlu717/Bracken"
LABEL license="https://github.com/jenniferlu717/Bracken/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y perl python-is-python3 libgomp1 pigz \
&& rm -rf /var/lib/apt/lists/* && apt-get autoclean

COPY --from=builder /kraken2 /kraken2
COPY --from=builder /Bracken-${BRACKEN_VER} /Bracken

ENV LC_ALL=C
ENV PATH="${PATH}:/kraken2:/Bracken"

CMD [ "bracken", "-h" ]

WORKDIR /data

## Test ##
FROM app as test

RUN apt-get update && apt-get install --no-install-recommends -y wget

# get kraken/bracken database
RUN wget --no-check-certificate https://genome-idx.s3.amazonaws.com/kraken/k2_viral_20231009.tar.gz && \
    mkdir db && tar -C db -xvf k2_viral_20231009.tar.gz

# download and classify SARS-CoV-2 reads
RUN wget --no-check-certificate https://github.com/StaPH-B/docker-builds/raw/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_1.fastq.gz \
    https://github.com/StaPH-B/docker-builds/raw/83ee344304794f4ffa162d1c082bb35f916badcf/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    kraken2 --db ./db --paired --report k2_report.txt SRR13957123_1.fastq.gz SRR13957123_2.fastq.gz

# make abundance estimation with bracken
RUN bracken -d ./db -i k2_report.txt -o bracken_report.txt -r 75 -l S -t 10 && \
    cat bracken_report.txt
