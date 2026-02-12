ARG VADR_VERSION=1.7

FROM staphb/vadr:$VADR_VERSION AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION=${VADR_VERSION} \
    VADR_RSV_MODELS_VER="1.5-2"

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

# download RSV VADR models; copy model files into VADRMODELDIR
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/rsv/${VADR_RSV_MODELS_VER}/vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    tar -xf /vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    rm -v /vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    cp -nvr /vadr-models-rsv-${VADR_RSV_MODELS_VER}/* ${VADRMODELDIR} && \
    rm -rfv /vadr-models-rsv-${VADR_RSV_MODELS_VER}

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

### COMMENTING OUT RSV TEST BELOW SINCE THIS TEST CAN CONSUME UPWARDS OF 30GB RAM ###
### it runs fine when you have that much RAM available, but not in GHActions runners that are limited to 7GB RAM ###

# download a test RSV genome, run through VADR using RSV models
# example commands taken from VADR RSV guide: https://github.com/ncbi/vadr/wiki/RSV-annotation
# RUN echo "testing RSV functionality..." && \
#  wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/rsv/rsv.r10.fa && \
# fasta-trim-terminal-ambigs.pl rsv.r10.fa \
#     --minlen 50 \
#     --maxlen 15500 \
#     >/data/rsv.r10.trimmed.fasta && \
# v-annotate.pl --split \
#     -r \
#     -xnocomp \
#     -mkey rsv \
#     /data/rsv.r10.trimmed.fasta \
#     rsv-vadr-test-output
