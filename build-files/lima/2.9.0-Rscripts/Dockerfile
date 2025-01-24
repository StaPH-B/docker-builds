ARG LIMA_VER="2.9.0"

## Builder ##
FROM ubuntu:jammy as builder

ARG LIMA_VER
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    gfortran \
    r-base

# build required R packages
RUN R -e "install.packages(c('ggplot2', 'dplyr', 'tidyr' ,'viridis', 'scales', 'data.table', 'hexbin'), quietly = TRUE, warn.conflicts = FALSE, repos = 'http://cran.us.r-project.org')"

# Rscripts
RUN wget -P /usr/local/bin/ https://github.com/PacificBiosciences/barcoding/raw/master/scripts/r/report_summary.R \
    https://github.com/PacificBiosciences/barcoding/raw/master/scripts/r/report_detail.R &&\
    chmod +x /usr/local/bin/report_summary.R /usr/local/bin/report_detail.R

## App ##
FROM ubuntu:jammy as app

ARG LIMA_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Lima"
LABEL software.version="${LIMA_VER}"
LABEL description="The PacBio Barcode Demultiplixer & Primer Remover"
LABEL website="https://github.com/PacificBiosciences/barcoding"
LABEL license="https://github.com/PacificBiosciences/barcoding/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    r-base &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/R/site-library/ /usr/local/lib/R/site-library/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

RUN wget https://github.com/PacificBiosciences/barcoding/releases/download/v${LIMA_VER}/lima.tar.gz &&\
    tar -C /usr/local/bin -xvf lima.tar.gz &&\
    rm lima.tar.gz

ENV LC_ALL=C

CMD lima -h && lima-undo -h

WORKDIR /data

FROM app as test
# download test files
RUN wget -q https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/HiFiViral_Barcoded_M13_Primer_Plate.fasta \
    https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/InqabaOmicronSamples_Barcoded_Sample.csv \
    https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/m64187e_211217_130958.hifi_reads.bam
# run test
RUN lima m64187e_211217_130958.hifi_reads.bam HiFiViral_Barcoded_M13_Primer_Plate.fasta demux.hifi.bam --biosample-csv InqabaOmicronSamples_Barcoded_Sample.csv --hifi-preset ASYMMETRIC &&\
    cat demux.hifi.lima.summary
    
RUN report_summary.R demux.hifi.lima.report &&\
    ls | grep png





