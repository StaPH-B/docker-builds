FROM continuumio/miniconda:4.7.12 as app

# for easy upgrade later. ARG variables only persist during image build time
ARG SMALT_VER="0.7.6"
ARG SAMTOOLSVER="1.15"
ARG BAMVER="0.0.50"

# metadata
LABEL base.image="continuumio/miniconda:4.7.12"
LABEL dockerfile.version="1"
LABEL software="Smalt"
LABEL software.version="0.7.6"
LABEL description="SMALT aligns DNA sequencing reads with a reference genome."
LABEL website="https://www.sanger.ac.uk/tool/smalt-0/"
LABEL license="https://www.sanger.ac.uk/tool/smalt-0/"
LABEL maintainer1="Jill Hagey"
LABEL maintainer.email1="jvhagey@gmail.com"

# set the environment
ENV PATH="/miniconda/bin:$PATH"

RUN conda config --add channels defaults && \
    conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda install smalt=${SMALT_VER} samtools=${SAMTOOLSVER} bambamc=${BAMVER} && \
    conda install -c anaconda wget=1.20.1 && \
    conda clean -a -y

# set perl locale settings
# Required by most tools that use perl with singularity so we can use container with both docker and singularity
ENV LC_ALL=C

# Add references and entrypoint script
WORKDIR /data

# new base for testing
FROM app as test

# Grab test data
COPY tests/ /data/

# Run Smalt
RUN wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/819/615/GCF_000819615.1_ViralProj14015/GCF_000819615.1_ViralProj14015_genomic.fna.gz
RUN smalt index -k 13 -s 6 test_PhiX174 GCF_000819615.1_ViralProj14015_genomic.fna.gz

# Check validity of outputs
RUN cmp /data/test_PhiX174.smi /data/PhiX174.smi  && cmp /data/test_PhiX174.sma /data/PhiX174.sma
