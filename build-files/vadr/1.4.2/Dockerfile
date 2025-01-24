FROM ubuntu:xenial as app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.4.2" \
  VADR_SARSCOV2_MODELS_VERSION="1.3-2" \
  VADR_MPXV_MODELS_VERSION="1.4.2-1" \
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
LABEL dockerfile.version="3"
LABEL software="VADR"
LABEL software.version=${VADR_VERSION}
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
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
 autoconf \
 libinline-c-perl \
 liblwp-protocol-https-perl \
 zip \
 unzip && \
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

# install the latest sarscov2 and mpxv models 
# copy calici model files into VADRMODELDIR to allow VADR tests to pass completely
# cleanup duplicate copies of model files
RUN wget -O vadr-models-sarscov2.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/${VADR_SARSCOV2_MODELS_VERSION}/vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}.tar.gz && \
 wget -O vadr-models-mpxv.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/mpxv/${VADR_MPXV_MODELS_VERSION}/vadr-models-mpxv-${VADR_MPXV_MODELS_VERSION}.tar.gz && \
 tar -xf vadr-models-sarscov2.tar.gz && \
 tar -xf vadr-models-mpxv.tar.gz && \
 mkdir -vp ${VADRMODELDIR} && \
 cp -nv /vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}/* ${VADRMODELDIR} && \
 cp -nv /vadr-models-mpxv-${VADR_MPXV_MODELS_VERSION}/* ${VADRMODELDIR} && \
 rm -rf /vadr-models-sarscov2* && \
 rm -rf /vadr-models-mpxv* && \
 cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR} && \
 rm -rf ${VADRINSTALLDIR}/vadr-models-calici/ 

# Virus model files other than sarscov2 will need to be made available to vadr either in
# the $VADRMODELDIR or another path can be specified using the 'v-annotate.pl -mdir' option.
# These files will need to be mounted into the container at runtime, e.g. 'docker run -v' option.

# set working directory
WORKDIR /data

FROM app as test 

# download B.1.1.7 genome from Utah
ADD https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa /test-data/SRR13957123.consensus.fa

# print help options (which prints version at top)
# run test script included w VADR
# test terminal N trimming script
# run v-annotate.pl on trimmed B.1.1.7 genome
RUN v-annotate.pl -h && \
 /opt/vadr/vadr/testfiles/do-install-tests-local.sh && \ 
 /opt/vadr/vadr/miniscripts/fasta-trim-terminal-ambigs.pl \
        /test-data/SRR13957123.consensus.fa \
        --minlen 50 \
        --maxlen 30000 \
        > /test-data/SRR13957123.consensus.trimmed.fasta && \
 v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc \
       --mkey sarscov2 --lowsim5seq 6 --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
       "/test-data/SRR13957123.consensus.trimmed.fasta" \
       "SRR13957123-vadr-outdir" && \
  ls SRR13957123-vadr-outdir

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

# download assembly for a MPXV from  (link here)
# run VADR trimming script and v-annotate.pl
# link to GenBank accession: https://www.ncbi.nlm.nih.gov/nuccore/OP022171
ARG GENBANK_ACCESSION="OP022171.1"
RUN datasets download virus genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
 unzip ${GENBANK_ACCESSION}.zip && rm ${GENBANK_ACCESSION}.zip && \
 mv -v ncbi_dataset/data/genomic.fna ncbi_dataset/data/${GENBANK_ACCESSION}.genomic.fna && \
 fasta-trim-terminal-ambigs.pl /data/ncbi_dataset/data/${GENBANK_ACCESSION}.genomic.fna \
    --minlen 50 \
    --maxlen 210000 \
    >/data/${GENBANK_ACCESSION}.trimmed.fasta && \
v-annotate.pl --split --cpu 2 \
    --glsearch -s -r \
    --nomisc \
    --mkey mpxv \
    --r_lowsimok \
    --r_lowsimxd 100 \
    --r_lowsimxl 2000 \
    --alt_pass discontn,dupregin \
    /data/${GENBANK_ACCESSION}.trimmed.fasta \
    ${GENBANK_ACCESSION}-mpxv-vadr-test-output