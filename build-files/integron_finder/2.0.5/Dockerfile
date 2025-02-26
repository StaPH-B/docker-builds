FROM ubuntu:jammy AS app

ARG INTEGRON_FINDER_VER="2.0.5"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Integron Finder"
LABEL software.version="${INTEGRON_FINDER_VER}"
LABEL description="Finds integrons in DNA sequences"
LABEL website="https://github.com/gem-pasteur/Integron_Finder"
LABEL license="https://github.com/gem-pasteur/Integron_Finder/blob/master/COPYING"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    hmmer \
    infernal \
    prodigal && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir integron_finder==${INTEGRON_FINDER_VER}

ENV LC_ALL=C

CMD [ "integron_finder", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y wget

RUN wget -q https://github.com/gem-pasteur/Integron_Finder/raw/master/tests/data/Replicons/NZ_CP016323.fna &&\
    integron_finder --local-max --circ --keep-tmp NZ_CP016323.fna &&\
    cat Results_Integron_Finder_NZ_CP016323/NZ_CP016323.summary &&\
    head Results_Integron_Finder_NZ_CP016323/NZ_CP016323.integrons



