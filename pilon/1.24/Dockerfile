FROM ubuntu:jammy as app

# ARG sets environment variables during the build stage
ARG PILONVER="1.24"
ARG JAVAVER="11"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pilon"
LABEL software.version="${PILONVER}"
LABEL description="Automatically improve draft assemblies and find variation among strains"
LABEL website="https://github.com/broadinstitute/pilon"
LABEL license="https://github.com/broadinstitute/pilon/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  procps \
  wget \
  openjdk-${JAVAVER}-jre && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install pilon
# creating a versionless jarfile so that scripts don't have to be updated
RUN mkdir pilon && \
  cd pilon && \
  wget -q https://github.com/broadinstitute/pilon/releases/download/v${PILONVER}/pilon-${PILONVER}.jar && \
  mv -v pilon-${PILONVER}.jar pilon.jar && ls && pwd

WORKDIR /data

ENV PATH="/pilon:${PATH}" LC_ALL=C

FROM staphb/samtools:1.16 as samtools

WORKDIR /test

RUN wget -q https://github.com/StaPH-B/docker-builds/blob/1670ca89936c634d62814ae7958062e1d80a5989/tests/SARS-CoV-2/SRR13957123.sorted.bam?raw=true && \
  mv SRR13957123.sorted.bam?raw=true SRR13957123.sorted.bam && \
  samtools index SRR13957123.sorted.bam

FROM app as test

WORKDIR /test

COPY --from=samtools /test/SRR13957123* /test/

RUN java -jar /pilon/pilon.jar --version && java -jar /pilon/pilon.jar --help

RUN wget -q https://github.com/UPHL-BioNGS/Cecret/blob/1928809ea07efb947039293fdf5609e8e577e61d/configs/MN908947.3.fasta?raw=true && \
  mv MN908947.3.fasta?raw=true MN908947.3.fasta && \
  java -Xmx6G -jar /pilon/pilon.jar --genome MN908947.3.fasta --frags SRR13957123.sorted.bam --changes && \
  echo "pilon changes:" && cat pilon.changes && ls pilon.fasta