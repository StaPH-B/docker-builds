FROM ubuntu:jammy as app

ARG JASMINE_VER="2.0.0"

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
    wget &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate -P /usr/local/bin/ https://github.com/PacificBiosciences/jasmine/releases/download/v${JASMINE_VER}/jasmine &&\
    chmod 755 /usr/local/bin/jasmine

ENV LC_ALL=C

CMD [ "jasmine", "-h" ]

WORKDIR /data

## Test prep ##
FROM staphb/pbtk:3.1.1 as testdata

RUN wget -q --no-check-certificate https://downloads.pacbcloud.com/public/Sequel-II-CpG-training/CCS/methylated/m64168_200823_191315.hifi_reads.bam &&\
    pbindex m64168_200823_191315.hifi_reads.bam &&\
    zmwfilter --downsample-count 10 m64168_200823_191315.hifi_reads.bam test.bam &&\
    rm m64168_200823_191315.hifi_reads.bam

## Test ##
FROM app as test

COPY --from=testdata /data/test.bam /data/test.bam 

RUN jasmine test.bam out.bam --log-level INFO
