FROM mambaorg/micromamba:2.8.1-ubuntu24.04 AS app

ARG LISSERO_VERSION="0.4.10"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.8.1-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="LisSero"
LABEL software.version="${LISSERO_VERSION}"
LABEL description="In silico serogroup typing of Listeria monocytogenes"
LABEL website="https://github.com/MDU-PHL/LisSero"
LABEL license="https://github.com/MDU-PHL/LisSero/blob/master/LICENSE"
LABEL maintainer="Arnold Rodriguez"
LABEL maintainer.email="arnold.rodriguezhilario@flhealth.gov"

# lissero pulls python and blast; procps-ng provides ps; wget is used by the test stage
RUN micromamba install --yes --name base -c conda-forge -c bioconda \
    lissero=${LISSERO_VERSION} procps-ng wget && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "lissero", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

# serotype 4b reference (F2365, GCF_000008285.1); expect serogroup "4b, 4d, 4e"
RUN wget -q "https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/008/285/GCF_000008285.1_ASM828v1/GCF_000008285.1_ASM828v1_genomic.fna.gz" && \
    gunzip GCF_000008285.1_ASM828v1_genomic.fna.gz && \
    lissero GCF_000008285.1_ASM828v1_genomic.fna | tee lissero_test.tsv && \
    grep "4b, 4d, 4e" lissero_test.tsv

RUN lissero --version && \
    blastn -version
