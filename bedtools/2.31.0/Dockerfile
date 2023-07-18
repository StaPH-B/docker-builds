ARG BEDTOOLS_VER="2.31.0"

### builder stage for compiling bedtools code ###
FROM ubuntu:jammy as builder

# re-instantiate variable so we can use it in builder stage
ARG BEDTOOLS_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="bedtools"
LABEL software.version="${BEDTOOLS_VER}"
LABEL description="bedtools - the swiss army knife for genome arithmetic"
LABEL website="https://github.com/arq5x/bedtools2"
LABEL license="https://github.com/arq5x/bedtools2/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# install deps via apt-get, these are mainly for compiling bedtools code and for running tests. some are for downloading files (wget, ca-certificates)
# last command is to point 'python' cmd to `python3` so that bedtools test scripts work. There are bash scripts that call 'python'
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \ 
    zlib1g-dev \
    libghc-bzlib-dev \
    liblzma-dev \
    wget \
    ca-certificates \
    python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# python3 required when compiling via `make` command for creating old CLI executables
# dependencies listed here (albeit for v2.30.0, still should be identical): https://packages.ubuntu.com/jammy/bedtools
# requires libghc-bzlib-dev, build-essential, zlib1g-dev, and a few others
# 'make install' should place binary executable files in /usr/local/bin
RUN wget -q https://github.com/arq5x/bedtools2/archive/refs/tags/v${BEDTOOLS_VER}.tar.gz && \
   tar -xzf v${BEDTOOLS_VER}.tar.gz && \
   cd bedtools2-${BEDTOOLS_VER} && \
   make && \
   make install 

### keeping old installation cmds here in case we want to install via pre-compiled binary again in the future ###
# RUN cd /usr/local/bin && \
#     wget https://github.com/arq5x/bedtools2/releases/download/v${BEDTOOLS_VER}/bedtools.static && \
#     mv bedtools.static bedtools && \
#     chmod +x bedtools && \
#     mkdir /data

### test stage ###
FROM builder as test

# re-instantiate variable so we can use it again in the test stage
ARG BEDTOOLS_VER

# test scripts expect to be run from the bedtools root dir
WORKDIR /bedtools2-${BEDTOOLS_VER}

# commenting out ulimit command in test/test.sh (gitpod complains)
# run tests included with bedtools code
RUN sed -i 's/ulimit/#ulimit/g' test/test.sh && \
make test

### final app stage ###
# starting from fresh base image instead of a previous stage
FROM ubuntu:jammy as app 

# copy in all bedtools executable files from builder stage to final app stage
COPY --from=builder /usr/local/bin/* /usr/local/bin

# setting just in case for singularity compatibility
ENV LC_ALL=C

# default command is to print help options
CMD [ "bedtools", "--help" ]

# set final working directory to /data
WORKDIR /data

# check help options and version
RUN bedtools --help && \
bedtools --version