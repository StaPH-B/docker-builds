FROM mambaorg/micromamba:1.5.8 as app

USER root
WORKDIR /

ARG GENOFLU_VER="1.03-0"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="micromamba:1.5.8"
LABEL dockerfile.version="1"
LABEL software="genoflu"
LABEL software.version=$GENOFLU_VER
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
FROM app as test

# getting all the exectubles in bin
RUN genoflu.py --help && genoflu.py --version

# testing a genome
RUN wget -q https://raw.githubusercontent.com/USDA-VS/GenoFLU/main/test/test-genome-A1.fasta && \
  genoflu.py -f test-genome-A1.fasta 