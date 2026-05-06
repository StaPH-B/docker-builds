ARG CIRCOS_VER="0.69-10"

FROM ubuntu:noble AS app 

ARG CIRCOS_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Circos"
LABEL software.version="${CIRCOS_VER}"
LABEL description="Circos is a software package for visualizing data and information"
LABEL website="https://circos.ca/"
LABEL license="https://circos.ca/"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# circos tools version is 0.23-1 in noble
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    # install all circos deps the lazy way
    $(apt-cache depends circos=0.69.9+dfsg-2 | grep "Depends:" | awk '{print $2}' | grep -v '<') \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://circos.ca/distribution/circos-${CIRCOS_VER}.tgz && \
    tar -xvf circos-${CIRCOS_VER}.tgz && \
    rm circos-${CIRCOS_VER}.tgz

ENV PATH="/circos-${CIRCOS_VER}/bin:$PATH" \
    LC_ALL=C

CMD ["circos", "-h"]

WORKDIR /data

## Test ##
FROM app AS test 

ARG CIRCOS_VER

# required perl modules
RUN circos -modules

# internal test
RUN cd /circos-${CIRCOS_VER}/example &&\
    rm circos.png circos.svg run.out &&\
    ./run &&\
    cat run.out