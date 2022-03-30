FROM continuumio/miniconda:4.7.12

# Version arguments
ARG FREYJA_SOFTWARE_VERSION="1.2.0"

LABEL base.image="continuumio/miniconda:4.7.12"
LABEL dockerfile.version="1"
LABEL software="Freyja"
LABEL software.version=${FREYJA_SOFTWARE_VERSION}
LABEL description="Freyja is a tool to recover relative lineage abundances from mixed SARS-CoV-2 samples from a sequencing dataset (BAM aligned to the Hu-1 reference)"
LABEL website="https://github.com/andersen-lab/Freyja"
LABEL license="https://github.com/andersen-lab/Freyja/blob/main/LICENSE"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@theiagen.com"

# Create Freyja conda environment and add to PATH
RUN conda create -n freyja-env -c defaults -c bioconda -c conda-forge freyja=${FREYJA_SOFTWARE_VERSION} \
&& echo "source activate freyja-env" > ~/.bashrc

ENV PATH /opt/conda/envs/freyja-env/bin:/opt/conda/envs/env/bin:$PATH

# set working directory to /data
WORKDIR /data
