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

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    perl \
    cpanminus \
    make \
    build-essential \
    libgd-dev \
    # Circos Perl Dependencies from Ubuntu Repos:
    libclone-perl \
    libconfig-general-perl \
    libfont-ttf-perl \
    libgd-perl \
    libmath-bezier-perl \
    libmath-round-perl \
    libmath-vecstat-perl \
    libparams-validate-perl \
    libreadonly-perl \
    libregexp-common-perl \
    libsvg-perl \
    libset-intspan-perl \
    libstatistics-basic-perl \
    libtext-format-perl \
    liblist-moreutils-perl \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# 2. Install any remaining niche modules that might not be in APT (with --notest)
RUN cpanm --notest GD::Polyline

RUN wget --no-check-certificate https://circos.ca/distribution/circos-${CIRCOS_VER}.tgz &&\
    tar -xvf circos-${CIRCOS_VER}.tgz && rm circos-${CIRCOS_VER}.tgz

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