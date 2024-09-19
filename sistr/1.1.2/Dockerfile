FROM ubuntu:jammy AS app

ARG SISTR_VER="1.1.2"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SISTR"
LABEL software.version="1.1.2"
LABEL description="Salmonella In Silico Typing Resource (SISTR)"
LABEL website="https://github.com/peterk87/sistr_cmd"
LABEL license="https://github.com/peterk87/sistr_cmd/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    python3-setuptools \
    python3-pandas \
    python3-numpy \
    python3-tables \
    python3-scipy \
    python3-pycurl \
    ncbi-blast+ \
    mafft \
    mash &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/phac-nml/sistr_cmd/archive/refs/tags/v${SISTR_VER}.tar.gz &&\
    tar -xvf v${SISTR_VER}.tar.gz && rm v${SISTR_VER}.tar.gz &&\
    cd sistr_cmd-${SISTR_VER}/ &&\
    python3 setup.py install &&\
    cd .. && rm -rf sistr_cmd-${SISTR_VER}

WORKDIR /data

ENV LC_ALL=C

CMD ["sistr", "--help"]

## Test ##
FROM app AS test

RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz &&\
    gunzip GCF_000006945.2_ASM694v2_genomic.fna.gz

RUN sistr --qc -vv --alleles-output allele-results.json --novel-alleles novel-alleles.fasta --cgmlst-profiles cgmlst-profiles.csv -f tab -o sistr-output.tab GCF_000006945.2_ASM694v2_genomic.fna &&\
    cat sistr-output.tab 