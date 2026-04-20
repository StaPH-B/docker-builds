FROM ubuntu:noble AS app

ARG FASTP_VER="1.3.2"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="fastp"
LABEL software.version="${FASTP_VER}"
LABEL description="An ultra-fast all-in-one FASTQ preprocessor"
LABEL website="https://github.com/OpenGene/fastp"
LABEL license="https://github.com/OpenGene/fastp/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

WORKDIR /usr/local/bin

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    jq \
    python3 \
    python-is-python3 \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget http://opengene.org/fastp/fastp.${FASTP_VER} && \
    mv fastp.${FASTP_VER} fastp && \
    chmod a+x ./fastp

RUN wget https://raw.githubusercontent.com/OpenGene/fastp/v${FASTP_VER}/parallel.py \
    -O /usr/local/bin/parallel.py && \
    chmod +x /usr/local/bin/parallel.py

ENV LC_ALL=C

WORKDIR /data

CMD [ "fastp", "--help" ]



FROM app AS test

WORKDIR /test


RUN fastp --help && \
    fastp --version

RUN jq --help && \
    jq --version

RUN parallel.py -h

# downloading sars-cov-2 fastq test files
RUN wget -q \
    https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz \
    https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz

# running fastp on the files
RUN fastp \
    -i SRR13957123_1.fastq.gz \
    -I SRR13957123_2.fastq.gz \
    -o SRR13957123_PE1.fastq.gz \
    -O SRR13957123_PE2.fastq.gz \
    -h SRR13957123_fastp.html \
    -j SRR13957123_fastp.json