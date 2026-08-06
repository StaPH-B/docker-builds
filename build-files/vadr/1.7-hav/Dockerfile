ARG VADR_VERSION=1.7

FROM staphb/vadr:${VADR_VERSION}-slim AS app

# for easy upgrade later
ENV VADR_VERSION=${VADR_VERSION} \
    VADR_HAV_MODELS_COMMIT="b1f29b27bc77acf4b0ab8acc61dac7355ffc912e"
    #VADR_HAV_MODELS_VER="1.0"

LABEL base.image="staphb/vadr:${VADR_VERSION}"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/NLM-DIR/vadr"
LABEL license="https://github.com/NLM-DIR/vadr/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

WORKDIR /

# download latest available commit (as of 2026-08-06) of HAV VADR model files and move files into $VADRMODELDIR
RUN wget https://github.com/greninger-lab/vadr-models-hav/archive/${VADR_HAV_MODELS_COMMIT}.zip && \
    unzip ${VADR_HAV_MODELS_COMMIT}.zip && \
    cd vadr-models-hav-${VADR_HAV_MODELS_COMMIT} && \
    ls && \
    mv -v hav/* ${VADRMODELDIR} && \
    ls -l ${VADRMODELDIR} && \
    rm -rf /vadr-models-hav-${VADR_HAV_MODELS_COMMIT} /${VADR_HAV_MODELS_COMMIT}.zip

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

# download a test HAV genome, run through VADR using HAV models
RUN echo "testing HAV functionality..." && \
    wget https://raw.githubusercontent.com/StaPH-B/docker-builds/refs/heads/master/build-files/vadr/1.6.3-hav/hav.fasta && \
    fasta-trim-terminal-ambigs.pl hav.fasta \
        --minlen 50 \
        --maxlen 10500 \
        > hav.trimmed.fasta && \
    v-annotate.pl --split \
        -r \
        -xnocomp \
        -mkey hav \
        hav.trimmed.fasta \
        hav-vadr-test-output
