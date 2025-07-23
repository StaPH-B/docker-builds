ARG COLORIDVER="0.1.4.3"

FROM ubuntu:jammy AS app

ARG COLORIDVER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="colorid"
LABEL software.version="${COLORIDVER}"
LABEL description="Experiments with using BIGSI data structure for metagenomic and QC applications"
LABEL website="https://github.com/hcdenbakker/colorid"
LABEL license="https://github.com/hcdenbakker/colorid/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# install minimal dependencies, cleanup apt garbage
RUN apt-get update && apt-get install -y \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# ColorID install
RUN mkdir colorid && \
    cd colorid && \
    wget https://github.com/hcdenbakker/colorid/releases/download/v${COLORIDVER}/colorid_Linux64v${COLORIDVER} && \
    mv colorid_Linux64v${COLORIDVER} colorid && \
    chmod +x colorid && \
    mkdir /data

# set PATH and locale settings just in case 
ENV PATH="$PATH:/colorid"\
    LC_ALL=C

WORKDIR /data

CMD [ "colorid", "--help" ]

FROM app AS test

ARG COLORIDVER

WORKDIR /test

RUN colorid --help && colorid --version

RUN wget https://github.com/hcdenbakker/colorid/archive/refs/tags/v${COLORIDVER}.tar.gz && \
    tar -vxf v${COLORIDVER}.tar.gz && \
    cd colorid-${COLORIDVER} && \
    colorid build -s 750000 -n 4 -k 27 -b phage -r test_data/ref_file.txt && \
    colorid read_id -b phage.bxi -q ./test_data/SRR548019.fastq.gz -n test_read_id -d 10 && \
    colorid search -b phage.bxi -q ./test_data/SRR548019.fastq.gz -f 1 > test.out && \
    head test.out
