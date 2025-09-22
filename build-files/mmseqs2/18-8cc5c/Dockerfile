FROM ubuntu:jammy AS app

ARG MMSEQS2_VER="18-8cc5c"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="MMseqs2"
LABEL software.version="${MMSEQS2_VER}"
LABEL description="MMseqs2 (Many-against-Many sequence searching) is a software suite to search and cluster huge protein and nucleotide sequence sets."
LABEL website="https://github.com/soedinglab/MMseqs2"
LABEL license="https://github.com/soedinglab/MMseqs2/blob/master/LICENSE.md"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/soedinglab/MMseqs2/releases/download/${MMSEQS2_VER}/mmseqs-linux-sse41.tar.gz && \
    tar -vxf mmseqs-linux-sse41.tar.gz && \
    rm mmseqs-linux-sse41.tar.gz

# 'ENV' instructions set environment variables that persist from the build into the resulting image
# Use for e.g. $PATH and locale settings for compatibility with Singularity
ENV PATH="/mmseqs/bin:$PATH" \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "mmseqs" ]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app AS test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

# print help and version info; check dependencies (not all software has these options available)
# Mostly this ensures the tool of choice is in path and is executable
RUN mmseqs && mmseqs --help && mmseqs version

# using the provided example files
RUN mmseqs easy-search /mmseqs/examples/QUERY.fasta /mmseqs/examples/DB.fasta alnResult.m8 tmp && \
    mmseqs easy-cluster /mmseqs/examples/DB.fasta clusterRes tmp && \
    mmseqs easy-linclust /mmseqs/examples/DB.fasta clusterRes tmp 

# stolen from https://github.com/soedinglab/MMseqs2/wiki/Tutorials
WORKDIR /tutorial

RUN wget -q http://wwwuser.gwdg.de/~compbiol/mmseqs2/tutorials/mystery_reads.fasta && \
    # Download the database
    wget -q http://wwwuser.gwdg.de/~compbiol/mmseqs2/tutorials/uniprot_sprot_2018_03.fasta.gz && \
    wget -q http://wwwuser.gwdg.de/~compbiol/mmseqs2/tutorials/uniprot_sprot_2018_03_mapping.tsv.gz && \
    gunzip uniprot_sprot_2018_03_mapping.tsv.gz && \
    # Create a taxonomically annotated sequence database
    mmseqs createdb uniprot_sprot_2018_03.fasta.gz uniprot_sprot && \
    mmseqs createtaxdb uniprot_sprot tmp --tax-mapping-file uniprot_sprot_2018_03_mapping.tsv && \
    # Transfer the annotation of the reference protein to our unknown reads
    mmseqs createdb mystery_reads.fasta reads && \
    mmseqs taxonomy reads uniprot_sprot lca_result tmp -s 2 && \
    # Convert this database into a human readable tab separated values file
    mmseqs createtsv reads lca_result lca.tsv && \
    # summarize the data into a single file
    mmseqs taxonomyreport uniprot_sprot lca_result report.txt && \
    # Visualizing taxonomic results
    mmseqs taxonomyreport uniprot_sprot lca_result report.html --report-mode 1 && \
    # retrieve only the reads that belong to a pathogen
    mmseqs filtertaxdb uniprot_sprot lca_result lca_only_pathogen --taxon-list XXX && \
    # a list of all queries that were filtered out
    grep -Pv '\t1$' lca_only_pathogen.index > pathogenic_read_ids && \
    # Convert taxonomic labels back into a FASTA file
    mmseqs createsubdb pathogenic_read_ids reads reads_pathogen && \
    mmseqs convert2fasta reads_pathogen reads_pathogen.fasta

    # the next steps require plass or some other protein assembler
    # plass assemble reads_pathogen.fasta pathogen_assembly.fasta tmp && \
    # mmseqs easy-cluster pathogen_assembly.fasta assembly_clustered tmp
