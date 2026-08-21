ARG LIMA_VER="26.2.1"

## Builder ##
FROM staphb/lima:${LIMA_VER} AS app

ARG LIMA_VER
ARG DEBIAN_FRONTEND=noninteractive

LABEL base.image="staphb/lima:${LIMA_VER}"
LABEL dockerfile.version="1"
LABEL software="Lima"
LABEL software.version="${LIMA_VER}"
LABEL description="The PacBio Barcode Demultiplixer & Primer Remover"
LABEL website="https://github.com/PacificBiosciences/barcoding"
LABEL license="https://github.com/PacificBiosciences/barcoding/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y \
    r-base \
    r-cran-ggplot2 \
    r-cran-dplyr \
    r-cran-tidyr \
    r-cran-viridis \
    r-cran-scales \
    r-cran-data.table \
    r-cran-hexbin &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Rscripts
RUN wget -P /usr/local/bin/ https://github.com/PacificBiosciences/barcoding/raw/master/scripts/r/report_summary.R \
    https://github.com/PacificBiosciences/barcoding/raw/master/scripts/r/report_detail.R &&\
    chmod +x /usr/local/bin/report_summary.R /usr/local/bin/report_detail.R

CMD ["/bin/bash", "-c", "lima -h && lima-undo -h"]

WORKDIR /data

FROM app AS test

RUN lima -h && lima-undo -h

# download test files
RUN wget -q https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/HiFiViral_Barcoded_M13_Primer_Plate.fasta \
    https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/InqabaOmicronSamples_Barcoded_Sample.csv \
    https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/m64187e_211217_130958.hifi_reads.bam
# run test
RUN lima m64187e_211217_130958.hifi_reads.bam HiFiViral_Barcoded_M13_Primer_Plate.fasta demux.hifi.bam --biosample-csv InqabaOmicronSamples_Barcoded_Sample.csv --hifi-preset ASYMMETRIC &&\
    cat demux.hifi.lima.summary
    
RUN report_summary.R demux.hifi.lima.report &&\
    ls | grep png





