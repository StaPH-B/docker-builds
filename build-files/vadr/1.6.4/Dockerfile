FROM ubuntu:jammy AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ARG VADR_VERSION="1.6.4"

ENV LC_ALL=C \
  VADRINSTALLDIR="/opt/vadr"

ENV VADRSCRIPTSDIR="${VADRINSTALLDIR}/vadr" \
  VADRMINISCRIPTSDIR="${VADRINSTALLDIR}/vadr/miniscripts" \
  VADRMODELDIR="${VADRINSTALLDIR}/vadr-models" \
  VADRINFERNALDIR="${VADRINSTALLDIR}/infernal/binaries" \
  VADREASELDIR="${VADRINSTALLDIR}/infernal/binaries" \
  VADRHMMERDIR="${VADRINSTALLDIR}/infernal/binaries" \
  VADRBIOEASELDIR="${VADRINSTALLDIR}/Bio-Easel" \
  VADRSEQUIPDIR="${VADRINSTALLDIR}/sequip" \
  VADRBLASTDIR="${VADRINSTALLDIR}/ncbi-blast/bin" \
  VADRFASTADIR="${VADRINSTALLDIR}/fasta/bin" \
  VADRMINIMAP2DIR="${VADRINSTALLDIR}/minimap2"

ENV PERL5LIB=${VADRSCRIPTSDIR}:${VADRSEQUIPDIR}:${VADRBIOEASELDIR}/blib/lib:${VADRBIOEASELDIR}/blib/arch:$PERL5LIB \
  PATH=${VADRINSTALLDIR}/vadr:${VADRSCRIPTSDIR}:${VADRMINISCRIPTSDIR}:${VADRINSTALLDIR}/vadr/testfiles:$PATH

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
# use vadr-install.sh script to install VADR into ${VADRINSTALLDIR} (set to /opt/vadr)
# this script grabs files from tagged release and sets things up in /opt/vadr/vadr
# calici models are copied for test stage
# last step is to delete the original source code that is a duplicate (/opt/vadr/vadr-${VADR_VERSION})
RUN mkdir -p ${VADRMODELDIR} && \
  mkdir -p ${VADRINSTALLDIR} && \
  cd ${VADRINSTALLDIR} && \ 
  wget -q https://github.com/ncbi/vadr/archive/refs/tags/vadr-${VADR_VERSION}.tar.gz && \
  mkdir vadr-${VADR_VERSION} && \
  tar -xzf vadr-${VADR_VERSION}.tar.gz -C vadr-${VADR_VERSION} --strip-components 1 && \
  rm vadr-${VADR_VERSION}.tar.gz && \
  bash vadr-${VADR_VERSION}/vadr-install.sh linux && \
  rm -rf vadr-${VADR_VERSION}/ && \
  cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR}/. && \
  rm -rf ${VADRINSTALLDIR}/vadr-models-calici/ && \
  mkdir /data

# set working directory
WORKDIR /data

CMD ["v-annotate.pl", "-h"]

FROM app AS test 

ARG VADR_SARSCOV2_MODELS_VERSION="1.3-2"

RUN v-annotate.pl -h

WORKDIR /

# run included tests
RUN do-install-tests-local.sh

# download SARS-CoV-2 models and try running
RUN wget -O vadr-models-sarscov2.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/${VADR_SARSCOV2_MODELS_VERSION}/vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}.tar.gz && \
  tar -xf vadr-models-sarscov2.tar.gz && \
  cp -nv /vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}/* ${VADRMODELDIR}/.

WORKDIR /test

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
  fasta-trim-terminal-ambigs.pl \
    SRR13957123.consensus.fa \
    --minlen 50 \
    --maxlen 30000 \
    > SRR13957123.consensus.trimmed.fasta && \
  v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc \
    --mkey sarscov2 --lowsim5seq 6 --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
    SRR13957123.consensus.trimmed.fasta \
    SRR13957123-vadr-outdir && \
  ls SRR13957123-vadr-outdir

# lists models in image
RUN ls ${VADRMODELDIR}/*cm