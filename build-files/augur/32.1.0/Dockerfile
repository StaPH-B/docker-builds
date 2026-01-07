FROM python:3.11-slim AS app

ARG AUGUR_VER="32.1.0"
ARG SEQKIT_VER="2.12.0"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="python:3.11-slim"
LABEL dockerfile.version="1"
LABEL software="augur"
LABEL software.version=${AUGUR_VER}
LABEL description="Augur is the bioinformatics toolkit we use to track evolution from sequence and serological data.The output of augur is a series of JSONs that can be used to visualize your results using Auspice."
LABEL website="https://github.com/nextstrain/augur"
LABEL license="https://github.com/nextstrain/augur/blob/master/LICENSE.txt"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    ca-certificates \
    wget \
    mafft \
    iqtree \
    raxml \
    fasttree  \
    vcftools && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install seqkit
RUN wget -q https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VER}/seqkit_linux_amd64.tar.gz && \
	tar -xzf seqkit_linux_amd64.tar.gz && \
	mv seqkit /usr/local/bin/. && \
	rm seqkit_linux_amd64.tar.gz

# install augur
RUN wget -q https://github.com/nextstrain/augur/archive/refs/tags/${AUGUR_VER}.tar.gz && \
    tar -xzf ${AUGUR_VER}.tar.gz && \
    pip install ${AUGUR_VER}.tar.gz --no-cache-dir && \
    rm -v ${AUGUR_VER}.tar.gz

# augur tree calls iqtree 
RUN ln -s /usr/bin/iqtree2 /usr/bin/iqtree

CMD [ "augur", "--help" ]

WORKDIR /data

FROM app AS test

RUN augur --help

WORKDIR /test

RUN apt-get update && apt-get install -y --no-install-recommends git

RUN git clone https://github.com/nextstrain/zika-tutorial && \
    cd zika-tutorial && \
    mkdir results && \
    augur index \
        --sequences data/sequences.fasta \
        --output results/sequence_index.tsv && \
    augur filter \
        --sequences data/sequences.fasta \
        --sequence-index results/sequence_index.tsv \
        --metadata data/metadata.tsv \
        --exclude config/dropped_strains.txt \
        --output-sequences results/filtered.fasta \
        --group-by country year month \
        --sequences-per-group 20 \
        --min-date 2012 && \
    augur align \
        --sequences results/filtered.fasta \
        --reference-sequence config/zika_outgroup.gb \
        --output results/aligned.fasta \
        --fill-gaps && \
    augur tree \
        --alignment results/aligned.fasta \
        --output results/tree_raw.nwk && \
    augur refine \
        --tree results/tree_raw.nwk \
        --alignment results/aligned.fasta \
        --metadata data/metadata.tsv \
        --output-tree results/tree.nwk \
        --output-node-data results/branch_lengths.json \
        --timetree \
        --coalescent opt \
        --date-confidence \
        --date-inference marginal \
        --clock-filter-iqd 4 && \
    augur traits \
        --tree results/tree.nwk \
        --metadata data/metadata.tsv \
        --output-node-data results/traits.json \
        --columns region country \
        --confidence && \
    augur ancestral \
        --tree results/tree.nwk \
        --alignment results/aligned.fasta \
        --output-node-data results/nt_muts.json \
        --inference joint && \
    augur translate \
        --tree results/tree.nwk \
        --ancestral-sequences results/nt_muts.json \
        --reference-sequence config/zika_outgroup.gb \
        --output-node-data results/aa_muts.json && \
    augur export v2 \
        --tree results/tree.nwk \
        --metadata data/metadata.tsv \
        --node-data results/branch_lengths.json \
                    results/traits.json \
                    results/nt_muts.json \
                    results/aa_muts.json \
        --colors config/colors.tsv \
        --lat-longs config/lat_longs.tsv \
        --auspice-config config/auspice_config.json \
        --output auspice/zika.json && \
    head auspice/zika.json

RUN pip list
