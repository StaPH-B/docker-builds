FROM mambaorg/micromamba:2.9.0-ubuntu24.04 AS app

ARG PYPOLCA_VER="0.5.0"

USER root

WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:2.9.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="pypolca"
LABEL software.version="${PYPOLCA_VER}"
LABEL description="Polishes long reads"
LABEL website="https://github.com/gbouras13/pypolca"
LABEL license="https://github.com/gbouras13/pypolca/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN micromamba install --name base -c conda-forge -c bioconda pypolca=${PYPOLCA_VER} && \
    micromamba clean -a -f -y && \
    mkdir /data

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD ["pypolca", "-h"]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app AS test

WORKDIR /test

RUN pypolca -h && \
    pypolca --version

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
    pypolca run -a SRR13957123.consensus.fa -1 SRR13957123_1.fastq.gz -2 SRR13957123_2.fastq.gz  -t 2 -o test && \
    head test/pypolca_*.log && \
    ls test/pypolca.report test/pypolca.vcf test/pypolca_corrected.fasta

RUN micromamba list -n base
