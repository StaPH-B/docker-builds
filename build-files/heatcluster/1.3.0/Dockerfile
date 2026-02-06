ARG HEATCLUSTER_VER="1.3.0"

FROM ubuntu:jammy AS app

ARG HEATCLUSTER_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="HeatCluster"
LABEL software.version="${HEATCLUSTER_VER}"
LABEL description="Creates a heatmap from SNP-dists output"
LABEL website="https://github.com/erinyoung/heatcluster"
LABEL license="https://github.com/erinyoung/heatcluster/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \ 
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir heatcluster==${HEATCLUSTER_VER} && \
    mkdir /data

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "heatcluster", "-h" ]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

ARG HEATCLUSTER_VER

RUN heatcluster -h && heatcluster -v

RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget --no-check-certificate https://github.com/erinyoung/heatcluster/archive/refs/tags/${HEATCLUSTER_VER}.tar.gz && \
    tar -xzf ${HEATCLUSTER_VER}.tar.gz

RUN heatcluster -i heatcluster-${HEATCLUSTER_VER}/test/small_matrix.csv && \
    ls heatcluster_sorted.csv
