FROM mambaorg/micromamba:2.3.2-ubuntu22.04 AS app

# for easy upgrade later. ARG variables only persist during image build time
ARG KLEBORATE_VER="3.2.4"
ARG PYTHON_VER="3.9"
ARG MINIMAP2_VER="2.30"
ARG MASH_VER="2.3"
ARG AMRFINDERPLUS_VER="4.0.23"
ARG EZCLERMONT_VER="0.7.0"
ARG ECTYPER_VER="2.0.0"
ARG AMRFINDER_DB_VER="2025-07-16.1"
#NOTE: stxtyper is installed as part of amrfinderplus since it's a submodule of amrfinderplus. StxTyper v1.0.42 comes installed with amrfinderplus v4.0.23
#NOTE: dna_features_viewer is installed as a dependency of kleborate via pip (using kleborate's requirements.txt)

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Kleborate"
LABEL software.version="${KLEBORATE_VER}"
LABEL description="tool to screen genome assemblies of Klebsiella pneumoniae and the Klebsiella pneumoniae species complex (KpSC)"
LABEL website="https://github.com/katholt/Kleborate"
LABEL license="https://github.com/katholt/Kleborate/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# install prerequisites. Cleanup apt garbage
# unzip just needed for test stage. It's tiny so no harm to keep in APP stage
RUN apt-get update && apt-get install -y --no-install-recommends \
  unzip \
  wget \
  ca-certificates && \
  rm -rf /var/lib/apt/lists/* && apt-get autoclean

# setup base conda/micromamba environment with dependencies
RUN micromamba install --name base -c conda-forge -c bioconda python=${PYTHON_VER} minimap2=${MINIMAP2_VER} mash=${MASH_VER} ezclermont=${EZCLERMONT_VER} ectyper=${ECTYPER_VER} ncbi-amrfinderplus=${AMRFINDERPLUS_VER} && \
micromamba clean -a -f -y && \
mkdir /data

# set PATH
ENV PATH="/opt/conda/bin/:${PATH}" \
LC_ALL=C.UTF-8

# download amrfinder databases and index them
# done in this manner to pin the database version instead of pulling the latest version with `amrfinder -u` 
# softlink is required for `amrfinder -l` and typical `amrfinder` use cases to work properly
RUN mkdir -p /opt/conda/share/amrfinderplus/data/${AMRFINDER_DB_VER} && \
echo "Downloading amrfinder databases and indexing them now..." && \
wget -q -P /opt/conda/share/amrfinderplus/data/${AMRFINDER_DB_VER} ftp://ftp.ncbi.nlm.nih.gov/pathogen/Antimicrobial_resistance/AMRFinderPlus/database/4.0/${AMRFINDER_DB_VER}/* && \
amrfinder_index /opt/conda/share/amrfinderplus/data/${AMRFINDER_DB_VER} && \
ln -s /opt/conda/share/amrfinderplus/data/${AMRFINDER_DB_VER} /opt/conda/share/amrfinderplus/data/latest

# install kleborate; uninstall mash (that comes with kleborate via pypi, see: https://github.com/klebgenomics/Kleborate/issues/90); make /data
RUN pip install --no-cache-dir kleborate==${KLEBORATE_VER} pandas && \
pip uninstall mash -y

# set working directory
WORKDIR /data

CMD [ "kleborate", "--help" ]

FROM app AS test

WORKDIR /test

# from https://kleborate.readthedocs.io/en/latest/Installation.html
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/813/595/GCF_002813595.1_ASM281359v1/GCF_002813595.1_ASM281359v1_genomic.fna.gz && \
kleborate -a GCF_002813595.1_ASM281359v1_genomic.fna.gz -o kleborate_test -p kpsc && \
head kleborate_test/klebsiella_pneumo_complex_output.txt

# test e. coli specific modules
# STEC genome from here: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_018509925.1/
# expect to see stx2d_operon detected
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/018/509/925/GCA_018509925.1_PDT001047072.1/GCA_018509925.1_PDT001047072.1_genomic.fna.gz && \
gunzip GCA_018509925.1_PDT001047072.1_genomic.fna.gz && \
kleborate -a GCA_018509925.1_PDT001047072.1_genomic.fna -o kleborate_ecoli_test --preset escherichia && \
grep 'stx2d' kleborate_ecoli_test/escherichia_output.txt

# testing on another E. coli PNUSAE021029: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_012047485.2/
# Known to have both stx2a and stx2c operons
# Also known to be O157:H7 serotype
# ectyper should report 'EHEC' pathotype
# also known to have lots of virulence factors like eae, ehxA, many different esp genes (espA, espB, espJ, espK, espP, espX1)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/047/485/GCA_012047485.2_PDT000417198.3/GCA_012047485.2_PDT000417198.3_genomic.fna.gz && \
gunzip GCA_012047485.2_PDT000417198.3_genomic.fna.gz && \
kleborate -a GCA_012047485.2_PDT000417198.3_genomic.fna -o kleborate-ecoli-test2 --preset escherichia && \
grep 'stx2a' kleborate-ecoli-test2/escherichia_output.txt && \
grep 'stx2c' kleborate-ecoli-test2/escherichia_output.txt && \
grep 'O157:H7' kleborate-ecoli-test2/escherichia_output.txt && \
grep 'EHEC' kleborate-ecoli-test2/escherichia_output.txt && \
grep 'eae' kleborate-ecoli-test2/escherichia_output.txt 

# testing on a particularly drug-resistant E. coli PNUSAE020982: https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_012117185.1/
# known to have blaCTX-M-27, sul1, tet(A), dfrA17, erm(B), gyrA_D87N, gyrA_S83L, parC_S80I
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/117/185/GCA_012117185.1_PDT000432447.1/GCA_012117185.1_PDT000432447.1_genomic.fna.gz && \
gunzip GCA_012117185.1_PDT000432447.1_genomic.fna.gz && \
kleborate -a GCA_012117185.1_PDT000432447.1_genomic.fna -o kleborate-ecoli-test3 --preset escherichia && \
grep 'blaCTX-M-27' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'sul1' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'tet(A)' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'dfrA17' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'erm(B)' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'gyrA_D87N' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'gyrA_S83L' kleborate-ecoli-test3/escherichia_output.txt && \
grep 'parC_S80I' kleborate-ecoli-test3/escherichia_output.txt

# print help and version info
# list all tools installed via micromamba (put these in the tool-specific REAMDME.md)
RUN kleborate --help && \
kleborate --version && \
kleborate --list_modules && \
micromamba list -n base
