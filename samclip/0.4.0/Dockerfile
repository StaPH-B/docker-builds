ARG SAMCLIP_VER="0.4.0"

FROM ubuntu:jammy as app

ARG SAMCLIP_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="samclip"
LABEL software.version="${SAMCLIP_VER}"
LABEL description="Samclip: filter SAM file for soft and hard clipped alignments"
LABEL website="https://github.com/tseemann/samclip"
LABEL license="https://github.com/tseemann/samclip/blob/master/LICENSE"
LABEL maintainer="Dhatri Badri"
LABEL maintainer.email="dhatrib@umich.edu"

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    software-properties-common \
    perl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install samclip
RUN wget https://github.com/tseemann/samclip/archive/refs/tags/v${SAMCLIP_VER}.tar.gz && \
    tar -xvf v${SAMCLIP_VER}.tar.gz && \
    rm v${SAMCLIP_VER}.tar.gz && \
    chmod +x /samclip-${SAMCLIP_VER}/samclip && \
    mkdir /data

ENV PATH="${PATH}:/samclip-${SAMCLIP_VER}/" \
    LC_ALL=C

CMD [ "samclip", "--help" ]

WORKDIR /data

FROM app as test

RUN samclip --help && \
    samclip --version

WORKDIR /test

# Run test using samclip executable
RUN wget https://raw.githubusercontent.com/tseemann/samclip/master/test.fna && \
    wget https://raw.githubusercontent.com/tseemann/samclip/master/test.sam && \
    wget https://raw.githubusercontent.com/tseemann/samclip/master/test.fna.fai && \
    samclip --ref test.fna < test.sam > out.sam  
