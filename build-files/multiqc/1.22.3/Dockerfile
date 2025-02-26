FROM ubuntu:jammy as app

ARG MULTIQC_VER="1.22.3"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MultiQC"
LABEL software.version="${MULTIQC_VER}"
LABEL description="Aggregate bioinformatics results across many samples into a single report."
LABEL website="https://github.com/MultiQC/MultiQC"
LABEL license="https://github.com/MultiQC/MultiQC/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip && \
    apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install multiqc
RUN pip3 install --no-cache-dir "multiqc==${MULTIQC_VER}"

ENV LC_ALL='C.UTF-8' \
    LANG='C.UTF-8'

CMD multiqc --help

RUN mkdir /data
WORKDIR /data

# testing layer starts here
FROM app as test

# getting git
RUN apt-get update && apt-get install -y git

# to ensure multiqc is in PATH
RUN multiqc --help

# set working directory so that all test inputs & outputs are kept in /test
RUN mkdir /test
WORKDIR /test

# getting multiqc test data
RUN git clone https://github.com/ewels/MultiQC_TestData && \
    multiqc . && \
    ls multiqc_report.html 
    
