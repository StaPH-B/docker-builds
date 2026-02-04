ARG VADR_VERSION=1.7

FROM staphb/vadr:$VADR_VERSION AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION=${VADR_VERSION} \
    VADR_FLU_MODELS_VER="1.6.3-2"

LABEL base.image="staphb/vadr:${VADR_VERSION}"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/ncbi/vadr"
LABEL license="https://github.com/ncbi/vadr/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

WORKDIR /

# download flu VADR models; copy model files into VADRMODELDIR
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/flu/${VADR_FLU_MODELS_VER}/vadr-models-flu-${VADR_FLU_MODELS_VER}.tar.gz && \
    tar -xf /vadr-models-flu-${VADR_FLU_MODELS_VER}.tar.gz && \
    rm -v /vadr-models-flu-${VADR_FLU_MODELS_VER}.tar.gz && \
    cp -nvr /vadr-models-flu-${VADR_FLU_MODELS_VER}/* ${VADRMODELDIR} && \
    rm -rfv /vadr-models-flu-${VADR_FLU_MODELS_VER}

# set working directory
WORKDIR /data

CMD ["v-annotate.pl", "-h"]

FROM app AS test 

# testing that executable is in PATH
# v-build.pl -h to ensure required perl modules are available (See issue #1393)
RUN v-annotate.pl -h &&  \
v-build.pl -h && \
fasta-trim-terminal-ambigs.pl -h || echo "prints to stderr for some reason"

# running vadr tests
#NOTE: These tests require the flavi and calici models to be present, which are not included in this image. These tests are however run in the docker build process for the `build-files/vadr/1.6.4-2505/Dockerfile` image.
#RUN /opt/vadr/vadr/testfiles/do-install-tests-local.sh

WORKDIR /test

# download some test flu genomes, run through VADR using flu models
# example commands taken from VADR flu guide: https://github.com/ncbi/vadr/wiki/Influenza-annotation
RUN echo "testing flu functionality..." && \
    wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/flu/pretrim.flu.3.fa && \
    fasta-trim-terminal-ambigs.pl pretrim.flu.3.fa \
        --minlen 60 \
        > flu.3.fa && \
    v-annotate.pl --split \
        -r \
        --atgonly \
        --xnocomp \
        --nomisc \
        --alt_fail extrant5,extrant3 \
        --mkey flu \
        flu.3.fa \
        flu-vadr-test-output
