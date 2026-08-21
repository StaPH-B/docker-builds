## Builder
FROM ubuntu:noble AS app

ARG LJA_VER="0.2"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="La Jolla Assembler"
LABEL software.version="${LJA_VER}"
LABEL description="A tool for genome assembly from PacBio HiFI reads based on de Bruijn graphs."
LABEL website="https://github.com/AntonBankevich/LJA"
LABEL license="https://github.com/AntonBankevich/LJA/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    g++-11 \
    make \
    cmake \
    zlib1g-dev &&\
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 1 &&\
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 1 &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# patch & compile LJA
RUN wget --no-check-certificate https://github.com/AntonBankevich/LJA/archive/refs/tags/untagged-c539e6b1159980742576.tar.gz -O LJA.tar.gz &&\
    mkdir LJA &&\
    tar -C LJA --strip-components=1 -xvf LJA.tar.gz &&\
    rm LJA.tar.gz &&\
    sed -i '/#include "graphlite\.hpp"/a #include <optional>' /LJA/src/tools/graphlite/serialize.hpp &&\
    cd LJA && cmake . &&\
    make

ENV PATH="/LJA/bin:$PATH" \
    LC_ALL=C

CMD [ "lja", "--help" ]

WORKDIR /data


## prep test data ##
FROM staphb/rasusa:4.1.0 AS testdata

RUN wget https://downloads.pacbcloud.com/public/dataset/2021-11-Microbial-96plex/demultiplexed-reads/m64004_210929_143746.bc2033.bam &&\
    rasusa reads --coverage 20 --genome-size 1.6m --output test.fastq.gz --output-format fastq m64004_210929_143746.bc2033.bam 

## Test ##
FROM app AS test 

COPY --from=testdata /data/test.fastq.gz /data/test.fastq.gz

# internal test
RUN run_tests
# test real data
RUN lja -t 4 -o test --reads /data/test.fastq.gz