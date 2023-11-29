FROM python:3.7-slim as app

ARG GENOVI_VER="0.4.3"
ARG CIRCOS_VER="0.69-9"

LABEL base.image="python:3.7-slim"
LABEL dockerfile.version="1"
LABEL software="GenoVi"
LABEL software.version="${GENOVI_VER}"
LABEL description="Visualizing circos plots"
LABEL website="https://github.com/robotoD/GenoVi"
LABEL license="https://github.com/robotoD/GenoVi/blob/main/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# most of this is for circos. cairo is for genovi.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    ca-certificates \
    procps \
    libgd-dev \
    perl \
    cpanminus \
    pkg-config \
    make \
    libgd-graph-perl \
    libcairo2-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# these. are. all. for. circos
RUN cpanm Config::General \
    Number::Format \
    ExtUtils::Config \
    ExtUtils::InstallPaths \
    Clone \
    Font::TTF::Font \
    GD \
    GD::Polyline \
    Math::Bezier \
    Math::Round \
    Math::VecStat \
    Params::Validate \
    Readonly \
    Regexp::Common \
    List::MoreUtils \
    SVG \
    Set::IntSpan \
    Statistics::Basic \
    Text::Format

# there are often more up-to-date versions of genovi on pypi as opposed to github
# cariosvg is required for creating png, but not listed as a dependency
RUN pip3 install --no-cache genovi==${GENOVI_VER} cairosvg

# install circos (and a short test)
RUN wget -q http://circos.ca/distribution/circos-${CIRCOS_VER}.tgz && \
    tar -xvf circos-${CIRCOS_VER}.tgz && \
    rm circos-${CIRCOS_VER}.tgz && \
    cd /circos-${CIRCOS_VER}/bin && \
    ./list.modules && \
    ./test.modules

# adding circos to PATH
ENV PATH=/circos-${CIRCOS_VER}/bin:$PATH \
    LC_ALL=C.UTF-8

CMD genovi --help

WORKDIR /data

FROM app as test

WORKDIR /test

RUN genovi -h && genovi --version

# using the input files from a recent published version on github
RUN wget -q https://github.com/robotoD/GenoVi/archive/refs/tags/0.2.16.tar.gz && \
    tar -vxf 0.2.16.tar.gz && \
    genovi -i GenoVi-0.2.16/input_test/Corynebacterium_alimapuense_VA37.gbk -s draft -cs paradise --cogs_unclassified -bc white && \
    genovi -i GenoVi-0.2.16/input_test/Acinetobacter_radioresistens_DD78.gbff -cs strong -s complete --size 