ARG PPANGGOLIN_VER="1.2.105"
ARG ARAGORN_VER="1.2.41"
ARG MMSEQS2_VER="15-6f452"
ARG MAFFT_VER="7.505"
ARG PRODIGAL_VER="2.6.3"
ARG INFERNAL_VER="1.1.5"

FROM ubuntu:jammy as builder

ARG ARAGORN_VER
ARG PRODIGAL_VER
ARG INFERNAL_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    libc6-dev \
    make \
    gcc \
    python3 \
    wget

# get ARAGORN
RUN wget -q https://www.ansikte.se/ARAGORN/Downloads/aragorn${ARAGORN_VER}.c && \
    gcc -O3 -ffast-math -finline-functions -o /usr/local/bin/aragorn aragorn${ARAGORN_VER}.c && \
    aragorn -h 

# get Prodigal
RUN wget https://github.com/hyattpd/Prodigal/archive/refs/tags/v${PRODIGAL_VER}.tar.gz && \
    tar -xvf v${PRODIGAL_VER}.tar.gz && \
    cd Prodigal-${PRODIGAL_VER} && \
    make install && \
    prodigal -h

# get infernal
RUN wget eddylab.org/infernal/infernal-${INFERNAL_VER}.tar.gz && \
    tar -xvf infernal-${INFERNAL_VER}.tar.gz && \
    cd infernal-${INFERNAL_VER} && \
    ./configure && \
    make check && \
    make install 
    #cd easel && \
    #make install
    
FROM ubuntu:jammy as app

ARG PPANGGOLIN_VER
ARG MMSEQS2_VER
ARG MAFFT_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="PPanGGOLiN"
LABEL software.version="${PPANGGOLIN_VER}"
LABEL description="Depicting microbial species diversity via a Partitioned PanGenome Graph Of Linked Neighbors"
LABEL website="https://github.com/labgem/PPanGGOLiN"
LABEL license="https://github.com/labgem/PPanGGOLiN/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

COPY --from=builder /usr/local/bin/* /usr/local/bin/

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    gcc \
    procps \
    python3 \
    python3-dev \
    python3-pip \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# get MMSEQS2
RUN wget -q https://github.com/soedinglab/MMseqs2/releases/download/${MMSEQS2_VER}/mmseqs-linux-avx2.tar.gz && \
    tar -xvf mmseqs-linux-avx2.tar.gz && \
    rm mmseqs-linux-avx2.tar.gz

# get mafft
RUN wget https://mafft.cbrc.jp/alignment/software/mafft_${MAFFT_VER}-1_amd64.deb && \
    dpkg -i mafft_${MAFFT_VER}-1_amd64.deb && \
    rm mafft_${MAFFT_VER}-1_amd64.deb

# get python dependencies 
RUN pip install gmpy2 networkx numpy tables plotly pandas colorlover bokeh scipy tqdm

# get PPanGGOLiN
RUN wget -q https://github.com/labgem/PPanGGOLiN/archive/refs/tags/${PPANGGOLIN_VER}.tar.gz && \
    python3 -m pip install ${PPANGGOLIN_VER}.tar.gz && \
    rm -rf ${PPANGGOLIN_VER}.tar.gz && \
    mkdir /data

RUN ppanggolin -h

ENV PATH="/mmseqs/bin:$PATH" LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD ppanggolin -h

# 'WORKDIR' sets working directory
WORKDIR /data

FROM app as test

ARG PPANGGOLIN_VER

WORKDIR /test

RUN ppanggolin --help && \
    ppanggolin --version && \
    aragorn -h && \
    prodigal -h && \
    which mafft && \
    cmbuild -h && \
    mmseqs -h

RUN wget -q https://github.com/labgem/PPanGGOLiN/archive/refs/tags/${PPANGGOLIN_VER}.tar.gz && \
    tar -xvf ${PPANGGOLIN_VER}.tar.gz && \
    ppanggolin annotate --fasta ppanggolin-${PPANGGOLIN_VER}/testingDataset/organisms.fasta.list