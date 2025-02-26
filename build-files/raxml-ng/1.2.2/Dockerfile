FROM ubuntu:jammy as app

ARG RAXMLNG_VER="1.2.2"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="RAxML Next Generation"
LABEL software.version="${RAXMLNG_VER}"
LABEL description="RAxML-NG is a phylogenetic tree inference tool which uses maximum-likelihood (ML) optimality criterion"
LABEL website="https://github.com/amkozlov/raxml-ng"
LABEL license="https://github.com/amkozlov/raxml-ng/blob/master/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.com"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    unzip &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/amkozlov/raxml-ng/releases/download/${RAXMLNG_VER}/raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip &&\
    unzip raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip raxml-ng -d /usr/local/bin/ &&\
    rm raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip

ENV LC_ALL=C

CMD [ "raxml-ng", "--help" ]

WORKDIR /data

## Test ##
FROM app as test

ARG RAXMLNG_VER="1.2.2"

RUN wget --no-check-certificate https://github.com/amkozlov/raxml-ng/releases/download/${RAXMLNG_VER}/raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip &&\
    unzip -j raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip data/test.fa &&\     
    raxml-ng --msa test.fa --model GTR+G &&\
    cat test.fa.raxml.bestTree

