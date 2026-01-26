ARG VADR_VERSION=1.7

FROM staphb/vadr:$VADR_VERSION AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_MEV_MODELS_VER="1.02"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/ncbi/vadr"
LABEL license="https://github.com/ncbi/vadr/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# download MeV VADR models; copy model files into VADRMODELDIR
RUN wget https://github.com/greninger-lab/vadr-models-mev/archive/refs/tags/v${VADR_MEV_MODELS_VER}.tar.gz && \
    tar -xf v${VADR_MEV_MODELS_VER}.tar.gz && \
    rm -v v${VADR_MEV_MODELS_VER}.tar.gz && \
    cp -nvr vadr-models-mev-${VADR_MEV_MODELS_VER}/mev/* ${VADRMODELDIR} && \
    rm -rfv vadr-models-mev-${VADR_MEV_MODELS_VER}

# set working directory
WORKDIR /data

CMD ["v-annotate.pl", "-h"]

FROM app AS test 

# testing that executable is in PATH
RUN v-annotate.pl -h && fasta-trim-terminal-ambigs.pl -h || echo "prints to stderr for some reason"

WORKDIR /test

# downloads a test MeV/measles genome, run through VADR using MeV models
RUN wget https://raw.githubusercontent.com/greninger-lab/vadr-models-mev/refs/heads/main/mev/mev.fa && \
    fasta-trim-terminal-ambigs.pl mev.fa \
        --minlen 50 \
        > mev.trimmed.fasta && \
    v-annotate.pl --split \
        -r \
        -xnocomp \
        -mkey mev \
        --indefclass 0.01 \
        mev.trimmed.fasta \
        mev-vadr-test-output
