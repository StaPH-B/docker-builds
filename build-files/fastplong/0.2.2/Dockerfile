ARG FASTPLONG_VER="0.2.2"

FROM ubuntu:jammy AS app

# List all software versions are ARGs near the top of the dockerfile
# 'ARG' sets environment variables during the build stage
# ARG variables are ONLY available during image build, they do not persist in the final image
ARG FASTPLONG_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="fastplong"
LABEL software.version="${FASTPLONG_VER}"
LABEL description="Ultrafast preprocessing and quality control for long reads"
LABEL website="https://github.com/OpenGene/fastplong"
LABEL license="https://github.com/OpenGene/fastplong/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    libdeflate-dev \
    libisal-dev \
    libhwy-dev \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate -q http://opengene.org/fastplong/fastplong.${FASTPLONG_VER} && \
    mv fastplong.${FASTPLONG_VER} /usr/local/bin/fastplong && \
    chmod a+x /usr/local/bin/fastplong

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "fastplong", "--help" ]

# 'WORKDIR' sets working directory
WORKDIR /data

##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####
##### Step 2. Set up the testing stage.                                 #####
##### The docker image is built to the 'test' stage before merging, but #####
##### the test stage (or any stage after 'app') will be lost.           #####
##### ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- #####

# A second FROM insruction creates a new stage
FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN fastplong --help

RUN wget --no-check-certificate -q https://zenodo.org/records/10733190/files/df_test_files.tar.gz && \
    tar -xvf df_test_files.tar.gz && \
    fastplong -i test_files/test.fastq.gz -o filtered.test.fastq.gz && \
    ls filtered.test.fastq.gz
