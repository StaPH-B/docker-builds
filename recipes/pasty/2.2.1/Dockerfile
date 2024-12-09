ARG PASTY_VER="2.2.1"

FROM mambaorg/micromamba:1.5.8 AS app

ARG PASTY_VER

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="pasty"
LABEL software.version="${PASTY_VER}"
LABEL description="In silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies"
LABEL website="https://github.com/rpetit3/pasty"
LABEL license="https://github.com/rpetit3/pasty/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN micromamba install --name base -c conda-forge -c bioconda pasty=${PASTY_VER} &&\
    micromamba clean -afy

ENV PATH="/opt/conda/bin/:$PATH" \
    LC_ALL=C

CMD ["pasty", "--help"]

WORKDIR /data

## Test ##
FROM app AS test

ARG PASTY_VER

RUN apt-get update && apt-get install -y wget

# adapted from https://github.com/rpetit3/pasty/blob/main/test/README.md
RUN wget -q https://github.com/rpetit3/pasty/archive/refs/tags/v${PASTY_VER}.tar.gz &&\
    tar -xvf v${PASTY_VER}.tar.gz &&\
    cd pasty-${PASTY_VER}/test/ &&\
    for i in $(ls data | grep "fna.gz"); do pasty --input ./data/$i --prefix $(basename $i .fna.gz) --outdir results/ --force; done &&\
    head -n 1 results/O1-GCF_001420225.tsv > staphb-test.tsv &&\
    ls results/ | grep -v "details" | grep -v "blastn" | xargs -I {} grep -v "schema_version" results/{} | sort -k1 >> staphb-test.tsv &&\
    cat staphb-test.tsv

