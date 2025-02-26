FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist during image build time
ARG MINIMAP2_VER="2.28"

# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="Minimap2"
LABEL software.version="${MINIMAP2_VER}"
LABEL description="versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database"
LABEL website="https://github.com/lh3/minimap2"
LABEL license="https://github.com/lh3/minimap2/blob/master/LICENSE.txt"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="Kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# install deps and cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    bzip2 \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install minimap2 binary; make /data
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 | tar -jxvf - --no-same-owner && \
    mkdir /data

# set final PATH and LC_ALL for singularity compatibility
ENV PATH="${PATH}:/minimap2-${MINIMAP2_VER}_x64-linux" \
LC_ALL=C

# set final working directory as /data
WORKDIR /data

CMD minimap2 -h

# test layer
FROM app as test

RUN minimap2 -h

# use /test as working directory for tests
WORKDIR /test

# git clone minimap2 github repo solely for the purpose of getting test data files
# the minimap2 command used below is that installed in the 'app' layer, proven by the output of "command -v minimap2"
# lastly, I'm using the test commands listed here: https://github.com/lh3/minimap2#getting-started
RUN apt-get update && apt-get install -y --no-install-recommends git wget && \
    git clone https://github.com/lh3/minimap2 && \
    cd minimap2 && \
    echo && \
    echo "double checking that the 'minimap2' command used below is the executable installed in the app stage of the docker image. Here is the path:" && \
    command -v minimap2 && \
    echo && \
    minimap2 -a test/MT-human.fa test/MT-orang.fa > test.sam && \
    minimap2 -x map-ont -d MT-human-ont.mmi test/MT-human.fa && \
    minimap2 -a MT-human-ont.mmi test/MT-orang.fa > test.sam && \
    minimap2 --version

# downloading some actual data
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/943/119/195/GCA_943119195.1_2015LSAL00020/GCA_943119195.1_2015LSAL00020_genomic.fna.gz && \
    gzip -d GCA_943119195.1_2015LSAL00020_genomic.fna.gz && \
    wget https://zenodo.org/records/10733190/files/df_test_files.tar.gz && \
    tar -xvf df_test_files.tar.gz && \
    minimap2 -x lr:hq -a GCA_943119195.1_2015LSAL00020_genomic.fna test_files/test.fastq.gz > lrhq_test.sam