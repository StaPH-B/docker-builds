FROM ubuntu:noble AS app

ARG PYEUK_VER="0.8.1"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="PyEuk"
LABEL software.version="${PYEUK_VER}"
LABEL description="A Tool Suite for Catalogue-Free Multilocus Typing"
LABEL website="https://github.com/veg/pyeuk"
LABEL license="https://github.com/veg/pyeuk/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN wget https://github.com/veg/pyeuk/archive/refs/tags/v${PYEUK_VER}.tar.gz &&\
    tar -xvf v${PYEUK_VER}.tar.gz && rm v${PYEUK_VER}.tar.gz &&\
    cd pyeuk-${PYEUK_VER} &&\
    pip3 install --break-system-packages --no-cache-dir ".[amplicon,report]" 

ENV LC_ALL=C

CMD [ "pyeuk --help" ]    

WORKDIR /data

## Test ##
FROM app AS test 

RUN apt-get update && apt-get install -y --no-install-recommends git

RUN pyeuk fetch-test-data &&\
    cyclospora-typing run-all -s test_data/specimens -o ./outbreak_output &&\
    pyeuk cluster -m outbreak_output/ensemble_distance_matrix.csv -o sweep --k-min 2 --k-max 12 --n-boot 100 --report &&\
    pyeuk report sweep/*_SWEEP.json --matrix outbreak_output/ensemble_distance_matrix.csv -o alt_report.html --flavor clinical
