ARG CIRCOS_VER="0.69-9"

FROM ubuntu:jammy as app 

ARG CIRCOS_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Circos"
LABEL software.version="${CIRCOS_VER}"
LABEL description="Circos is a software package for visualizing data and information"
LABEL website="https://circos.ca/"
LABEL license="https://circos.ca/"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    perl \
    cpanminus \
    libgd-dev \
    make \
    gcc-x86-64-linux-gnu \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN cpanm Clone Config::General Font::TTF::Font GD GD::Polyline Math::Bezier Math::Round Math::VecStat \
    Params::Validate Readonly Regexp::Common SVG Set::IntSpan Statistics::Basic Text::Format List::MoreUtils

RUN wget --no-check-certificate https://circos.ca/distribution/circos-${CIRCOS_VER}.tgz &&\
    tar -xvf circos-${CIRCOS_VER}.tgz && rm circos-${CIRCOS_VER}.tgz

ENV PATH="$PATH:/circos-0.69-9/bin" \
    LC_ALL=C

CMD ["circos" "-h"]

WORKDIR /data

## Test ##
FROM app as test 

ARG CIRCOS_VER

# required perl modules
RUN circos -modules

# internal test
RUN cd /circos-${CIRCOS_VER}/example &&\
    rm circos.png circos.svg run.out &&\
    ./run &&\
    cat run.out