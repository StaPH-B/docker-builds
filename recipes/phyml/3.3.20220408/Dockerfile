FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist during image build time
ARG PHYML_VER="3.3.20220408"

# metadata
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2"
LABEL software="Phyml"
LABEL software.version="3.3.20220408"
LABEL description="PhyML estimates maximum likelihood phylogenies from alignments of nucleotide or amino acid sequences."
LABEL website="https://github.com/stephaneguindon/phyml/"
LABEL license="https://github.com/stephaneguindon/phyml/blob/master/COPYING"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="jvhagey@gmail.com"

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
        ca-certificates \
        pkg-config=0.29.1-0ubuntu4 \
        automake=1:1.16.1-4ubuntu6 \
        autoconf=2.69-11.1 \
        gcc=4:9.3.0-1ubuntu2 \
        texlive-latex-base=2019.20200218-1 \
        build-essential=12.8ubuntu1.1 \
        wget=1.20.3-1ubuntu2 && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget https://github.com/stephaneguindon/phyml/archive/refs/tags/v${PHYML_VER}.tar.gz && \
    tar -zxvf v${PHYML_VER}.tar.gz && \
    cd phyml-${PHYML_VER} && \
    sh autogen.sh && \
    ./configure --enable-phyml && \
    make

# set perl locale settings
# Required by most tools that use perl with singularity so we can use container with both docker and singularity
ENV LC_ALL=C

# Add references and entrypoint script
ENV PATH="${PATH}:/phyml-${PHYML_VER}/src"

# Add references and entrypoint script
WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY /test/snvAlignment.phy /data/

#run test
RUN phyml -i snvAlignment.phy --datatype nt --model GTR -v 0.0 -s BEST --ts/tv e --nclasses 4 --alpha e --bootstrap -4 --quiet
