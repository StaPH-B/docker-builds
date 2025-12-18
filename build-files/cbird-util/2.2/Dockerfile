FROM ubuntu:jammy AS app

ARG CBIRD_UTIL_VER="2.2"
ARG DATASETS_VER="v18.9.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="C-BIRD"
LABEL software.version=${CBIRD_UTIL_VER}
LABEL description="C-BIRD utility tool"
LABEL website="https://github.com/Kincekara/C-BIRD"
LABEL license="https://github.com/Kincekara/C-BIRD/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

ARG DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    unzip \
    jq \
    python3-pandas \
    python3-lxml \
    python3-docx \
    python-argparse \
    python3-numpy &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/ncbi/datasets/releases/download/${DATASETS_VER}/linux-amd64.cli.package.zip &&\
    unzip linux-amd64.cli.package.zip && rm linux-amd64.cli.package.zip &&\
    mv datasets dataformat /usr/local/bin/

RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/species_genome_size.txt.gz &&\
    gunzip species_genome_size.txt.gz &&\
    date +%Y-%m-%d > sgs_download_date.txt &&\
    mv species_genome_size.txt sgs_download_date.txt /usr/local/lib/

COPY html_report.py est_coverage.py qc_report.py plain_report.py /usr/local/bin/

ENV LC_ALL=C

CMD ["echo", "This image is part of the C-BIRD pipeline (https://github.com/Kincekara/C-BIRD) and is not intended to be used separately.\n\
The available tools are html_report.py, est_coverage.py, qc_report.py, plain_report.py, datasets, and dataformat."]

WORKDIR /data

FROM app AS test

COPY test/ /test/

RUN cd /test && ./test.sh