ARG ANICLUSTERMAP_VER="1.3.0"
ARG FASTANI_VER="1.34"
ARG SKANI_VER="0.2.1"

FROM staphb/fastani:${FASTANI_VER} as fastani
FROM staphb/skani:${SKANI_VER} as skani

## App ##
FROM ubuntu:jammy as app 

ARG ANICLUSTERMAP_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="ANIclustermap"
LABEL software.version="${ANICLUSTERMAP_VER}"
LABEL description="ANIclustermap draws ANI(Average Nucleotide Identity) clustermap between all-vs-all microbial genomes."
LABEL website="https://github.com/moshi4/ANIclustermap"
LABEL license="https://github.com/moshi4/ANIclustermap/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

# install aniclustermap and its dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    libgomp1 &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/* &&\
    pip install aniclustermap==${ANICLUSTERMAP_VER}

# import fastani & skani
COPY --from=fastani /usr/local/bin/fastANI /usr/local/bin/
COPY --from=skani /usr/local/bin/skani /usr/local/bin/

# default run command
CMD ANIclustermap -h

# singularity compatibility
ENV LC_ALL=C

WORKDIR /data

## Test ##
FROM app as test

ARG ANICLUSTERMAP_VER

RUN apt-get update && apt-get install -y wget

# download test data from repo
RUN wget https://github.com/moshi4/ANIclustermap/archive/refs/tags/v${ANICLUSTERMAP_VER}.tar.gz &&\
    tar -xvf v${ANICLUSTERMAP_VER}.tar.gz
# run default fastani mode
RUN ANIclustermap -i ANIclustermap-${ANICLUSTERMAP_VER}/example/input/minimal_dataset/ -o fastani
# run skani mode
RUN ANIclustermap -m skani -i ANIclustermap-${ANICLUSTERMAP_VER}/example/input/minimal_dataset/ -o skani
# check results
RUN ls fastani &&\
    cat fastani/ANIclustermap_matrix.tsv &&\
    ls skani &&\
    cat skani/ANIclustermap_matrix.tsv

