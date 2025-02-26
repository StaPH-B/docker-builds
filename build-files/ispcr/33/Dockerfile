ARG ISPCR_VER="33"

## Builder ##
FROM ubuntu:jammy as builder

ARG ISPCR_VER
ARG MACHTYPE="x86_64-pc-linux-gnu"

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    unzip

RUN wget https://hgwdev.gi.ucsc.edu/~kent/src/isPcr${ISPCR_VER}.zip &&\
    unzip isPcr${ISPCR_VER}.zip &&\
    cd isPcrSrc &&\
    sed -i 's/-Werror//g' inc/common.mk &&\
    mkdir -p bin/$MACHTYPE &&\
    mkdir -p lib/$MACHTYPE &&\
    make HOME=$PWD MACHTYPE=${MACHTYPE} C_INCLUDE_PATH=/usr/include LIBRARY_PATH=/usr/lib CFLAGS="-fcommon" &&\
    mv bin/$MACHTYPE/* /usr/local/bin/

## App ##
FROM ubuntu:jammy as app 

ARG ISPCR_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="isPcr"
LABEL software.version="${ISPCR_VER}"
LABEL description="In-Slico PCR"
LABEL website="https://users.soe.ucsc.edu/~kent/"
LABEL license="All modules are copyright 2000-2004 by Jim Kent. License is hereby granted for personal, academic, and non-profit use."
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/* /usr/local/bin/

ENV LC_ALL=C

CMD [ "isPcr" ]

WORKDIR /data

## Test ##
FROM app as test

# prepare inputs
RUN apt-get update && apt-get install -y wget &&\
    wget https://hgdownload.soe.ucsc.edu/goldenPath/wuhCor1/bigZips/wuhCor1.fa.gz &&\
    gunzip wuhCor1.fa.gz &&\
    echo "orf1a CTAGGACCTCTTTCTGCTCA ACACTCTCCTAGCACCATCA" > primers

# run a test
RUN isPcr wuhCor1.fa primers stdout

