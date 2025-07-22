ARG BUSCO_VER="6.0.0"

FROM mambaorg/micromamba:2.3.0-ubuntu22.04 AS app

ARG BUSCO_VER

LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="BUSCO"
LABEL software.version="${BUSCO_VER}"
LABEL description="Assessing genome assembly and annotation completeness with Benchmarking Universal Single-Copy Orthologs"
LABEL website="https://busco.ezlab.org/"
LABEL license="https://gitlab.com/ezlab/busco/-/raw/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

USER root

WORKDIR /

RUN micromamba install --name base -c conda-forge -c bioconda busco=${BUSCO_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

# AGUSTUS_CONFIG_PATH still needs to be set for micromamba install
ENV AUGUSTUS_CONFIG_PATH="/opt/conda/config/" \ 
    PATH="/opt/conda/bin/:$PATH" \
    LC_ALL=C

WORKDIR /data

CMD ["busco", "-h"]

## Tests ##
FROM app AS test

ARG BUSCO_VER

# install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates

RUN busco -h

WORKDIR /test

# getting test files
RUN wget -q https://gitlab.com/ezlab/busco/-/archive/${BUSCO_VER}/busco-${BUSCO_VER}.tar.gz && \
    tar -xvf busco-${BUSCO_VER}.tar.gz && ls

# run tests for bacteria and eukaryota
RUN busco -i busco-${BUSCO_VER}/test_data/bacteria/genome.fna -c 4 -m geno -f --out test_bacteria
RUN busco -i busco-${BUSCO_VER}/test_data/eukaryota/genome.fna -c 4 -m geno -f --out test_eukaryota
RUN busco -i busco-${BUSCO_VER}/test_data/eukaryota/genome.fna -l eukaryota_odb12 -c 4 -m geno -f --out test_eukaryota_augustus --augustus

# generate plot
RUN mkdir my_summaries &&\
    find . -name "short_summary.*.txt" -exec cp {} my_summaries \; &&\
    busco --plot my_summaries

# using actual data (Salmonella genome)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/010/941/835/GCA_010941835.1_PDT000052640.3/GCA_010941835.1_PDT000052640.3_genomic.fna.gz  && \
    gzip -d GCA_010941835.1_PDT000052640.3_genomic.fna.gz && \
    busco -m genome -i GCA_010941835.1_PDT000052640.3_genomic.fna -o busco_GCA_010941835.1 --cpu 4 --auto-lineage-prok && \
    head busco_GCA_010941835.1/short_summary*.txt

RUN micromamba list -n base