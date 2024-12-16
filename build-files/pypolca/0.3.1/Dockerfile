# both of these use the ubuntu:jammy base
FROM staphb/freebayes:1.3.7 as freebayes
FROM staphb/samtools:1.19 as samtools

FROM ubuntu:jammy as app

ARG PYPOLCA_VER="0.3.1"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pypolca"
LABEL software.version="${PYPOLCA_VER}"
LABEL description="Polishes long reads"
LABEL website="https://github.com/gbouras13/pypolca"
LABEL license="https://github.com/gbouras13/pypolca/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    ca-certificates \
    wget \
    bwa \
    vcftools \
    libseqlib-dev \
    libvcflib-tools \
    parallel \
    bc \
    python3 \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=freebayes /usr/local/bin/* /usr/local/bin/
COPY --from=samtools  /usr/local/bin/* /usr/local/bin/

RUN pip3 install --no-cache pypolca==${PYPOLCA_VER}

ENV PATH="$PATH" \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD pypolca -h

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app as test

WORKDIR /test

RUN pypolca -h && \
    pypolca --version

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_1.fastq.gz && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123_2.fastq.gz && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
    pypolca run -a SRR13957123.consensus.fa -1 SRR13957123_1.fastq.gz -2 SRR13957123_2.fastq.gz  -t 2 -o test && \
    head test/pypolca_*.log && \
    ls test/pypolca.report test/pypolca.vcf test/pypolca_corrected.fasta
