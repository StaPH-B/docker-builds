ARG RESFINDER_VER="4.7.2"

FROM ubuntu:jammy AS app

# ARG sets environment variables during the build stage
ARG RESFINDER_VER

# Database may not be properly versioned, but using a version tag here (2024-08-06)
# see here: https://bitbucket.org/genomicepidemiology/resfinder_db/downloads/?tab=tags
ARG RESFINDER_DB_COMMIT_HASH="2.6.0"

# Database may not be properly versioned, but using a version tag here (2024-08-08)
# see here: https://bitbucket.org/genomicepidemiology/pointfinder_db/downloads/?tab=tags
ARG POINTFINDER_DB_COMMIT_HASH="4.1.1"

# Database may not be properly versioned, but using a version tag here (2023-05-31)
# see here: https://bitbucket.org/genomicepidemiology/disinfinder_db/downloads/?tab=tags
ARG DISINFINDER_DB_COMMIT_HASH="2.0.1"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="resfinder"
LABEL software.version=${RESFINDER_VER}
LABEL description="Identifies acquired resistance genes and point mutations in total or partial sequenced isolates of bacteria."
LABEL website="https://bitbucket.org/genomicepidemiology/resfinder/src/master/"
LABEL license="https://bitbucket.org/genomicepidemiology/resfinder/src/master/README.md"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# so that apt doesn't ask for a region during apt install step
ARG DEBIAN_FRONTEND noninteractive

# install dependencies; cleanup apt garbage 
# ncbi-blast+ 2.12.0+ds-3build1 (ubuntu:jammy)
# python3 v3.10
# uses git at runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  ca-certificates \
  procps \
  ncbi-blast+ \
  python3 \
  python3-pip \
  python3-setuptools \
  python3-dev \
  libz-dev \
  unzip \
  git \
  kma && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install resfinder ()
# It is no longer recommended to clone the ResFinder bitbucket repository unless you plan to do development work on ResFinder.
# Instead we recommend installing ResFinder using pip...
# https://bitbucket.org/genomicepidemiology/resfinder/src/master/ 2024-03-21
RUN pip3 install --no-cache-dir resfinder==${RESFINDER_VER} && \
  mkdir /data

# resfinder database install
RUN mkdir /resfinder_db && \
  wget https://git@bitbucket.org/genomicepidemiology/resfinder_db/get/${RESFINDER_DB_COMMIT_HASH}.tar.gz && \
  tar -C /resfinder_db --strip-components=1 -xvf ${RESFINDER_DB_COMMIT_HASH}.tar.gz && \
  rm -rf ${RESFINDER_DB_COMMIT_HASH}.tar.gz && \
  cd /resfinder_db && \
  python3 INSTALL.py kma_index non_interactive

# pointfinder database install
RUN mkdir /pointfinder_db && \
  wget https://git@bitbucket.org/genomicepidemiology/pointfinder_db/get/${POINTFINDER_DB_COMMIT_HASH}.tar.gz && \
  tar -C /pointfinder_db --strip-components=1 -xvf ${POINTFINDER_DB_COMMIT_HASH}.tar.gz && \
  rm -rf ${POINTFINDER_DB_COMMIT_HASH}.tar.gz && \
  cd /pointfinder_db && \
  python3 INSTALL.py kma_index non_interactive

# disinfinder database install
RUN mkdir /disinfinder_db && \
  wget https://git@bitbucket.org/genomicepidemiology/disinfinder_db/get/${DISINFINDER_DB_COMMIT_HASH}.tar.gz && \
  tar -C /disinfinder_db --strip-components=1 -xvf ${DISINFINDER_DB_COMMIT_HASH}.tar.gz && \
  rm -rf ${DISINFINDER_DB_COMMIT_HASH}.tar.gz && \
  cd /disinfinder_db && \
  python3 INSTALL.py kma_index non_interactive

# so that run_resfinder.py is in the PATH
ENV PATH="${PATH}" \
  # specifying database locations
  CGE_RESFINDER_RESGENE_DB="/resfinder_db" \
  CGE_RESFINDER_RESPOINT_DB="/pointfinder_db" \
  CGE_DISINFINDER_DB="/disinfinder_db"

CMD ["python3", "-m", "resfinder", "-h"]

WORKDIR /data

FROM app AS test

ARG RESFINDER_VER

# checking suggested usage
RUN python3 -m resfinder -h

WORKDIR /test

# getting test files
RUN wget https://git@bitbucket.org/genomicepidemiology/resfinder/get/${RESFINDER_VER}.tar.gz && \
  tar -vxf ${RESFINDER_VER}.tar.gz && \
  mv genomicepi* resfinder

