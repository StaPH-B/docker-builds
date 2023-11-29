FROM ubuntu:jammy as app

ARG CHECKM_VER="1.2.2"
ARG PPLACER_VER="v1.1.alpha19"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="CheckM"
LABEL software.version="${CHECKM_VER}"
LABEL description="CheckM provides a set of tools for assessing the quality of genomes recovered from isolates, single cells, or metagenomes."
LABEL website="dockerfile-template/Dockerfile dockerfile-template/README.md"
LABEL license="https://github.com/Ecogenomics/CheckM/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# install system requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    python3-pip \
    hmmer \
    prodigal &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm and its dependencies
RUN pip install --no-cache-dir numpy matplotlib pysam checkm-genome &&\
    wget https://github.com/matsen/pplacer/releases/download/${PPLACER_VER}/pplacer-linux-${PPLACER_VER}.zip && \
    unzip pplacer-linux-${PPLACER_VER}.zip && rm pplacer-linux-${PPLACER_VER}.zip

ENV PATH=$PATH:/pplacer-Linux-${PPLACER_VER} \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run.
CMD [ "checkm", "-h" ]

# 'WORKDIR' sets working directory
WORKDIR /data

## Test ##
FROM app as test

# download database and inform CheckM of where the files have been placed
RUN wget https://data.ace.uq.edu.au/public/CheckM_databases/checkm_data_2015_01_16.tar.gz &&\
    mkdir checkm_db && tar -C checkm_db -xvf checkm_data_2015_01_16.tar.gz &&\
    checkm data setRoot checkm_db 

# run test with internal test data
RUN checkm taxonomy_wf species "Escherichia coli" ./checkm_db/test_data/ ./checkm_test_results

