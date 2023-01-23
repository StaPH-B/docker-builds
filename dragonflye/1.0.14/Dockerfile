FROM mambaorg/micromamba:1.2.0 as app

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
ARG DRAGONFLYE_VER="1.0.14"

# metadata labels
LABEL base.image="mambaorg/micromamba:1.2.0"
LABEL dockerfile.version="1"
LABEL software="dragonflye"
LABEL software.version=${DRAGONFLYE_VER}
LABEL description="Conda environment for dragonflye. Dragonflye: Assemble bacterial isolate genomes from Nanopore reads."
LABEL website="https://github.com/rpetit3/dragonflye"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/rpetit3/dragonflye/blob/main/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates \
 git \
 procps \
 bsdmainutils && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

# commenting out for now since using bioconda/micromamba to install env
# # get the dragonflye repo
# RUN wget "https://github.com/cov-lineages/pangolin/archive/${DRAGONFLYE_VER}.tar.gz" && \
#  tar -xf ${DRAGONFLYE_VER}.tar.gz && \
#  rm ${DRAGONFLYE_VER}.tar.gz && \
#  mv -v pangolin-* pangolin

# modify environment.yml to pin specific versions during install
# create the conda environment using modified environment.yml
RUN micromamba install -n base -c conda-forge -c bioconda -c defaults -y dragonflye=${DRAGONFLYE_VER} && \
 micromamba clean -a -y && \
 mkdir /data

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# WORKDIR /pangolin

# run pip install step; download optional pre-computed assignment hashes for UShER (useful for running on large batches of samples)
# best to skip using the assigment-cache if running on one sample for speed
# print versions
# RUN pip install . && \
#  pangolin --add-assignment-cache && \
#  micromamba clean -a -y && \
#  mkdir /data && \
#  pangolin --all-versions && \
#  usher --version

WORKDIR /data

# hardcode pangolin executable into the PATH variable
ENV PATH="$PATH:/opt/conda/bin/" \
 LC_ALL=C.UTF-8

# new base for testing
FROM app as test

# so that mamba/conda env is active when running below commands
ENV ENV_NAME="base"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

RUN dragonflye --help && \
 dragonflye --check

# so that testing outputs are inside /test
WORKDIR /test

# download test data (ONT and ILMN FASTQs)
# modified code from here: https://github.com/rpetit3/dragonflye/blob/main/.github/workflows/test-dragonflye.yml
RUN echo "downloading ILMN and ONT test data from bactopia/bactopia-tests on GitHub..." && \
    wget https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/nanopore/ERR3772599.fastq.gz && \
    wget https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/illumina/SRR2838702_R1.fastq.gz && \
    wget https://raw.githubusercontent.com/bactopia/bactopia-tests/main/data/species/portiera/illumina/SRR2838702_R2.fastq.gz

# test assembly and polishing algorithms with test data
RUN echo "Testing Raven Assembler (quality filtered)..." && \
dragonflye --reads /test/ERR3772599.fastq.gz --prefix ERR3772599 --cpus 0 --nopolish --outdir raven-minquality --gsize 300000 --assembler raven --minquality 8 && \
echo "Test Raven Assembler (quality filtered, no length filter)..." \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --nopolish --outdir raven-minquality-nominreadlen --gsize 300000 --assembler raven --minquality 6 --minreadlen 0 && \
echo "Test Raven Assembler (quality filtered, no length filter, trimming)" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --nopolish --outdir raven-minquality-nominreadlen-trim --gsize 300000 --assembler raven --minquality 6 --minreadlen 0 --trim && \
echo "Test Raven Assembler (quality filtered, no length filter, trim opts)" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --nopolish --outdir raven-minquality-nominreadlen-trimopts --gsize 300000 --assembler raven --minquality 6 --minreadlen 0 --trim --trimopts '--adapter_threshold 95' && \
echo "Testing Raven Assembler" && \
dragonflye --reads /test/ERR3772599.fastq.gz --prefix ERR3772599-raven --cpus 0 --nopolish --depth 5 --outdir raven --gsize 300000 --assembler raven && \
echo "Testing Raven Assembler + Racon Polish" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --outdir raven-racon --gsize 300000 --assembler raven && \
echo "Testing Flye Assembler + Medaka Polish" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --outdir raven-medaka --gsize 300000 --assembler raven --racon 0 --model r103_min_high_g345 && \
echo "Testing Flye Assembler + Medaka Polish + --medaka_opts" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --outdir raven-medaka-opts --gsize 300000 --assembler raven --racon 0 --model r103_min_high_g345 --medaka_opts '-b 200' && \
echo "Testing Flye Assembler + Racon & Medaka Polish" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --outdir raven-both --gsize 300000 --assembler raven && \
echo "Testing Flye Assembler + Racon & Pilon Polish" && \
dragonflye --reads /test/ERR3772599.fastq.gz --R1 /test/SRR2838702_R1.fastq.gz --R2 /test/SRR2838702_R2.fastq.gz --cpus 0 --outdir raven-polypolish --gsize 300000 --assembler raven && \
echo "Testing Flye Assembler + Racon & Polypolish Polish" && \
dragonflye --reads /test/ERR3772599.fastq.gz --R1 /test/SRR2838702_R1.fastq.gz --R2 /test/SRR2838702_R2.fastq.gz --cpus 0 --outdir raven-pilon --gsize 300000 --assembler raven --polypolish 0 --pilon 1 && \
echo "Testing Miniasm Assembler" && \
dragonflye --reads /test/ERR3772599.fastq.gz --prefix ERR3772599_mini.asm --cpus 1 --nopolish --outdir miniasm --gsize 300000 --assembler miniasm && \
echo "Testing Flye Assembler" && \
dragonflye --reads /test/ERR3772599.fastq.gz --cpus 0 --nopolish --outdir flye --gsize 300000 --assembler flye && \
echo "Testing Flye Assembler (with --nano-hq)" && \
dragonflye --reads /test/ERR3772599.fastq.gz --prefix ERR3772599-nano.hq --cpus 0 --nopolish --outdir flyehq --gsize 300000 --assembler flye --nanohq && \
echo "Testing --list_models" && \
dragonflye --list_models 2>&1 | grep r941_min_sup_g507
