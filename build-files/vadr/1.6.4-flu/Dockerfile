FROM ubuntu:jammy AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.6.4" \
    VADR_FLU_MODELS_VER="1.6.3-2"\
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
# copy calici files that are used in testing
RUN mkdir -p ${VADRINSTALLDIR}/vadr-${VADR_VERSION} /data ${VADRMODELDIR} && \
    cd ${VADRINSTALLDIR} && \ 
    wget -q https://github.com/ncbi/vadr/archive/refs/tags/vadr-${VADR_VERSION}.tar.gz && \
    tar -xzf vadr-${VADR_VERSION}.tar.gz -C vadr-${VADR_VERSION} --strip-components 1 && \
    rm vadr-${VADR_VERSION}.tar.gz && \
    bash vadr-${VADR_VERSION}/vadr-install.sh linux && \
    rm -rf vadr-${VADR_VERSION}/ && \
    cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR}

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
RUN v-annotate.pl -h
RUN fasta-trim-terminal-ambigs.pl -h || echo "prints to stderr for some reason"

# running vadr tests
RUN /opt/vadr/vadr/testfiles/do-install-tests-local.sh

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
