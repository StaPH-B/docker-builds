# base image
FROM ubuntu:xenial

ENV VADR_VERSION="1.2" \
  VADR_SARSCOV2_MODELS_VERSION="1.2-2" \
  LC_ALL=C \
  VADRINSTALLDIR=/opt/vadr

ENV VADRSCRIPTSDIR=$VADRINSTALLDIR/vadr \
 VADRMODELDIR=$VADRINSTALLDIR/vadr-models \
 VADRINFERNALDIR=$VADRINSTALLDIR/infernal/binaries \
 VADREASELDIR=$VADRINSTALLDIR/infernal/binaries \
 VADRHMMERDIR=$VADRINSTALLDIR/hmmer/binaries \
 VADRBIOEASELDIR=$VADRINSTALLDIR/Bio-Easel \
 VADRSEQUIPDIR=$VADRINSTALLDIR/sequip \
 VADRBLASTDIR=$VADRINSTALLDIR/ncbi-blast/bin \
 VADRFASTADIR=$VADRINSTALLDIR/fasta/bin

ENV PERL5LIB=$VADRSCRIPTSDIR:$VADRSEQUIPDIR:$VADRBIOEASELDIR/blib/lib:$VADRBIOEASELDIR/blib/arch:$PERL5LIB \
 PATH=$VADRSCRIPTSDIR:$PATH

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

# install and/or setup more things. Make /data for use as a working dir
RUN mkdir -p ${VADRINSTALLDIR} && \
 cd ${VADRINSTALLDIR} && \
 wget https://raw.githubusercontent.com/ncbi/vadr/release-${VADR_VERSION}/vadr-install.sh && \
 bash vadr-install.sh linux && \
 mkdir /data

# install the latest sarscov2 models 
# copy calici models into VADRMODELDIR to allow tests to pass completely
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
