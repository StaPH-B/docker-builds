FROM ubuntu:noble AS app

ARG MERQURY_VER="1.4.1"
ARG MERYL_VER="1.4.1"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Merqury"
LABEL software.version="${MERQURY_VER}"
LABEL description="Evaluate genome assemblies with k-mers and more"
LABEL website="https://github.com/marbl/merqury"
LABEL license="https://github.com/marbl/merqury/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    xz-utils \
    libgomp1 \
    default-jre-headless \
    r-cran-argparse \
    r-cran-ggplot2 \
    r-cran-scales \
    bedtools \
    samtools &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

# install meryl
RUN wget https://github.com/marbl/meryl/releases/download/v${MERYL_VER}/meryl-${MERYL_VER}.Linux-amd64.tar.xz &&\
    tar -xJf meryl-${MERYL_VER}.Linux-amd64.tar.xz &&\
    rm meryl-${MERYL_VER}.Linux-amd64.tar.xz

# install merqury
RUN wget https://github.com/marbl/merqury/archive/v${MERQURY_VER}.tar.gz &&\
    tar -xvf v${MERQURY_VER}.tar.gz &&\
    rm v${MERQURY_VER}.tar.gz

ENV PATH="/opt/meryl-${MERYL_VER}/bin/:/opt/merqury-${MERQURY_VER}/:$PATH" \
    MERQURY="/opt/merqury-${MERQURY_VER}" \
    LC_ALL=C

CMD [ "merqury.sh" ]

WORKDIR /data

## Test ##
FROM app AS test 

RUN wget https://gembox.cbcb.umd.edu/triobinning/athal_COL.fasta &&\
    wget https://obj.umiacs.umd.edu/marbl_publications/merqury/athal/a_thal.k18.meryl.tar.gz &&\
    tar -xf a_thal.k18.meryl.tar.gz

RUN merqury.sh F1.k18.meryl athal_COL.fasta test &&\
    cat test.qv