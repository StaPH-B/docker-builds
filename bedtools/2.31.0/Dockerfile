ARG BEDTOOLS_VER="2.31.0"

FROM ubuntu:jammy as app

ARG BEDTOOLS_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="bedtools"
LABEL software.version="$BEDTOOLS_VER"
LABEL description="bedtools - the swiss army knife for genome arithmetic"
LABEL website="https://github.com/arq5x/bedtools2"
LABEL license="https://github.com/arq5x/bedtools2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# requires libghc-bzlib-dev build-essential zlib1g-dev
# RUN wget -q https://github.com/arq5x/bedtools2/archive/refs/tags/v${BEDTOOLS_VER}.tar.gz && \
#    tar -xvf v${BEDTOOLS_VER}.tar.gz && \
#    cd bedtools2-${BEDTOOLS_VER} && \
#    make && \
#    mkdir /data

RUN cd /usr/local/bin && \
    wget https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VER}/bedtools.static && \
    mv bedtools.static bedtools && \
    chmod +x bedtools && \
    mkdir /data

RUN bedtools --help

# setting just in case for singularity compatibility
ENV LC_ALL=C

WORKDIR /data

CMD [ "bedtools", "--help" ]

FROM app as test

ARG BEDTOOLS_VER

WORKDIR /test

RUN wget -q https://github.com/arq5x/bedtools2/archive/refs/tags/v${BEDTOOLS_VER}.tar.gz && \
    tar -xf v${BEDTOOLS_VER}.tar.gz && \
    # getting rid of ulimit (gitpod complains)
    sed -i 's/ulimit/#ulimit/g' /test/bedtools2-${BEDTOOLS_VER}/test/test.sh && \
    # changing executable to the one installed in app
    for tool_test in $(ls /test/bedtools2-${BEDTOOLS_VER}/test/*/test*sh) ; do echo $tool_test ; sed -i 's/BT=.*/BT=bedtools/g' $tool_test ; done 
ls
WORKDIR /test/bedtools2-${BEDTOOLS_VER}/test

# missing htsutil for testing (built if we built from the github repo)
RUN bash test.sh