##### short description of included test files #####
### test files for typical gene detection (or lack thereof)
# test_isolate_01.fa fasta header ">test_isolate_01 blaB-2_1_AF189300"
# test_isolate_02.fa fasta header ">test_isolate_02 blaCTX-M-33_1_AY238472"
# test_isolate_03.fa fasta header ">test_isolate_03 no_res"

### test FASTA files for point mutation detection
# test_isolate_05.fa fasta header ">test_isolate_05 gyrA_mut
# test_isolate_09a.fa fasta header ">gyrA_G81D_GGT241GAT"
# test_isolate_09b.fa fasta header ">gyrA_G81D_GAT_D82G_GGC"

# test fastq files are also available for isolates 01, 05, 09a, and 09b. They are used to test KMA's functionality
# run resfinder on supplied fasta files for gene detection (-acq for acquired genes, NOT point mutations)
RUN echo "TESTING RESFINDER ON SUPPLIED FASTA FILES FOR ACQUIRED GENES" && \
  for ISOLATE in 01 02 03; do \
    python3 -m resfinder -ifa /test/resfinder/tests/data/test_isolate_${ISOLATE}.fa -o test_resfinder_fastaInput_isolate_${ISOLATE} -acq -l 0.9 -t 0.9; \
  done && \
  ls test_resfinder_fastaInput_*

# run resfinder on supplied fastq files for gene detection (-acq for acquired genes, and -c -s "Escherichia coli" for point mutations)
RUN echo "TESTING RESFINDER ON SUPPLIED FASTQ FILES FOR ACQUIRED GENES AND POINT MUTATIONS" && \
  for ISOLATE in 01 05 09a 09b ; do \
    python3 -m resfinder -ifq /test/resfinder/tests/data/test_isolate_${ISOLATE}_1.fq /test/resfinder/tests/data/test_isolate_${ISOLATE}_2.fq \
      -o test_resfinder_fastqInput_isolate_${ISOLATE} \
      -acq -l 0.9 -t 0.9\
      -c -s "Escherichia coli"; \
  done && \
  ls test_resfinder_fastqInput_*

# run resfinder on supplied fasta files for point mutation detection (-c and --species for point mutations, NOT acquired resistance genes)
RUN echo "TESTING RESFINDER ON SUPPLIED FASTA FILES FOR POINT MUTAITON DETECTION" && \
  for ISOLATE in 05 09a 09b ; do \
    python3 -m resfinder -ifa /test/resfinder/tests/data/test_isolate_${ISOLATE}.fa -o test_pointfinder_fastaInput_isolate_${ISOLATE} -c --species "Escherichia coli"; \
  done && \
  ls test_pointfinder*

# look for expected outputs in resulting files; grep exits 1 if term is not found, meaning test layer will not build properly
RUN echo "FASTA INPUTS, SEARCHING FOR EXPECTED (RESFINDER) OUTPUTS:" && \
  grep 'blaB-2' test_resfinder_fastaInput_isolate_01/ResFinder_results_tab.txt && \
  grep 'blaCTX' test_resfinder_fastaInput_isolate_02/ResFinder_results_tab.txt && \
  grep -B 1 'No hit found' test_resfinder_fastaInput_isolate_03/ResFinder_results_table.txt && \
  echo "FASTQ INPUT TESTS, SEARCHING FOR EXPECTED (POINTFINDER AND RESFINDER) OUTPUTS:" && \
  grep "blaB-2" test_resfinder_fastqInput_isolate_01/ResFinder_results_tab.txt && \
  grep "gyrA p.S83A" test_resfinder_fastqInput_isolate_05/PointFinder_table.txt && \
  grep "gyrA p.G81D" test_resfinder_fastqInput_isolate_09a/PointFinder_table.txt && \
  grep "gyrA p.G81D" test_resfinder_fastqInput_isolate_09b/PointFinder_table.txt && \
  echo "FASTA INPUTS, SEARCHING FOR EXPECTED (POINTFINDER) OUTPUTS:" && \
  grep "gyrA p.S83A" test_pointfinder_fastaInput_isolate_05/PointFinder_table.txt && \
  grep "gyrA p.G81D" test_pointfinder_fastaInput_isolate_09a/PointFinder_table.txt && \
  grep "gyrA p.G81D" test_pointfinder_fastaInput_isolate_09b/PointFinder_table.txt && \
  grep "gyrA p.D82G" test_pointfinder_fastaInput_isolate_09b/PointFinder_table.txt
