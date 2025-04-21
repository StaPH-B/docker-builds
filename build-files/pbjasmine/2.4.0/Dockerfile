FROM ubuntu:jammy AS app

ARG JASMINE_VER="2.4.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Jasmine"
LABEL software.version="${JASMINE_VER}"
LABEL description="Jasmine predicts 5-Methylcytosine (5mC) of each CpG site in PacBio HiFi reads"
LABEL website="https://github.com/pacificbiosciences/jasmine/"
LABEL license="https://github.com/PacificBiosciences/jasmine/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    xz-utils &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/PacificBiosciences/jasmine/releases/download/v${JASMINE_VER}/jasmine.tar.xz &&\
    tar -C /usr/local/ -xvf jasmine.tar.xz &&\
    rm jasmine.tar.xz    

ENV LC_ALL=C

CMD [ "jasmine", "-h" ]

WORKDIR /data

## Test prep ##
FROM staphb/pbtk:3.1.1 AS testdata

RUN wget -q --no-check-certificate https://downloads.pacbcloud.com/public/Sequel-II-CpG-training/CCS/methylated/m64168_200823_191315.hifi_reads.bam &&\
    pbindex m64168_200823_191315.hifi_reads.bam &&\
    zmwfilter --downsample-count 10 m64168_200823_191315.hifi_reads.bam test.bam &&\
    rm m64168_200823_191315.hifi_reads.bam

## Test ##
FROM app AS test

COPY --from=testdata /data/test.bam /data/test.bam 

RUN jasmine test.bam out.bam --log-level INFO
