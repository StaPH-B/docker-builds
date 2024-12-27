FROM ubuntu:jammy as app

ARG MULTIQC_VER="1.18"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MultiQC"
LABEL software.version="${MULTIQC_VER}"
LABEL description="Aggregate bioinformatics results across many samples into a single report."
LABEL website="https://github.com/ewels/MultiQC"
LABEL license="https://github.com/ewels/MultiQC/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"
# Although... let's be honest. Most of this is copied and pasted from Abigail Shockey

# install remaining dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    wget \
    git \
    python3 \
    python3-dev \
    python3-pip \
    locales \
    pandoc \
    texlive-xetex && \
    locale-gen en_US.UTF-8 && \
    apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install multiqc
RUN pip3 install "multiqc==${MULTIQC_VER}"


# add pandoc to path
ENV PATH="${PATH}" \
    LC_ALL='C.UTF-8' LANG='C.UTF-8'

CMD multiqc --help

RUN mkdir /data
WORKDIR /data

# testing layer starts here
FROM app as test

# to ensure multiqc is in PATH
RUN multiqc --help

# set working directory so that all test inputs & outputs are kept in /test
RUN mkdir /test
WORKDIR /test

# getting multiqc test data and testing pandoc
RUN git clone https://github.com/ewels/MultiQC_TestData && \
    multiqc . && \
    ls multiqc_report.html 
    
RUN multiqc /test/MultiQC_TestData/data/modules/BUSCO --filename multiqc_report2.html -o multiqc_data2 --pdf && \
    ls multiqc_data2/multiqc_report2.html multiqc_data2/multiqc_report2_data
