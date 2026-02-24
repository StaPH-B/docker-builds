ARG HIFIASM_VER="0.25.0"
ARG YAK_VER="0.1"

## Builder ##
FROM ubuntu:noble AS builder

ARG HIFIASM_VER
ARG YAK_VER

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    zlib1g-dev &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# hifiasm
RUN wget https://github.com/chhylp123/hifiasm/archive/refs/tags/${HIFIASM_VER}.tar.gz &&\
    tar -xvf ${HIFIASM_VER}.tar.gz && rm ${HIFIASM_VER}.tar.gz &&\
    cd hifiasm-${HIFIASM_VER} && make &&\
    mv hifiasm /usr/local/bin/

# yak is needed for trio binning assembly
RUN wget https://github.com/lh3/yak/archive/refs/tags/v${YAK_VER}.tar.gz &&\
    tar -xvf v${YAK_VER}.tar.gz && rm v${YAK_VER}.tar.gz &&\
    cd yak-${YAK_VER} && make &&\
    mv yak /usr/local/bin/

## App ##
FROM ubuntu:noble AS app

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="hifiasm"
LABEL software.version="${HIFIASM_VER}"
LABEL description="Hifiasm is a fast haplotype-resolved de novo assembler initially designed for PacBio HiFi reads"
LABEL website="https://github.com/chhylp123/hifiasm"
LABEL license="https://github.com/chhylp123/hifiasm/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

COPY --from=builder /usr/local/bin/ /usr/local/bin/

ENV LC_ALL=C

CMD ["hifiasm", "-h"]

WORKDIR /data

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y wget

# test hiifiasm
RUN wget https://github.com/chhylp123/hifiasm/releases/download/v0.7/chr11-2M.fa.gz &&\
    hifiasm -o test -t4 -f0 chr11-2M.fa.gz 2> test.log &&\
    awk '/^S/{print ">"$2;print $3}' test.bp.p_ctg.gfa > test.p_ctg.fa &&\
    head -c 500 test.p_ctg.fa

    # test yak
RUN yak count -K1.5g -t4 -o test.yak chr11-2M.fa.gz 2> yak.log &&\
    tail -n 4 yak.log
