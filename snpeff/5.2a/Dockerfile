ARG SNPEFF_VER="5.2a"
ARG SNPEFF_JAR_VER="5.2"
ARG SNPSIFT_VER="5.1"

## Builder ##
FROM ubuntu:focal as builder

ARG SNPEFF_VER
ARG SNPEFF_JAR_VER
ARG SNPSIFT_VER

# Install open using apt 
RUN apt-get update && apt-get install -y software-properties-common && \
  apt-get update && apt-get install -y \
  openjdk-11-jre \
  ant \
  maven \
  curl \
  wget && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install dependencies and snpEff executables from the source code using Maven.
RUN wget https://github.com/pcingola/SnpEff/archive/refs/tags/v${SNPEFF_VER}.tar.gz && \
  tar -xvf v${SNPEFF_VER}.tar.gz && \
  rm v${SNPEFF_VER}.tar.gz && \
  cd /SnpEff-${SNPEFF_VER}/lib && \
  # install Antlr
  mvn install:install-file -Dfile=antlr-4.5.1-complete.jar -DgroupId=org.antlr -DartifactId=antlr -Dversion=4.5.1 -Dpackaging=jar && \
  # install BioJava core
  mvn install:install-file -Dfile=biojava3-core-3.0.7.jar -DgroupId=org.biojava -DartifactId=biojava3-core -Dversion=3.0.7 -Dpackaging=jar && \
  # install BioJava structure
  mvn install:install-file -Dfile=biojava3-structure-3.0.7.jar -DgroupId=org.biojava -DartifactId=biojava3-structure -Dversion=3.0.7 -Dpackaging=jar && \
  cd /SnpEff-${SNPEFF_VER} && \
  # skipping scripts_build/make.sh and instead putting relevant commands here
  mvn clean compile assembly:single jar:jar && \
  cp /SnpEff-${SNPEFF_VER}/target/SnpEff-${SNPEFF_JAR_VER}-jar-with-dependencies.jar /snpEff.jar && \
  # The version for the dependencies matches that of SNPSIFT
  mvn install:install-file -Dfile=/SnpEff-${SNPEFF_VER}/target/SnpEff-${SNPEFF_JAR_VER}.jar -DgroupId=org.snpeff -DartifactId=SnpEff -Dversion=${SNPSIFT_VER} -Dpackaging=jar -DgeneratePom=true --quiet && \
  mkdir /data

# Install dependencies and SnpSift executables from the source code using Maven.
RUN wget https://github.com/pcingola/SnpSift/archive/refs/tags/v${SNPSIFT_VER}.tar.gz && \
  tar -xvf v${SNPSIFT_VER}.tar.gz && \
  rm v${SNPSIFT_VER}.tar.gz && \
  cd /SnpSift-${SNPSIFT_VER} && \
  mvn clean compile assembly:single jar:jar && \
  cp target/SnpSift-${SNPSIFT_VER}-jar-with-dependencies.jar /SnpSift.jar && \
  mvn install:install-file -Dfile=target/SnpSift-${SNPSIFT_VER}.jar -DgroupId=org.snpsift -DartifactId=SnpSift -Dversion=${SNPSIFT_VER} -Dpackaging=jar -DgeneratePom=true 

# Modify java executables and set environment variable $PATH
RUN mv SnpEff-${SNPEFF_VER} snpEff && \
  mv snpEff.jar snpEff && \
  mv SnpSift.jar snpEff && \
  chmod +x /snpEff/snpEff.jar && \
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

## App ##
FROM ubuntu:focal as app
ARG SNPEFF_VER
ARG SNPEFF_JAR_VER
ARG SNPSIFT_VER

# Metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SnpEff & SnpSift"
LABEL software.version=${SNPEFF_VER}
LABEL snpeff.jarfile.version=${SNPEFF_JAR_VER}
LABEL snpsift.software.version=${SNPSIFT_VER}
LABEL description="Genetic variant annotation and effect prediction toolbox."
LABEL description.SnpSift="Used after SnpEff annotation to filter and manipulate annotated files."
LABEL website="https://pcingola.github.io/SnpEff"
LABEL license="https://github.com/pcingola/SnpEff/blob/master/LICENSE.md"
LABEL maintainer="Tom Iverson"
LABEL maintainer.email="tiverson@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive

# perl, python2, and r are required for the scripts
RUN apt-get update && apt-get install --no-install-recommends -y \
  openjdk-11-jre-headless \
  perl \
  r-base \
  python-is-python2 \
  curl \
  && apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /snpEff/snpeff /snpEff/snpsift /snpEff/snpEff.jar /snpEff/SnpSift.jar /snpEff/snpEff.config /snpEff/
COPY --from=builder /snpEff/scripts/ /snpEff/scripts/ 

ENV PATH="${PATH}:/snpEff:/snpEff/scripts" 

CMD snpEff -h

WORKDIR /data

# Run test of annotation
FROM app as test
RUN apt-get update && apt-get install -y wget

COPY test_snpeff_snpsift.sh .

RUN bash test_snpeff_snpsift.sh 

# from issue https://github.com/StaPH-B/docker-builds/issues/760
RUN buildDbNcbi.sh CP014866.1
