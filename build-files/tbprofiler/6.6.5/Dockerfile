FROM mambaorg/micromamba:2.3.0-ubuntu22.04 AS app

USER root
WORKDIR /

ARG TBPROFILER_VER="6.6.5"

# this version is the shortened commit hash on the `master` branch here https://github.com/jodyphelan/tbdb/
# commits are found on https://github.com/jodyphelan/tbdb/commits/master
# this was the latest commit as of 2025-07-17
ARG TBDB_COMMIT="33305126125183ee55d25228d15756fae590cde3"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="tbprofiler"
LABEL software.version="${TBPROFILER_VER}"
LABEL description="The pipeline aligns reads to the H37Rv reference using bowtie2, BWA or minimap2 and then calls variants using bcftools. These variants are then compared to a drug-resistance database."
LABEL website="https://github.com/jodyphelan/TBProfiler/"
LABEL database="https://github.com/jodyphelan/tbdb/"
LABEL license="https://github.com/jodyphelan/TBProfiler/blob/master/LICENSE"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Sage Wright"
LABEL maintainer3.email="sagemwright@gmail.com"

# install tb-profiler via bioconda; install into 'base' conda env
RUN micromamba install --yes --name base --channel conda-forge --channel bioconda  \
    tb-profiler=${TBPROFILER_VER} && \
    micromamba clean --all --yes -f && micromamba list

# hardcode 'base' env bin into PATH, so conda env does not have to be "activated" at run time
ENV PATH="/opt/conda/bin:${PATH}"

# Version of database can be confirmed at /opt/conda/share/tbprofiler/tbdb.version.json
# can also run 'tb-profiler list_db' to find the same version info

# https://github.com/jodyphelan/tbdb
RUN tb-profiler update_tbdb --commit ${TBDB_COMMIT} && \
    tb-profiler list_db

WORKDIR /data

# Added command to bring help menu up upon running container.
CMD ["tb-profiler"]

# test stage
FROM app AS test

# checking if tool is in PATH
RUN tb-profiler && tb-profiler version

WORKDIR /tests

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget ca-certificates

# download some TB FASTQs and run through tb-profiler
RUN wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_1.fastq.gz && \
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR166/009/ERR1664619/ERR1664619_2.fastq.gz && \
    tb-profiler profile -1 ERR1664619_1.fastq.gz -2 ERR1664619_2.fastq.gz -t 2 -p ERR1664619 --txt

RUN grep 'commit' /opt/conda/share/tbprofiler/tbdb.variables.json && tb-profiler list_db

RUN micromamba list -n base
