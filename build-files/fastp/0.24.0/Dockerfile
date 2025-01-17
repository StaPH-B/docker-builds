FROM ubuntu:jammy as app

ARG FASTP_VER="0.24.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Fastp"
LABEL software.version=${FASTP_VER}
LABEL description="An ultra-fast all-in-one FASTQ preprocessor"
LABEL website="https://github.com/OpenGene/fastp"
LABEL license="https://github.com/OpenGene/fastp/blob/master/LICENSE"
LABEL maintainer="Idowu Olawoye"
LABEL maintainer.email="olawoyei0303@run.edu.ng"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    jq &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate -O /usr/local/bin/fastp http://opengene.org/fastp/fastp.${FASTP_VER} && \
    chmod a+x /usr/local/bin/fastp

ENV LC_ALL=C

WORKDIR /data

CMD [ "fastp", "--help" ]

# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app as test

# downloading sars-cov-2 fastq test files
RUN wget -q --no-check-certificate \
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
