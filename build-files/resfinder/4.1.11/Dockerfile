FROM ubuntu:focal as app

# ARG sets environment variables during the build stage
ARG RESFINDER_VER="4.1.11"
ARG KMA_VER="1.4.3"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:focal"
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

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
# ncbi-blast+ is v2.9.0
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 python3-pip \
 ncbi-blast+ \
 gzip \
 procps \
 libz-dev \
 git \
 build-essential && \
 rm -rf /var/lib/apt/lists/* && apt-get autoclean

# download ResFinder code; checkout 4.1.11 tag
RUN git clone https://bitbucket.org/genomicepidemiology/resfinder.git && \
 cd resfinder && \
 git checkout tags/${RESFINDER_VER}

# Install python dependencies
RUN pip3 install tabulate \
 biopython \
 cgecore \
 gitpython \
 python-dateutil

# Install kma
RUN wget https://bitbucket.org/genomicepidemiology/kma/get/${KMA_VER}.tar.gz && \
 mkdir kma && \
 tar -xvf ${KMA_VER}.tar.gz -C kma --strip-components 1 && \
 cd kma && make && \
 mv kma* /usr/local/bin/

# pointfinder database install
# since there is not versioning: using git commit bfa1754 from 2022-04-22 (https://bitbucket.org/genomicepidemiology/pointfinder_db/commits/bfa17543d776faf3962ba1e824dec5f55a66d73b)
RUN cd /resfinder && \
 git clone https://git@bitbucket.org/genomicepidemiology/pointfinder_db.git db_pointfinder && \
 cd db_pointfinder && \
 git checkout bfa1754 && \
 python3 INSTALL.py /usr/local/bin/kma_index non_interactive

# resfinder database install
# since there is no versioning: using git commit a4cc8bc from 2022-07-19 (https://bitbucket.org/genomicepidemiology/resfinder_db/commits/a4cc8bc1e969b3829ad0f0bd4a6cadf615ac9f21)
RUN cd /resfinder && \
 git clone https://git@bitbucket.org/genomicepidemiology/resfinder_db.git db_resfinder && \
 cd db_resfinder && \
 git checkout a4cc8bc && \
 python3 INSTALL.py /usr/local/bin/kma_index non_interactive

# so that run_resfinder.py is in the PATH
ENV PATH="${PATH}:/resfinder"

# make all resfinder files readable and executable by all
RUN chmod 755 -R /resfinder/ 

WORKDIR /data

FROM app as test

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
  for ISOLATE in 01 02 03 ; do \
    run_resfinder.py -ifa /resfinder/tests/data/test_isolate_${ISOLATE}.fa -o /data/test_resfinder_fastaInput_isolate_${ISOLATE} -acq -l 0.9 -t 0.9; \
  done && \
ls /data/test_resfinder_fastaInput_*

# run resfinder on supplied fastq files for gene detection (-acq for acquired genes, and -c -s "Escherichia coli" for point mutations)
RUN echo "TESTING RESFINDER ON SUPPLIED FASTQ FILES FOR ACQUIRED GENES AND POINT MUTATIONS" && \
  for ISOLATE in 01 05 09a 09b ; do \
    run_resfinder.py -ifq /resfinder/tests/data/test_isolate_${ISOLATE}_1.fq /resfinder/tests/data/test_isolate_${ISOLATE}_2.fq \
      -o /data/test_resfinder_fastqInput_isolate_${ISOLATE} \
      -acq -l 0.9 -t 0.9\
      -c -s "Escherichia coli"; \
  done && \
ls /data/test_resfinder_fastqInput_*

# run resfinder on supplied fasta files for point mutation detection (-c and --species for point mutations, NOT acquired resistance genes)
RUN echo "TESTING RESFINDER ON SUPPLIED FASTA FILES FOR POINT MUTAITON DETECTION" && \
  for ISOLATE in 05 09a 09b ; do \
    run_resfinder.py -ifa /resfinder/tests/data/test_isolate_${ISOLATE}.fa -o /data/test_pointfinder_fastaInput_isolate_${ISOLATE} -c --species "Escherichia coli"; \
  done && \
ls /data/test_pointfinder*

# look for expected outputs in resulting files; grep exits 1 if term is not found, meaning test layer will not build properly
RUN echo "FASTA INPUTS, SEARCHING FOR EXPECTED (RESFINDER) OUTPUTS:" && \
 grep 'blaB-2' /data/test_resfinder_fastaInput_isolate_01/ResFinder_results_tab.txt && \
 grep 'blaCTX' /data/test_resfinder_fastaInput_isolate_02/ResFinder_results_tab.txt && \
 grep -B 1 'No hit found' /data/test_resfinder_fastaInput_isolate_03/ResFinder_results_table.txt && \
 echo "FASTQ INPUT TESTS, SEARCHING FOR EXPECTED (POINTFINDER AND RESFINDER) OUTPUTS:" && \
 grep "blaB-2" /data/test_resfinder_fastqInput_isolate_01/ResFinder_results_tab.txt && \
 grep "gyrA p.S83A" /data/test_resfinder_fastqInput_isolate_05/PointFinder_table.txt && \
 grep "gyrA p.G81D" /data/test_resfinder_fastqInput_isolate_09a/PointFinder_table.txt && \
 grep "gyrA p.G81D" /data/test_resfinder_fastqInput_isolate_09b/PointFinder_table.txt && \
 echo "FASTA INPUTS, SEARCHING FOR EXPECTED (POINTFINDER) OUTPUTS:" && \
 grep "gyrA p.S83A" /data/test_pointfinder_fastaInput_isolate_05/PointFinder_table.txt && \
 grep "gyrA p.G81D" /data/test_pointfinder_fastaInput_isolate_09a/PointFinder_table.txt && \
 grep "gyrA p.G81D" /data/test_pointfinder_fastaInput_isolate_09b/PointFinder_table.txt && \
 grep "gyrA p.D82G" /data/test_pointfinder_fastaInput_isolate_09b/PointFinder_table.txt
