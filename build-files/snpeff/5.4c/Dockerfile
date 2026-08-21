ARG SNPEFF_VER="5.4c"

FROM ubuntu:noble AS app
ARG SNPEFF_VER
# replace all '.' with '_' in SNPEFF version for download
ARG SNPEFF_DOWNLOAD_VER=${SNPEFF_VER//./_}

# Metadata
LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="SnpEff & SnpSift"
LABEL software.version=${SNPEFF_VER}
LABEL description="Genetic variant annotation and effect prediction toolbox."
LABEL description.SnpSift="Used after SnpEff annotation to filter and manipulate annotated files."
LABEL website="https://github.com/pcingola/SnpEff"
LABEL documentation="https://pcingola.github.io/SnpEff"
LABEL license="https://github.com/pcingola/SnpEff/blob/master/LICENSE.md"
LABEL maintainer="Tom Iverson"
LABEL maintainer.email="tiverson@utah.gov"


RUN apt-get update && apt-get install --no-install-recommends -y \
  openjdk-21-jre-headless \
  wget \
  ca-certificates \
  python3 \
  unzip \
  curl \
  && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://snpeff-public.s3.amazonaws.com/versions/snpEff_v${SNPEFF_DOWNLOAD_VER}_core.zip && \
  unzip snpEff_v${SNPEFF_DOWNLOAD_VER}_core.zip && \
  rm snpEff_v${SNPEFF_DOWNLOAD_VER}_core.zip

# Modify java executables and set environment variable $PATH
RUN chmod +x /snpEff/snpEff.jar && \
  echo "#!/bin/bash" >> /snpEff/snpeff && \
  chmod +x /snpEff/SnpSift.jar && \
  echo "#!/bin/bash" >> /snpEff/snpsift && \
  echo "exec java -jar /snpEff/snpEff.jar """"$""@"""" " >> /snpEff/snpeff && \
  chmod +x /snpEff/snpeff && \
  echo "exec java -jar /snpEff/SnpSift.jar """"$""@"""" " >> /snpEff/snpsift && \
  chmod +x /snpEff/snpsift

# Modify scripts to jar location
RUN for file in $(grep -iw "snpEff.jar" /snpEff/scripts/*sh | cut -f 1 -d ":" ) ; do cat $file | sed 's/snpEff.jar/\/snpEff\/snpEff.jar/g' > $file.tmp ; mv $file.tmp $file  ; done && \
  for file in $(grep -iw "SnpSift.jar" /snpEff/scripts/*sh | cut -f 1 -d ":" ) ; do cat $file | sed 's/snpEff.jar/\/snpEff\/SnpSift.jar/g' > $file.tmp ; mv $file.tmp $file  ; done && \
  chmod +x /snpEff/scripts/*sh

ENV PATH="${PATH}:/snpEff:/snpEff/scripts" 

CMD ["snpeff", "-help"]

WORKDIR /data

FROM app AS test

RUN snpeff -help 2>&1 || true && \
    snpsift -h 2>&1 || true

RUN snpeff download -v hg19 && \
    snpeff hg19 /snpEff/examples/test.chr22.vcf > annotated.vcf && \
    grep -v "^#" annotated.vcf | head -5 | tr "\t" "\ " | sed -e "s/.\{75\}/&\n/g"

# from issue https://github.com/StaPH-B/docker-builds/issues/760
RUN buildDbNcbi.sh CP014866.1
