ARG PBPTYPER_VERSION="2.0.0"

FROM mambaorg/micromamba:1.5.8 as app

# Version arguments
# ARG variables only persist during build time
ARG PBPTYPER_VERSION

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="pbptyper"
LABEL software.version="${PBPTYPER_VERSION}"
LABEL description="In silico Penicillin Binding Protein (PBP) typer for Streptococcus pneumoniae assemblies"
LABEL website="https://github.com/rpetit3/pbptyper"
LABEL license="https://github.com/rpetit3/pbptyper/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="curtis.kapsak@theiagen.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Install pbptyper into the base conda/micromamba environment, pinning the version
# clean up conda garbage
RUN micromamba install --name base -c conda-forge -c bioconda -c defaults pbptyper=${PBPTYPER_VERSION} && \
    micromamba clean -a -f -y

# set the environment, add base conda/micromamba bin directory into path
# set locale settings to UTF-8
ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

# set final working directory to /data
WORKDIR /data

CMD pbptyper --help

# new base for testing
FROM app as test

ARG PBPTYPER_VERSION

RUN pbptyper --help && \
    pbptyper --version

# so that all test inputs & outputs are kept in /test
WORKDIR /test

# download test data from pbptyper repo
RUN wget -q https://github.com/rpetit3/pbptyper/archive/refs/tags/v${PBPTYPER_VERSION}.tar.gz && \
    tar -vxf v${PBPTYPER_VERSION}.tar.gz
    
# shamelessly stolen and modified from https://github.com/rpetit3/pbptyper/blob/main/.github/workflows/test-pbptyper.yml (again)
RUN cd pbptyper-${PBPTYPER_VERSION} && \
    echo "ERR1065617" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/ERR1065617.fna.gz --prefix ERR1065617 && \
    cat ERR1065617.tsv && \
    head ERR1065617.tblastn.tsv && \
    echo "SRR2912551" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/SRR2912551.fna.gz --prefix SRR2912551 && \
    cat SRR2912551.tsv && \
    head SRR2912551.tblastn.tsv && \
    echo "SRR8654742" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/SRR8654742.fna --prefix SRR8654742 --outdir SRR8654742 && \
    cat SRR8654742/SRR8654742.tsv && \
    head SRR8654742/SRR8654742.tblastn.tsv && \
    echo "S. pseudopneumoniae" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/spseudopneumoniae.fna.gz --prefix spseudopneumoniae --outdir spseudopneumoniae && \
    cat spseudopneumoniae/spseudopneumoniae.tsv && \
    head spseudopneumoniae/spseudopneumoniae.tblastn.tsv && \
    echo "S. mitis" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/smitis.fna.gz --prefix smitis --outdir smitis && \
    cat smitis/smitis.tsv && \
    head smitis/smitis.tblastn.tsv && \
    echo "S. suis" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/ssuis.fna.gz --prefix ssuis --outdir ssuis && \
    cat ssuis/ssuis.tsv && \
    head ssuis/ssuis.tblastn.tsv && \
    echo "not-spn" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/not-spn.fna.gz --prefix not-spn && \
    cat not-spn.tsv && \
    head not-spn.tblastn.tsv && \
    echo "not-a-fasta" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/not-a-fasta.fasta --prefix not-a-fasta && \
    cat not-a-fasta.tsv && \
    head not-a-fasta.tblastn.tsv && \
    echo "poor" && \
    pbptyper --yaml data/pbptyper.yaml --targets data/pbptyper.fasta --input test/poor.fasta --prefix poor --outdir poor && \
    cat poor/poor.tsv && \
    head poor/poor.tblastn.tsv

RUN cd pbptyper-${PBPTYPER_VERSION} && \
    echo "ERR1065617 again" && \
    pbptyper --input test/ERR1065617.fna.gz --prefix ERR1065617_2 && \
    cat ERR1065617_2.tsv && \
    head ERR1065617_2.tblastn.tsv
