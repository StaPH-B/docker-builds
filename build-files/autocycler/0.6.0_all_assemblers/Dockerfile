FROM mambaorg/micromamba:2.5.0-ubuntu24.04 AS app

ARG AUTOCYCLER_VER="0.6.1"

USER root
WORKDIR /

LABEL base.image="mambaorg/micromamba:2.5.0-ubuntu24.04"
LABEL dockerfile.version="1"
LABEL software="Autocycler"
LABEL software.version="${AUTOCYCLER_VER}"
LABEL description="Generating consensus long-read assemblies for bacterial genomes"
LABEL website="https://github.com/rrwick/Autocycler"
LABEL license="https://github.com/rrwick/Autocycler/blob/main/LICENSE"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

COPY environment.yml /tmp/environment.yml

RUN micromamba install -y --name base -f /tmp/environment.yml && \
    micromamba clean -a -f -y && \
    mkdir /data

# Put env first on PATH
ENV PATH="/opt/conda/bin/:${PATH}" \
 LC_ALL=C.UTF-8

# Downloading autocycler and moving it to appropriate env path.
WORKDIR /opt/conda/bin
RUN curl -L -o autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz \
    https://github.com/rrwick/Autocycler/releases/download/v${AUTOCYCLER_VER}/autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    tar -xzf autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz && \
    rm autocycler-linux-x86_64-musl-v${AUTOCYCLER_VER}.tar.gz

# Testing to see if path is designated properly.
RUN autocycler --help && autocycler --version

# Ensure long read assemblers and helper software are installed by micromamba.
RUN micromamba list | grep -E "canu|curl|flye|metamdbg|miniasm|minimap2|minipolish|myloasm|necat|nextdenovo|nextpolish|plassembler|racon|raven-assembler|wtdbg"

WORKDIR /data


# Test stage
FROM app AS test

WORKDIR /test

RUN autocycler --help && \
    autocycler --version

# Download and test with demo dataset containing reads.fasta.gz
RUN curl -L -o autocycler-demo-dataset.tar\
    https://github.com/rrwick/Autocycler/releases/download/v0.1.0/autocycler-demo-dataset.tar && \
    tar -vxf autocycler-demo-dataset.tar

RUN threads=16 && \
    genome_size=$(autocycler helper genome_size --reads reads.fastq.gz --threads "$threads") && \
    echo "Genome size: $genome_size" && \
    # Step 1: subsample the long-read set into multiple files
    autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --genome_size "$genome_size" && \
    # Step 2: assemble each subsampled file
    mkdir assemblies && \
    for assembler in canu flye metamdbg miniasm necat nextdenovo plassembler raven; do \
        for i in 01 02 03 04; do \
            autocycler helper "$assembler" --reads subsampled_reads/sample_"$i".fastq --out_prefix assemblies/"$assembler"_"$i" --threads "$threads" --genome_size "$genome_size"; \
        done; \
    done && \
    # Optional step: remove the subsampled reads to save space
    rm subsampled_reads/*.fastq && \
    # Step 3: compress the input assemblies into a unitig graph
    autocycler compress -i assemblies -a autocycler_out && \
    # Step 4: cluster the input contigs into putative genomic sequences
    autocycler cluster -a autocycler_out && \
    # Steps 5 and 6: trim and resolve each QC-pass cluster
    for c in autocycler_out/clustering/qc_pass/cluster_*; do \
        autocycler trim -c "$c" && \
        autocycler resolve -c "$c"; \
    done && \
    # Step 7: combine resolved clusters into a final assembly
    autocycler combine -a autocycler_out -i autocycler_out/clustering/qc_pass/cluster_*/5_final.gfa && \
    autocycler subsample --reads reads.fastq.gz --out_dir subsampled_reads --genome_size "242000"