FROM staphb/samtools:1.21 as samtools
FROM staphb/htslib:1.21 as htslib

# As a reminder
# https://github.com/StaPH-B/docker-builds/pull/925#issuecomment-2010553275
# bbmap/docs/TableOfContents.txt lists additional dependencies

FROM ubuntu:jammy as app

ARG SAMBAMBAVER=1.0.1
ARG BBTOOLSVER=39.13

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="BBTools"
LABEL software.version=${BBTOOLSVER}
LABEL description="A set of tools labeled as \"Bestus Bioinformaticus\""
LABEL website="https://sourceforge.net/projects/bbmap"
LABEL documentation="https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/"
LABEL license="https://jgi.doe.gov/disclaimer/"
LABEL maintainer="Abigail Shockey"
LABEL maintainer.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Padraic Fanning"
LABEL maintainer2.email="faninnpm AT miamioh DOT edu"

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    openjdk-8-jre-headless \
    pigz \
    pbzip2 \
    lbzip2 \
    bzip2 \
    libcurl4-gnutls-dev \
    libdeflate-dev \
    wget \
    ca-certificates \
    procps && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoclean

# copy samtools to image
COPY --from=samtools /usr/local/bin/* /usr/local/bin/
COPY --from=htslib   /usr/local/bin/* /usr/local/bin/

# download and install sambamba
RUN wget -q https://github.com/biod/sambamba/releases/download/v${SAMBAMBAVER}/sambamba-${SAMBAMBAVER}-linux-amd64-static.gz && \
    gzip -d sambamba-${SAMBAMBAVER}-linux-amd64-static.gz && \
    mv sambamba-${SAMBAMBAVER}-linux-amd64-static /usr/local/bin/sambamba && \
    chmod +x /usr/local/bin/sambamba

# download and install bbtools
RUN wget -q https://sourceforge.net/projects/bbmap/files/BBMap_${BBTOOLSVER}.tar.gz && \
    tar -xzf BBMap_${BBTOOLSVER}.tar.gz && \
    rm BBMap_${BBTOOLSVER}.tar.gz && \
    mkdir /data

ENV PATH=/bbmap/:$PATH \
    LC_ALL=C

CMD tail -n 90 /bbmap/docs/TableOfContents.txt

WORKDIR /data

# testing
FROM app as test

# get test data and test one thing that uses samtools/sambamba
RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam && \
    streamsam.sh in='SRR13957123.primertrim.sorted.bam' out='test_SRR13957123.primertrim.sorted.fastq.gz' && \
    test -f test_SRR13957123.primertrim.sorted.fastq.gz
