FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

USER root
WORKDIR /

ARG GENOFLU_VER="1.07-0"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="genoflu"
LABEL software.version="$GENOFLU_VER"
LABEL description="Uses BLAST to detect whole-genome flu genotype"
LABEL website="https://github.com/USDA-VS/GenoFLU"
LABEL license="https://github.com/USDA-VS/GenoFLU/blob/main/LICENSE"
LABEL maintainer="Sage Wright"
LABEL maintainer.email="sagemwright@gmail.com"

# Install dependencies via apt-get; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install genoflu via bioconda; install into 'base' conda env
# genoflu is not recognized in micromamba by the version tag
RUN micromamba install --yes --name base --channel conda-forge --channel bioconda \
    genoflu=${GENOFLU_VER} && \
    micromamba clean --all --force-pkgs-dirs --yes

# ENV instructions set environment variables that persist from the build into the resulting image
# hardcode 'base' env bin into PATH, so conda env does not have to be "activated" at run time
ENV PATH="/opt/conda/bin:${PATH}"

# WORKDIR sets working directory
WORKDIR /data

# default command is to pull up help options for genoflu
CMD [ "genoflu.py", "--help" ]

# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app AS test

# install unzip for unzipping zip archive from NCBI
RUN apt-get update && apt-get install -y --no-install-recommends unzip

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN echo "Downloading and installing NCBI datasets tool... " && \
wget -q https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
chmod +x datasets && \
mv -v datasets /usr/local/bin

# download test H5N1 genome, should be genotype D1.8 which was assigned in v1.07 of GenoFlu
# https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_055461155.1/
RUN datasets download genome accession GCA_055461155.1 && \
unzip -o ncbi_dataset.zip && \
rm -v ncbi_dataset.zip && \
mv -v ncbi_dataset/data/GCA_055461155.1/GCA_055461155.1_ASM5546115v1_genomic.fna . && \
genoflu.py -f GCA_055461155.1_ASM5546115v1_genomic.fna && \
grep 'D1.8' *_stats.tsv

# getting all the exectubles in bin
RUN genoflu.py --help && genoflu.py --version

# testing a genome
RUN wget -q https://raw.githubusercontent.com/USDA-VS/GenoFLU/main/test/test-genome-A1.fasta && \
  genoflu.py -f test-genome-A1.fasta

# for generating list of packages installed via micromamba in tool-specific README
RUN micromamba list
