FROM ubuntu:jammy AS app

# to make it easier to upgrade for new versions; ARG variables only persist during docker image build time
ARG SPADES_VER="4.2.0"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SPAdes"
LABEL software.version="${SPADES_VER}"
LABEL description="de novo DBG genome assembler"
LABEL website="https://github.com/ablab/spades"
LABEL license="https://github.com/ablab/spades/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
# python v3.8.10 is installed here; point 'python' to python3
RUN apt-get update && apt-get install --no-install-recommends -y \
  python3 \
  python3-distutils \
  wget \
  pigz \
  ca-certificates \
  libgomp1 && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/* && \
  update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# install SPAdes binary; make /data
RUN wget -q https://github.com/ablab/spades/releases/download/v${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm -r SPAdes-${SPADES_VER}-Linux.tar.gz && \
  mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C.UTF-8 \
  PATH="${PATH}:/SPAdes-${SPADES_VER}-Linux/bin"

CMD ["spades.py", "--help"]

WORKDIR /data

# test layer
FROM app AS test

# print version and run the supplied test flag
RUN spades.py --version && spades.py --help

# run the supplied test
RUN spades.py --test

WORKDIR /test

# run on some test files
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR323/020/SRR32343420/SRR32343420_1.fastq.gz && \
  wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR323/020/SRR32343420/SRR32343420_2.fastq.gz && \
  spades.py --isolate -1 SRR32343420_1.fastq.gz -2 SRR32343420_2.fastq.gz --threads 4 -o test && \
  head /test/test/contigs.fasta
