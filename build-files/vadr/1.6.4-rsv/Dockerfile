FROM ubuntu:jammy AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.6.4" \
    VADR_RSV_MODELS_VER="1.5-2"\
    LC_ALL=C \
    VADRINSTALLDIR=/opt/vadr

ENV VADRSCRIPTSDIR=$VADRINSTALLDIR/vadr \
    VADRMINISCRIPTSDIR=$VADRINSTALLDIR/vadr/miniscripts \
    VADRMODELDIR=$VADRINSTALLDIR/vadr-models \
    VADRINFERNALDIR=$VADRINSTALLDIR/infernal/binaries \
    VADREASELDIR=$VADRINSTALLDIR/infernal/binaries \
    VADRHMMERDIR=$VADRINSTALLDIR/infernal/binaries \
    VADRBIOEASELDIR=$VADRINSTALLDIR/Bio-Easel \
    VADRSEQUIPDIR=$VADRINSTALLDIR/sequip \
    VADRBLASTDIR=$VADRINSTALLDIR/ncbi-blast/bin \
    VADRFASTADIR=$VADRINSTALLDIR/fasta/bin \
    VADRMINIMAP2DIR=$VADRINSTALLDIR/minimap2

ENV PERL5LIB=$VADRSCRIPTSDIR:$VADRSEQUIPDIR:$VADRBIOEASELDIR/blib/lib:$VADRBIOEASELDIR/blib/arch:$PERL5LIB \
    PATH=$VADRSCRIPTSDIR:$VADRMINISCRIPTSDIR:$VADRINFERNALDIR:$VADRBIOEASELDIR:$VADRSEQUIPDIR:$VADRBLASTDIR:$VADRFASTADIR:$VADRMINIMAP2DIR:$PATH

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/ncbi/vadr"
LABEL license="https://github.com/ncbi/vadr/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies via apt-get. Clean up apt garbage 
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    perl \
    curl \
    unzip \
    build-essential \
    autoconf \
    libinline-c-perl \
    liblwp-protocol-https-perl \
    zip \
    unzip \
    procps \
    zlib1g-dev && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# create relevant directories
# download vadr source code
# decompress souce code
# remove tarfile
# use vadr-install.sh script to install VADR into $VADRINSTALLDIR (set to /opt/vadr)
# remove directory that's no longer needed
# install perl module Mozilla::CA required in VADR v1.6.4
RUN mkdir -p ${VADRINSTALLDIR}/vadr-${VADR_VERSION} /data ${VADRMODELDIR} && \
    cd ${VADRINSTALLDIR} && \ 
    wget -q https://github.com/ncbi/vadr/archive/refs/tags/vadr-${VADR_VERSION}.tar.gz && \
    tar -xzf vadr-${VADR_VERSION}.tar.gz -C vadr-${VADR_VERSION} --strip-components 1 && \
    rm vadr-${VADR_VERSION}.tar.gz && \
    bash vadr-${VADR_VERSION}/vadr-install.sh linux && \
    rm -rf vadr-${VADR_VERSION}/ && \
    echo "DELETING VADR MODELS NOW..." && \
    rm -rf ${VADRMODELDIR}/* && \
    rm -rf ${VADRINSTALLDIR}/vadr-models-calici && \
    rm -rf ${VADRINSTALLDIR}/vadr-models-flavi && \
    echo "DONE DELETING VADR MODELS" && \
    yes | cpan install Mozilla::CA

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
