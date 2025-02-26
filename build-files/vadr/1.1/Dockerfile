# base image
FROM ubuntu:xenial

ENV VADR_VERSION="1.1"\
  VADR_CORONA_MODELS_VERSION="1.1-1" \
  LC_ALL=C \
  VADRINSTALLDIR=/opt/vadr

ENV VADRSCRIPTSDIR=$VADRINSTALLDIR/vadr \
 VADRMODELDIR=$VADRINSTALLDIR/vadr-models \
 VADRINFERNALDIR=$VADRINSTALLDIR/infernal/binaries \
 VADREASELDIR=$VADRINSTALLDIR/infernal/binaries \
 VADRHMMERDIR=$VADRINSTALLDIR/hmmer/binaries \
 VADRBIOEASELDIR=$VADRINSTALLDIR/Bio-Easel \
 VADRSEQUIPDIR=$VADRINSTALLDIR/sequip \
 VADRBLASTDIR=$VADRINSTALLDIR/ncbi-blast/bin

ENV PERL5LIB=$VADRSCRIPTSDIR:$VADRSEQUIPDIR:$VADRBIOEASELDIR/blib/lib:$VADRBIOEASELDIR/blib/arch:$PERL5LIB \
 PATH=$VADRSCRIPTSDIR:$PATH

# metadata - optional, but highly recommended
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version=${VADR_VERSION}
LABEL description="This software does viral annotations"
LABEL website="https://github.com/nawrockie/vadr"
LABEL license="https://github.com/nawrockie/vadr/blob/master/LICENSE"
LABEL maintainer="Anders Goncalves da Silva"
LABEL maintainer.email="andersgs@gmail.com"

# install dependencies via apt-get. Clean up apt garbage 
RUN apt-get update && apt-get install -y \
 wget \
 perl \
 curl \
 unzip \
 build-essential \
 autoconf && \
 apt-get install -y libinline-c-perl liblwp-protocol-https-perl && \
 apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install and/or setup more things. Make /data for use as a working dir
RUN mkdir -p ${VADRINSTALLDIR} && \
 cd ${VADRINSTALLDIR} &&\
 wget https://raw.githubusercontent.com/nawrockie/vadr/release-${VADR_VERSION}/vadr-install.sh &&\
 bash vadr-install.sh linux

# install the latest corona virus models
RUN wget -O vadr-models-corona.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/coronaviridae/${VADR_CORONA_MODELS_VERSION}/vadr-models-corona-${VADR_CORONA_MODELS_VERSION}.tar.gz
RUN tar -xf vadr-models-corona.tar.gz
RUN cp -n /vadr-models-corona-${VADR_CORONA_MODELS_VERSION}/* ${VADRMODELDIR}
RUN rm -rf /vadr-models-corona*

# set working directory
WORKDIR /data

RUN v-annotate.pl -h 
