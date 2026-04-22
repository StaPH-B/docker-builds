ARG RAXMLNG_VER="2.0.0"

FROM ubuntu:noble AS app
ARG RAXMLNG_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="RAxML Next Generation"
LABEL software.version="${RAXMLNG_VER}"
LABEL description="RAxML-NG is a phylogenetic tree inference tool which uses maximum-likelihood (ML) optimality criterion"
LABEL website="https://github.com/amkozlov/raxml-ng"
LABEL license="https://github.com/amkozlov/raxml-ng/blob/master/LICENSE.txt"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.com"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*


RUN wget -q https://github.com/amkozlov/raxml-ng/releases/download/${RAXMLNG_VER}/raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip && \
    unzip raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip && \
    rm raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip && \
    mv ./raxml-ng /usr/local/bin/raxml-ng

WORKDIR /data

RUN raxml-ng --help

ENV LC_ALL=C

CMD [ "raxml-ng", "--help" ]


FROM app AS test
ARG RAXMLNG_VER


WORKDIR /test

# Getting the release binary's data/test.fa file.
RUN wget -q https://github.com/amkozlov/raxml-ng/releases/download/${RAXMLNG_VER}/raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip && \
    unzip -j raxml-ng_v${RAXMLNG_VER}_linux_x86_64.zip data/test.fa

# Made extra copies to run tests on.
RUN cp test.fa test2.fa && \
    cp test.fa test3.fa

# Tree inference and Model selection test (moose)
RUN raxml-ng --msa test.fa --model GTR+G && \
    raxml-ng --msa test2.fa --model GTR+G --fast && \
    raxml-ng --msa test3.fa --moose --data-type DNA
    
# Visualization of the best tree and comparison to fast mode's best tree.
RUN cat test.fa.raxml.bestTree && \
    diff test.fa.raxml.bestTree test2.fa.raxml.bestTree || true

# Best model found and comparison of model params and ic_score
RUN cat test3.fa.raxml.moose.bestModel && \
    cat test3.fa.raxml.moose.json