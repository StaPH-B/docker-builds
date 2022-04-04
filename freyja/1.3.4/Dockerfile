FROM continuumio/miniconda:4.7.12 as app

# Version arguments
ARG FREYJA_SOFTWARE_VERSION="1.3.4"

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
RUN conda create -n freyja-env -c conda-forge -c bioconda -c defaults freyja=${FREYJA_SOFTWARE_VERSION} \
&& echo "source activate freyja-env" > ~/.bashrc

ENV PATH /opt/conda/envs/freyja-env/bin:/opt/conda/envs/env/bin:$PATH

# set working directory to /data
WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# Run Freyja
RUN freyja variants /data/Freyja_WWSC2.bam --variants /data/test_variants.tsv --depths /data/test_depths.tsv --ref /data/nCoV-2019.reference.fasta && freyja demix /data/test_variants.tsv /data/test_depths.tsv --output /data/test_demix.tsv

# Check outputs
RUN cat /data/test_demix.tsv && cat /data/Freyja_demix.tsv

# Check validity of outputs
RUN ["/bin/bash", "-c", "cmp /data/test_variants.tsv /data/Freyja_variants.tsv && cmp /data/test_depths.tsv /data/Freyja_depths.tsv && cmp /data/test_demix.tsv /data/Freyja_demix.tsv && echo done"]


