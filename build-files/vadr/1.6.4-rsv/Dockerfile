FROM ubuntu:jammy AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.6.3" \
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
    PATH=$VADRSCRIPTSDIR:$VADRMINISCRIPTSDIR:$PATH

# metadata - optional, but highly recommended
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/ncbi/vadr"
LABEL license="https://github.com/ncbi/vadr/blob/master/LICENSE"
LABEL maintainer="Anders Goncalves da Silva"
LABEL maintainer.email="andersgs@gmail.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"
LABEL maintainer3="Ines Mendes"
LABEL maintainer3.email="ines.mendes@theiagen.com"

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

# install VADR
# download entire VADR source code from GitHub release
# use vadr-install.sh script to install VADR into $VADRINSTALLDIR (set to /opt/vadr)
# this script grabs files from tagged release and sets things up in /opt/vadr/vadr
# last step is to delete the original source code that is a duplicate (/opt/vadr/vadr-$VADR_VERSION)
RUN mkdir -p ${VADRINSTALLDIR} && \
    cd ${VADRINSTALLDIR} && \ 
    wget https://github.com/ncbi/vadr/archive/refs/tags/vadr-${VADR_VERSION}.tar.gz && \
    mkdir vadr-${VADR_VERSION} && tar -xzf vadr-${VADR_VERSION}.tar.gz -C vadr-${VADR_VERSION} --strip-components 1 && \
    rm vadr-${VADR_VERSION}.tar.gz && \
    bash vadr-${VADR_VERSION}/vadr-install.sh linux && \
    rm -rf vadr-${VADR_VERSION}/ && \
    mkdir /data

# copy calici model files into VADRMODELDIR to allow VADR tests to pass completely
# cleanup duplicate copies of model files
RUN mkdir -vp ${VADRMODELDIR} && \
    cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR} && \
    rm -rf ${VADRINSTALLDIR}/vadr-models-calici/ 

# download RSV VADR models; copy model files into VADRMODELDIR
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/rsv/${VADR_RSV_MODELS_VER}/vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    tar -xf /vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    rm -v /vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    cp -nvr /vadr-models-rsv-${VADR_RSV_MODELS_VER}/* ${VADRMODELDIR} && \
    rm -rfv /vadr-models-rsv-${VADR_RSV_MODELS_VER}

# set working directory
WORKDIR /data

CMD ["v-annotate.pl", "-h"]

FROM app as test 

# print help options (which prints version at top)
# run test script included w VADR
# test terminal N trimming script
RUN v-annotate.pl -h && \
    /opt/vadr/vadr/testfiles/do-install-tests-local.sh 

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
    chmod +x datasets && \
    mv -v datasets /usr/local/bin

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
