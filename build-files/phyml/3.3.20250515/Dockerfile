ARG PHYML_VER="3.3.20250515"

FROM ubuntu:jammy AS builder

ARG PHYML_VER

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
        ca-certificates \
        pkg-config \
        automake \
        autoconf \
        gcc \
        texlive-latex-base \
        build-essential \
        wget && \
    rm -rf /var/lib/apt/lists/* && apt-get autoclean

RUN wget https://github.com/stephaneguindon/phyml/archive/refs/tags/v${PHYML_VER}.tar.gz && \
    tar -zxvf v${PHYML_VER}.tar.gz && \
    mv phyml-${PHYML_VER} /phyml && \
    cd /phyml && \
    sh autogen.sh && \
    ./configure --enable-phyml && \
    make

FROM ubuntu:jammy AS app

# for easy upgrade later. ARG variables only persist during image build time
ARG PHYML_VER

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Phyml"
LABEL software.version="${PHYML_VER}"
LABEL description="PhyML estimates maximum likelihood phylogenies from alignments of nucleotide or amino acid sequences."
LABEL website="https://github.com/stephaneguindon/phyml/"
LABEL license="https://github.com/stephaneguindon/phyml/blob/master/COPYING"
LABEL maintainer="Jill Hagey"
LABEL maintainer.email="jvhagey@gmail.com"

COPY --from=builder /phyml /phyml

# Add references and entrypoint script
ENV LC_ALL=C PATH="${PATH}:/phyml/src"

# Add references and entrypoint script
WORKDIR /data

CMD ["phyml", "--help"]

# new base for testing
FROM app AS test

WORKDIR /test

RUN phyml --help || echo "Prints to STDERR for whatever reason"

RUN apt-get update && apt-get install -y --no-install-recommends wget

# Grab test data
RUN wget --no-check-certificate https://raw.githubusercontent.com/StaPH-B/docker-builds/refs/heads/master/build-files/phyml/3.3.20220408/test/snvAlignment.phy && \
    phyml -i snvAlignment.phy --datatype nt --model GTR -v 0.0 -s BEST --ts/tv e --nclasses 4 --alpha e --bootstrap -4 --quiet && \
    head snvAlignment.phy_phyml_tree.txt
