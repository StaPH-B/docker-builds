ARG USHER_VER="0.6.3"

FROM ubuntu:jammy as builder

ARG USHER_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    python3 \
    mafft \
    libisal-dev \
    libtbb-dev \
    python3-pip \
    sudo \
    cmake \
    make \
    gcc \
    g++ \
    protobuf-compiler \
    libprotobuf-dev \
    openmpi-bin \
    openmpi-common \
    libopenmpi-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/yatisht/usher/archive/refs/tags/v${USHER_VER}.tar.gz && \
    tar -xvf v${USHER_VER}.tar.gz && \
    rm v${USHER_VER}.tar.gz && \
    cd /usher-${USHER_VER} && \
    ./install/installUbuntu.sh 

FROM ubuntu:jammy as app

ARG USHER_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="UShER"
LABEL software.version="${USHER_VER}"
LABEL description="Ultrafast Sample Placement on Existing Trees."
LABEL website="https://github.com/yatisht/usher"
LABEL license="https://github.com/yatisht/usher/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    python3 \
    mafft \
    libisal-dev \
    libtbb-dev \
    python3-pip \
    libboost-all-dev \
    libtbb-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usher-${USHER_VER}/build/* /usher/build/
COPY --from=builder /usher-${USHER_VER}/scripts/* /usher/scripts/

RUN wget -q http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/faSomeRecords -O /usr/local/bin/faSomeRecords && \
    wget -q http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/faSize -O /usr/local/bin/faSize && \
    wget -q http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/faToVcf -O /usr/local/bin/faToVcf && \
    chmod 775 /usr/local/bin/faSize /usr/local/bin/faSomeRecords /usr/local/bin/faToVcf

ENV PATH="/usher/build/:/usher/scripts/:$PATH" \
    LC_ALL=C \
    LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

RUN ls /usr/lib/x86_64-linux-gnu && ln -s /usr/lib/x86_64-linux-gnu/libtbb_preview.so.12 /usr/lib/x86_64-linux-gnu/libtbb_preview.so.2

CMD [ "usher", "--help" ]

WORKDIR /data

FROM app as test

ARG USHER_VER

WORKDIR /usher-${USHER_VER}

RUN usher --help && \
    usher --version

# https://usher-wiki.readthedocs.io/en/latest/UShER.html
RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -d output/

RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -c -d output2/

RUN usher -t test/global_phylo.nh -v test/global_samples.vcf -o global_assignments.pb -c -u -d output3/

RUN usher -i global_assignments.pb -v test/new_samples.vcf -u -d output4/

RUN usher -i global_assignments.pb -v test/new_samples.vcf -u -k 20 -d output5/

RUN usher -i global_assignments.pb -v test/new_samples.vcf -u -o new_global_assignments.pb -d output6/