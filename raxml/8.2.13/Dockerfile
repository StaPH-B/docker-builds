ARG RAXML_VER="8.2.13"

## Builder ##
FROM ubuntu:jammy as builder

ARG RAXML_VER

RUN apt-get update && apt-get install -y \
    build-essential\
    libopenmpi-dev \
    wget &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# compile all versions
RUN wget https://github.com/stamatak/standard-RAxML/archive/refs/tags/v${RAXML_VER}.tar.gz &&\
    tar -xvf v${RAXML_VER}.tar.gz &&\
    cd standard-RAxML-${RAXML_VER} &&\
    make -f Makefile.gcc && rm *.o &&\
    make -f Makefile.SSE3.gcc && rm *.o &&\
    make -f Makefile.AVX.gcc && rm *.o &&\
    make -f Makefile.PTHREADS.gcc && rm *.o &&\
    make -f Makefile.SSE3.PTHREADS.gcc && rm *.o &&\
    make -f Makefile.AVX.PTHREADS.gcc && rm *.o &&\
    make -f Makefile.MPI.gcc && rm *.o &&\
    make -f Makefile.SSE3.MPI.gcc && rm *.o &&\
    make -f Makefile.AVX.MPI.gcc && rm *.o &&\
    make -f Makefile.HYBRID.gcc && rm *.o &&\
    make -f Makefile.SSE3.HYBRID.gcc && rm *.o &&\
    make -f Makefile.AVX.HYBRID.gcc && rm *.o 

## App ##
FROM ubuntu:jammy as app

ARG RAXML_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="RAxML"
LABEL software.version="${RAXML_VER}"
LABEL description="A tool for Phylogenetic Analysis and Post-Analysis of Large Phylogenies"
LABEL website="https://github.com/stamatak/standard-RAxML"
LABEL license="https://github.com/stamatak/standard-RAxML/blob/v8.2.13/gpl-3.0.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y\
    openmpi-bin &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder standard-RAxML-${RAXML_VER}/raxmlHPC* /usr/local/bin/

ENV LC_ALL=C

CMD [ "raxmlHPC", "-h" ]

WORKDIR /data

## Test ##
FROM app as test

RUN apt-get update && apt-get install -y wget

# steal raxml-ng test data and run with raxml
RUN wget https://github.com/amkozlov/ng-tutorial/raw/master/prim.phy &&\
    raxmlHPC -s prim.phy -n test -m GTRGAMMA -p 2 &&\
    cat RAxML_result.test
    