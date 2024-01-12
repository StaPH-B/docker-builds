ARG HEATCLUSTER_VER="1.0.2c"

FROM ubuntu:jammy as app

ARG HEATCLUSTER_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="HeatCluster"
LABEL software.version="${HEATCLUSTER_VER}"
LABEL description="Creates a heatmap from SNP-dists output"
LABEL website="https://github.com/DrB-S/heatcluster"
LABEL license="https://github.com/DrB-S/heatcluster/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \ 
    wget \
    procps \
    ca-certificates \
    python3 \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /heatcluster

RUN pip3 install pandas numpy seaborn matplotlib pathlib

RUN wget -q https://github.com/DrB-S/heatcluster/archive/refs/tags/${HEATCLUSTER_VER}.tar.gz && \
    tar -xzf ${HEATCLUSTER_VER}.tar.gz && \
    ls && \
    cp heatcluster-${HEATCLUSTER_VER}/heatcluster.py /heatcluster/heatcluster.py && \
    chmod +x /heatcluster/heatcluster.py && \
    rm -rf heatcluster-${HEATCLUSTER_VER} && \
    rm ${HEATCLUSTER_VER}.tar.gz && \
    mkdir /data

ENV PATH="/heatcluster/:$PATH" \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "heatcluster.py", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

ARG HEATCLUSTER_VER

RUN heatcluster.py --help && heatcluster.py --version

RUN wget -q https://github.com/DrB-S/heatcluster/archive/refs/tags/${HEATCLUSTER_VER}.tar.gz && \
    tar -xzf ${HEATCLUSTER_VER}.tar.gz

WORKDIR /test/test_small

RUN heatcluster.py -i /test/heatcluster-${HEATCLUSTER_VER}/test/small_matrix.csv && \
    ls SNP_matrix.pdf sorted_matrix.csv

WORKDIR /test/test_med

RUN heatcluster.py -i /test/heatcluster-${HEATCLUSTER_VER}/test/med_matrix.txt -o test5 && \
    ls sorted_matrix.csv test5.pdf
