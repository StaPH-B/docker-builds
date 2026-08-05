ARG VADR_VERSION=1.7

FROM staphb/vadr:${VADR_VERSION}-slim AS app

# for easy upgrade later
ENV VADR_VERSION=${VADR_VERSION} \
    VADR_HAV_MODELS_COMMIT="b1f29b2"
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

# install git. Can remove this in the future if we switch to downloading a release tarball instead of cloning the repo and checking out a specific commit
RUN apt-get update && apt-get install -y --no-install-recommends \
git \
&& apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download latest available commit (as of 2026-08-04) of HAV VADR model files and move files into $VADRMODELDIR
# if another release is made in the future, we should change the below code to download the release tarball instead of cloning the repo and checking out a specific commit
RUN git clone https://github.com/greninger-lab/vadr-models-hav.git && \
cd vadr-models-hav && \
git checkout ${VADR_HAV_MODELS_COMMIT} && \
mv -v hav/* ${VADRMODELDIR} && \
ls -l ${VADRMODELDIR}

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
