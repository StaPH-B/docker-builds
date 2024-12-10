ARG IGVREPORTS_VER=1.12.0

FROM ubuntu:jammy as app

ARG IGVREPORTS_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="IGV Reports"
LABEL software.version="${IGVREPORTS_VER}"
LABEL description="A Python application to generate self-contained HTML reports for variant review and other genomic applications."
LABEL website="https://github.com/igvteam/igv-reports"
LABEL license="https://github.com/igvteam/igv-reports/blob/master/LICENSE.md"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    python3-pip \
    libcurl4-gnutls-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir igv-reports==${IGVREPORTS_VER}

ENV PATH="$PATH" LC_ALL=C CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

CMD [ "create_report", "-h" ]

WORKDIR /data

FROM app as test

ARG IGVREPORTS_VER

WORKDIR /test

RUN create_report -h

RUN wget -q https://github.com/igvteam/igv-reports/archive/refs/tags/v${IGVREPORTS_VER}.tar.gz && \
    tar -xvf v${IGVREPORTS_VER}.tar.gz && \
    cd igv-reports-${IGVREPORTS_VER} && \
    create_report test/data/variants/variants.vcf.gz \
        --genome hg38 \
        --ideogram test/data/hg38/cytoBandIdeo.txt \
        --flanking 1000 \
        --info-columns GENE TISSUE TUMOR COSMIC_ID GENE SOMATIC \
        --samples reads_1_fastq \
        --sample-columns DP GQ \
        --tracks test/data/variants/variants.vcf.gz test/data/variants/recalibrated.bam test/data/hg38/refGene.txt.gz \
        --output example_vcf.html && \
    wc -l example_vcf.html

