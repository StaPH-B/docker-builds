FROM ubuntu:jammy AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.6.4" \
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

# set working directory
WORKDIR /data

# set default command
CMD ["v-annotate.pl", "-h"]

FROM app AS test 

ARG VADR_SARSCOV2_MODELS_VERSION="1.3-2"

# testing that executable is in PATH
RUN v-annotate.pl -h
RUN fasta-trim-terminal-ambigs.pl -h || echo "prints to stderr for some reason"

# running vadr tests
RUN /opt/vadr/vadr/testfiles/do-install-tests-local.sh

# downloading some test files
WORKDIR /

# install the latest sarscov2 models 
RUN wget -O vadr-models-sarscov2.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/${VADR_SARSCOV2_MODELS_VERSION}/vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}.tar.gz && \
  tar -xf vadr-models-sarscov2.tar.gz && \
  cp -nv /vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}/* ${VADRMODELDIR} && \
  rm -rf /vadr-models-sarscov2*

WORKDIR /test

# print help options (which prints version at top)
# download B.1.1.7 genome from Utah
# run test script included w VADR
# test terminal N trimming script
# run v-annotate.pl on trimmed B.1.1.7 genome
RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \ 
  fasta-trim-terminal-ambigs.pl \
    SRR13957123.consensus.fa \
    --minlen 50 \
    --maxlen 30000 \
    > SRR13957123.consensus.trimmed.fasta && \
  v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc \
    --mkey sarscov2 --lowsim5seq 6 --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
    "SRR13957123.consensus.trimmed.fasta" \
    "SRR13957123-vadr-outdir" && \
  ls SRR13957123-vadr-outdir
