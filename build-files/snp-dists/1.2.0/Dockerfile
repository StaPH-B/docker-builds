ARG SNP_DISTS_VER=1.2.0

### Builder stage
FROM ubuntu:noble AS builder

ARG SNP_DISTS_VER

# install dependencies needed for compilation; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
wget \
ca-certificates \
procps \
make \
zlib1g \
gcc \
libz-dev \
build-essential \
git && \
apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install (recent version of) bats for testing framework since version in apt for ubuntu:noble does not include the "bats --abort" option
RUN git clone https://github.com/bats-core/bats-core.git && \
cd bats-core && \
./install.sh /usr/local

# install snp-dists; run make check and bats tests
# decided to run bats tests here since it uses binaries located within /snp-dists-<ver>/bin/ rather than installed version in /usr/local/bin/
RUN echo "Installing snp-dists version ${SNP_DISTS_VER}" && \
wget -q https://github.com/tseemann/snp-dists/archive/v${SNP_DISTS_VER}.tar.gz && \
tar -xzf v${SNP_DISTS_VER}.tar.gz && \
rm -v v${SNP_DISTS_VER}.tar.gz && \
cd /snp-dists-${SNP_DISTS_VER} && \
make && \
make check && \
make PREFIX=/usr/local install && \
echo "Running BATS tests..." && \
bats -T --abort test/test.sh

### app stage
FROM ubuntu:noble AS app

ARG SNP_DISTS_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="snp-dists"
LABEL software.version="${SNP_DISTS_VER}"
LABEL description="Convert a FASTA alignment to SNP distance matrix"
LABEL website="https://github.com/tseemann/snp-dists"
LABEL license="https://github.com/tseemann/snp-dists/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
wget \
ca-certificates \
procps \
zlib1g \
libgomp1 && \
apt-get autoclean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/snp-dists /usr/local/bin/snp-dists

# make /data and set as default working directory
RUN mkdir -v /data
WORKDIR /data

# set locale for singularity compatibility; no need to set PATH as /usr/local/bin is already there
ENV LC_ALL=C

CMD ["snp-dists", "--help"]

### Test stage
FROM app AS test

ARG SNP_DISTS_VER

RUN apt-get update && apt-get install -y --no-install-recommends \
wget \
ca-certificates && \
apt-get autoclean && rm -rf /var/lib/apt/lists/*

# setting working directory to /test
WORKDIR /test

# Run a simple test from snp-dists testing framework
RUN echo "Testing snp-dists with one test from testing framework..." && \
wget -q https://raw.githubusercontent.com/tseemann/snp-dists/refs/heads/master/test/good.aln && \
wget -q https://raw.githubusercontent.com/tseemann/snp-dists/refs/heads/master/test/good.res && \
snp-dists -b good.aln > good.out && \
diff -bB good.out good.res && \
echo "snp-dists version ${SNP_DISTS_VER} test completed successfully!"
