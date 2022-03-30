# base image
FROM ubuntu:xenial

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.2.1" \
  VADR_SARSCOV2_MODELS_VERSION="1.2-2" \
  LC_ALL=C \
  VADRINSTALLDIR=/opt/vadr

ENV VADRSCRIPTSDIR=$VADRINSTALLDIR/vadr \
 VADRMINISCRIPTSDIR=$VADRINSTALLDIR/vadr/miniscripts \
 VADRMODELDIR=$VADRINSTALLDIR/vadr-models \
 VADRINFERNALDIR=$VADRINSTALLDIR/infernal/binaries \
 VADREASELDIR=$VADRINSTALLDIR/infernal/binaries \
 VADRHMMERDIR=$VADRINSTALLDIR/hmmer/binaries \
 VADRBIOEASELDIR=$VADRINSTALLDIR/Bio-Easel \
 VADRSEQUIPDIR=$VADRINSTALLDIR/sequip \
 VADRBLASTDIR=$VADRINSTALLDIR/ncbi-blast/bin \
 VADRFASTADIR=$VADRINSTALLDIR/fasta/bin

ENV PERL5LIB=$VADRSCRIPTSDIR:$VADRSEQUIPDIR:$VADRBIOEASELDIR/blib/lib:$VADRBIOEASELDIR/blib/arch:$PERL5LIB \
 PATH=$VADRSCRIPTSDIR:$VADRMINISCRIPTSDIR:$PATH

# metadata - optional, but highly recommended
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version=${VADR_VERSION}
LABEL description="This software does viral annotations"
LABEL website="https://github.com/ncbi/vadr"
LABEL license="https://github.com/ncbi/vadr/blob/master/LICENSE"
LABEL maintainer1="Anders Goncalves da Silva"
LABEL maintainer1.email="andersgs@gmail.com"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="curtis.kapsak@theiagen.com"

# install dependencies via apt-get. Clean up apt garbage 
RUN apt-get update && apt-get install -y \
 wget \
 perl \
 curl \
 unzip \
 build-essential \
 autoconf && \
 apt-get install -y libinline-c-perl liblwp-protocol-https-perl && \
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

# install the latest sarscov2 models 
# copy calici models into VADRMODELDIR to allow VADR tests to pass completely
# cleanup duplicate copies of model files
RUN wget -O vadr-models-sarscov2.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/${VADR_SARSCOV2_MODELS_VERSION}/vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}.tar.gz && \
 tar -xf vadr-models-sarscov2.tar.gz && \
 mkdir -vp ${VADRMODELDIR} && \
 cp -nv /vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}/* ${VADRMODELDIR} && \
 rm -rf /vadr-models-sarscov2* && \
 cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR} && \
 rm -rf ${VADRINSTALLDIR}/vadr-models-calici/

# Virus model files other than sarscov2 will need to be made available to vadr either in
# the $VADRMODELDIR or another path can be specified using the 'v-annotate.pl -mdir' option.
# These files will need to be mounted into the container at runtime, e.g. 'docker run -v' option.

# set working directory
WORKDIR /data
