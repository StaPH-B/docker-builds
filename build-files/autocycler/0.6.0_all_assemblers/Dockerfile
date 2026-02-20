FROM mambaorg/micromamba:latest AS autocycler_all_assemblers

ARG AUTOCYCLER_VER="0.6.0"

LABEL base.image="mambaorg/micromamba:latest"
LABEL dockerfile.version="1"
LABEL software="Autocycler"
LABEL software.version="${AUTOCYCLER_VER}"
LABEL description="generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Autocycler"
LABEL license="https://github.com/rrwick/Autocycler/blob/main/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

# Create env + install tools supplied by rrwick at https://github.com/rrwick/Autocycler/blob/main/pipelines/Dockerfile_by_Ryan_Wick/Dockerfile
RUN micromamba create -y -n autocycler python=3.12 -c conda-forge -c bioconda curl \
 && for tool in canu flye lja metamdbg miniasm minimap2 minipolish necat nextdenovo nextpolish racon raven-assembler wtdbg; do \
        if micromamba install -y -n autocycler -c conda-forge -c bioconda "$tool"; then \
            printf " $tool" >> /tmp/installed_tools.txt; \
        else \
            printf " $tool" >> /tmp/missing_tools.txt; \
        fi; \
    done \
 && printf "\n" >> /tmp/installed_tools.txt \
 && printf "\n" >> /tmp/missing_tools.txt \
 && micromamba clean --all --yes

# Put env first on PATH
ENV PATH="/opt/conda/envs/autocycler/bin:$PATH"
ENV LC_ALL=C


# Downloading autocycler and moving it to appropriate env path.
WORKDIR /temp
RUN curl -L -o autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz \
    https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    tar -xzf autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    mv autocycler /opt/conda/envs/autocycler/bin/ && \
    rm autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz

# Testing to see if path is designated properly.
RUN autocycler --help && autocycler --version

WORKDIR /data


# Test stage
FROM autocycler_all_assemblers AS test

ARG AUTOCYCLER_VER

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

# demo dataset does not change with version
RUN curl -L -o autocycler-demo-dataset.tar\
    https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -vxf autocycler-demo-dataset.tar && \
    autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --genome_size "242000"