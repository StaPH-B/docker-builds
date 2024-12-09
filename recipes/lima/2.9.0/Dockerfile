FROM ubuntu:jammy as app

ARG LIMA_VER="2.9.0"

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
    wget &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/PacificBiosciences/barcoding/releases/download/v${LIMA_VER}/lima.tar.gz &&\
    tar -C /usr/local/bin -xvf lima.tar.gz &&\
    rm lima.tar.gz

ENV LC_ALL=C

CMD lima -h && lima-undo -h

WORKDIR /data

FROM app as test
# download test files
RUN wget -q --no-check-certificate https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/HiFiViral_Barcoded_M13_Primer_Plate.fasta \
    https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/InqabaOmicronSamples_Barcoded_Sample.csv \
    https://downloads.pacbcloud.com/public/dataset/HiFiViral/Jan_2022/m64187e_211217_130958.hifi_reads.bam
# run test
RUN lima m64187e_211217_130958.hifi_reads.bam HiFiViral_Barcoded_M13_Primer_Plate.fasta demux.hifi.bam --biosample-csv InqabaOmicronSamples_Barcoded_Sample.csv --hifi-preset ASYMMETRIC &&\
    cat demux.hifi.lima.summary





