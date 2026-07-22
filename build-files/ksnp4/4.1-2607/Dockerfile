FROM ubuntu:noble AS app

ARG KSNPVER=4.1

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="kSNP"
LABEL software.version="${KSNPVER}"
LABEL description="K-mer-based phylogenetic inference"
# There is a github repo, but it is not as updated as sourceforge
LABEL website="https://sourceforge.net/projects/ksnp/"
LABEL license="https://github.com/kissake/kSNP${KSNPVER}/blob/%40/THE%20BSD%20OPENSOURCE%20LICENSE.pdf"
LABEL maintainer="Jeremiah Nisbet"
LABEL maintainer.email="ksnp-dev@kissake.net"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    unzip \
    python3 \
    libgomp1 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

RUN wget -O kSNP.zip https://sourceforge.net/projects/ksnp/files/kSNP${KSNPVER}%20Linux%20package.zip && \
    unzip -j kSNP.zip "kSNP${KSNPVER} Linux package/kSNP${KSNPVER}pkg/*" &&\
    rm kSNP.zip &&\
    chmod +x * && ls -alh

ENV LC_ALL=C

CMD ["kSNP4"]

WORKDIR /data

## Test ##
FROM app AS test

RUN kSNP4 || echo "This prints to stderr for whatever reason"

# Adapted from RunExamples.sh https://raw.githubusercontent.com/kissake/kSNP4/refs/heads/%40/RunExamples.sh

# checking dependencies
RUN command -v jellyfish >/dev/null 2>&1    && echo "... Jellyfish found" && \
    command -v mummer >/dev/null 2>&1       && echo "... mummer found" && \
    command -v consense >/dev/null 2>&1     && echo "... consense found" && \
    command -v parsimonator >/dev/null 2>&1 && echo "... parsimonator found" && \
    command -v FastTreeMP >/dev/null 2>&1   && echo "... FastTree found" && \
    command -v kSNP4 >/dev/null 2>&1        && echo "... kSNP4 found"

WORKDIR /test

# Getting the example files
RUN wget https://sourceforge.net/projects/ksnp/files/Examples.zip/download && \
    mv download Examples.zip && \
    unzip Examples.zip

# Step 5: Test 1 - Basic SNP discovery on Example 1
RUN MakeKSNP4infile -indir Examples/Example1/Genomes -outfile Example1_test.in && \
    kSNP4 -in Example1_test.in -k 21 -outdir Test_Run1 && \
    ls Test_Run1/tree.parsimony.tre Test_Run1/SNPs_all

# Step 6: Test 2 - Kchooser4 run on Example 2
RUN MakeKSNP4infile -indir Examples/Example2/Genomes -outfile Example2_test.in && \
    Kchooser4 -in Example2_test.in

# Step 7: Test 3 - Multi-CPU run with rewritten annotation paths
RUN sed -i "s|/.*Examples/|$(pwd)/Examples/|g" Examples/Example2/Results/annotatedGenomes && \
    kSNP4 -in Example2_test.in -k 21 -CPU 2 -outdir Test_Run2 -annotate Examples/Example2/Results/annotatedGenomes && \
    ls Test_Run2/tree.parsimony.tre Test_Run2/SNPs_all_annotated
