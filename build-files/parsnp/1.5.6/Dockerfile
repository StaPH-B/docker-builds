# Global args persist across stages
ARG PARSNP_VER="1.5.6"
ARG HARVEST_VER="1.3"

FROM ubuntu:xenial as builder
ARG PARSNP_VER
ARG HARVEST_VER

# ARG variables only persist during build time
ARG PYTHON_VER="3.6.14"
ARG NUMPY_VER="1.19.5"
ARG RAXML_VER="8.2.12"
ARG FASTTREE_VER="2.1.11"
ARG MASH_VER="2.3"

# Metadata
LABEL base.image="ubuntu:xenial"
LABEL software="ParSNP"
LABEL software.version=${PARSNP_VER}
LABEL description="ParSNP: Rapid core genome multi-alignment."
LABEL website="https://harvest.readthedocs.io/en/latest/content/parsnp.html"
LABEL license.url="https://github.com/marbl/parsnp/blob/master/LICENSE"

# Update package index, install packages (ParSNP basic dependencies and packages needed to build from source)
RUN apt-get update && apt-get install -y \
    autoconf \
    automake-1.15 \
    build-essential \
    capnproto \
    libcapnp-dev \
    libgsl0-dev \
    libprotobuf-dev \
    libssl-dev \
    libtool \
    protobuf-compiler \
    libsqlite3-dev \
    wget \
    zlib1g-dev

# Add /usr/lib to the library path so Mash and HarvestTools can find the capnp libraries
ENV LD_LIBRARY_PATH="/usr/lib:/usr/local/lib"

# Move some static libraries that Mash and HarvestTools demand to where they want to see them
RUN cp /usr/lib/x86_64-linux-gnu/libprotobuf.a /usr/lib/ && \
    cp /usr/lib/x86_64-linux-gnu/libcapnp.a /usr/lib/ && \
    cp /usr/lib/x86_64-linux-gnu/libkj.a /usr/lib/

# Install python3, pip3, and numpy
WORKDIR /
RUN wget https://www.python.org/ftp/python/$PYTHON_VER/Python-$PYTHON_VER.tgz
RUN tar xvf Python-$PYTHON_VER.tgz && rm Python-$PYTHON_VER.tgz
WORKDIR "/Python-$PYTHON_VER"
RUN ./configure --enable-loadable-sqlite-extensions && make && make install
RUN pip3 install numpy==$NUMPY_VER

# Create alias for ParSNP to use python3
RUN ln -s /usr/local/bin/python3 /usr/local/bin/python & \
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip

# Install FastTree: http://www.microbesonline.org/fasttree/#Install
WORKDIR /
RUN wget http://www.microbesonline.org/fasttree/FastTree.c
RUN gcc -O3 -finline-functions -funroll-loops -Wall -o /usr/local/bin/FastTree FastTree.c -lm

# ParSNP expects the FastTree executable to be called 'fasttree'
RUN ln -sf /usr/local/bin/FastTree /usr/local/bin/fasttree

# Install RAxML: https://cme.h-its.org/exelixis/resource/download/NewManual.pdf
RUN wget https://github.com/stamatak/standard-RAxML/archive/refs/tags/v$RAXML_VER.tar.gz
RUN tar xvf v$RAXML_VER.tar.gz
WORKDIR standard-RAxML-$RAXML_VER
RUN make -f Makefile.AVX.PTHREADS.gcc
RUN cp /standard-RAxML-$RAXML_VER/raxmlHPC-PTHREADS-AVX /usr/local/bin/raxmlHPC-PTHREADS

# Install Mash: https://github.com/marbl/Mash/blob/master/INSTALL.txt
WORKDIR /
RUN wget https://github.com/marbl/Mash/archive/refs/tags/v$MASH_VER.tar.gz
RUN tar xvf v$MASH_VER.tar.gz
WORKDIR Mash-$MASH_VER
RUN ./bootstrap.sh
RUN ./configure --with-capnp=/usr && make && make install

# Install PhiPack: https://www.maths.otago.ac.nz/~dbryant/software/phimanual.pdf
WORKDIR /
RUN wget https://www.maths.otago.ac.nz/~dbryant/software/PhiPack.tar.gz
RUN tar xvf PhiPack.tar.gz
WORKDIR PhiPack/src
RUN make
RUN cp /PhiPack/Phi /usr/local/bin && cp /PhiPack/Profile /usr/local/bin

# Install HarvestTools
WORKDIR /
RUN wget https://github.com/marbl/harvest-tools/archive/refs/tags/v$HARVEST_VER.tar.gz
RUN tar xvf v$HARVEST_VER.tar.gz
WORKDIR harvest-tools-$HARVEST_VER
RUN ./bootstrap.sh
RUN ./configure --with-protobuf=/usr --with-capnp=/usr --prefix=/usr/local && make && make install

# Install ParSNP
WORKDIR /
RUN wget https://github.com/marbl/parsnp/archive/v$PARSNP_VER.tar.gz
RUN tar xvf v$PARSNP_VER.tar.gz && rm v$PARSNP_VER.tar.gz

WORKDIR "/parsnp-$PARSNP_VER"/muscle
RUN ./autogen.sh
RUN ./configure CXXFLAGS='-fopenmp' && make install

WORKDIR "/parsnp-$PARSNP_VER"/
RUN ./autogen.sh
RUN export ORIGIN=\$ORIGIN
RUN ./configure LDFLAGS='-Wl,-rpath,$$ORIGIN/../muscle/lib' && make LDADD=-lMUSCLE-3.7 && make install

FROM ubuntu:xenial as app
ARG PARSNP_VER
ARG HARVEST_VER

# Copy necessary packages into the production image
COPY --from=builder /harvest-tools-$HARVEST_VER/ /harvest-tools-$HARVEST_VER/
COPY --from=builder /parsnp-$PARSNP_VER/ /parsnp-$PARSNP_VER/
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

# Put harvesttools & parsnp in PATH
ENV PATH="/harvest-tools-$HARVEST_VER:$PATH"
ENV PATH="/parsnp-$PARSNP_VER:$PATH"

# This is so that parsnp can find a MUSCLE library it needs
ENV LD_LIBRARY_PATH="/usr/local/lib"

RUN mkdir data/
WORKDIR data

FROM app as test
# IS_GITHUB only applicable for tests run by GitHub action
ARG IS_GITHUB

# Need wget for pulling test data
RUN apt-get update && apt-get install -y \
    wget

# For calculating Robinson-Foulds distance between trees
RUN pip install "robinson-foulds==1.1"
RUN pip install six

# Run the tests on app output
RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests