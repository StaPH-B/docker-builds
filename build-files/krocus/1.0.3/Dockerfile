FROM ubuntu:jammy as app

ARG KROCUS_VER="1.0.3"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="krocus"
LABEL software.version="${KROCUS_VER}"
LABEL description="Predict a sequence type directly from uncorrected long reads"
LABEL website="https://github.com/andrewjpage/krocus/"
LABEL license="https://github.com/andrewjpage/krocus/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-biopython \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir krocus==${KROCUS_VER}

ENV LC_ALL=C

CMD [ "krocus", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN krocus --help && \
    krocus --version

RUN krocus_database_downloader -l && \
    krocus_database_downloader  --species "Klebsiella pneumoniae" --output_directory Klebsiella_pneumoniae

# klebsiella:147
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR303/058/SRR30357358/SRR30357358_1.fastq.gz && \
    krocus Klebsiella_pneumoniae SRR30357358_1.fastq.gz > results.txt && \
    head results.txt
