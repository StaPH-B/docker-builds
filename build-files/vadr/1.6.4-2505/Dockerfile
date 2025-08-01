FROM ubuntu:jammy AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.6.4" \
  VADR_FLU_MODELS_VER="1.6.3-2"\
  VADR_HAV_MODELS_VER="1.0.0" \
  VADR_MPXV_MODELS_VERSION="1.4.2-1" \
  VADR_RSV_MODELS_VER="1.5-2"\
  VADR_SARSCOV2_MODELS_VERSION="1.3-2" \
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
# install perl module Mozilla::CA required in VADR v1.6.4
RUN mkdir -p ${VADRINSTALLDIR}/vadr-${VADR_VERSION} /data ${VADRMODELDIR} && \
  cd ${VADRINSTALLDIR} && \ 
  wget -q https://github.com/ncbi/vadr/archive/refs/tags/vadr-${VADR_VERSION}.tar.gz && \
  tar -xzf vadr-${VADR_VERSION}.tar.gz -C vadr-${VADR_VERSION} --strip-components 1 && \
  rm vadr-${VADR_VERSION}.tar.gz && \
  bash vadr-${VADR_VERSION}/vadr-install.sh linux && \
  rm -rf vadr-${VADR_VERSION}/ && \
  cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR} && \
  yes | cpan install Mozilla::CA

# download flu VADR models; copy model files into VADRMODELDIR
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/flu/${VADR_FLU_MODELS_VER}/vadr-models-flu-${VADR_FLU_MODELS_VER}.tar.gz && \
    tar -xf /vadr-models-flu-${VADR_FLU_MODELS_VER}.tar.gz && \
    rm -v /vadr-models-flu-${VADR_FLU_MODELS_VER}.tar.gz && \
    cp -nvr /vadr-models-flu-${VADR_FLU_MODELS_VER}/* ${VADRMODELDIR} && \
    rm -rfv /vadr-models-flu-${VADR_FLU_MODELS_VER}

# download release of HAV VADR model files and move files into $VADRMODELDIR; clean up extra copies (original downloaded files)
RUN wget https://github.com/theiagen/VADR_models/archive/refs/tags/v${VADR_HAV_MODELS_VER}.tar.gz && \
    tar -xf v${VADR_HAV_MODELS_VER}.tar.gz && \
    rm -v v${VADR_HAV_MODELS_VER}.tar.gz && \ 
    cp -nvr /VADR_models-${VADR_HAV_MODELS_VER}/hav/* ${VADRMODELDIR} && \
    rm -rf /VADR_models-${VADR_HAV_MODELS_VER}

# download mpxv models 
RUN wget -O vadr-models-mpxv.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/mpxv/${VADR_MPXV_MODELS_VERSION}/vadr-models-mpxv-${VADR_MPXV_MODELS_VERSION}.tar.gz && \
  tar -xf vadr-models-mpxv.tar.gz && \
  cp -nv /vadr-models-mpxv-${VADR_MPXV_MODELS_VERSION}/* ${VADRMODELDIR} && \
  rm -rf /vadr-models-mpxv* 

# download RSV VADR models; copy model files into VADRMODELDIR
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/rsv/${VADR_RSV_MODELS_VER}/vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    tar -xf /vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    rm -v /vadr-models-rsv-${VADR_RSV_MODELS_VER}.tar.gz && \
    cp -nvr /vadr-models-rsv-${VADR_RSV_MODELS_VER}/* ${VADRMODELDIR} && \
    rm -rfv /vadr-models-rsv-${VADR_RSV_MODELS_VER}

# download the sarscov2 model
RUN wget -O vadr-models-sarscov2.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/sarscov2/${VADR_SARSCOV2_MODELS_VERSION}/vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}.tar.gz && \
  tar -xf vadr-models-sarscov2.tar.gz && \
  cp -nv /vadr-models-sarscov2-${VADR_SARSCOV2_MODELS_VERSION}/* ${VADRMODELDIR} && \
  rm -rf /vadr-models-sarscov2* 

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
RUN /opt/vadr/vadr/testfiles/do-install-tests-local.sh

WORKDIR /test-flu

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

WORKDIR /test-hav

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
        -mkey hav.vadr \
        hav.trimmed.fasta \
        hav-vadr-test-output

WORKDIR /test-mpxv

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
    chmod +x datasets && \
    mv -v datasets /usr/local/bin

# download assembly for a MPXV from the UK
# run VADR trimming script and v-annotate.pl
# link to GenBank accession: https://www.ncbi.nlm.nih.gov/nuccore/OP022171
ARG GENBANK_ACCESSION="OP022171.1"
RUN datasets download virus genome accession ${GENBANK_ACCESSION} --filename ${GENBANK_ACCESSION}.zip && \
    unzip ${GENBANK_ACCESSION}.zip && rm ${GENBANK_ACCESSION}.zip && \
    mv -v ncbi_dataset/data/genomic.fna ${GENBANK_ACCESSION}.genomic.fna && \
    fasta-trim-terminal-ambigs.pl ${GENBANK_ACCESSION}.genomic.fna \
        --minlen 50 \
        --maxlen 210000 \
        > ${GENBANK_ACCESSION}.trimmed.fasta && \
    v-annotate.pl --split --cpu 2 \
        --glsearch -s -r \
        --nomisc \
        --mkey mpxv \
        --r_lowsimok \
        --r_lowsimxd 100 \
        --r_lowsimxl 2000 \
        --alt_pass discontn,dupregin \
        --minimap2 \
        --s_overhang 150 \
        ${GENBANK_ACCESSION}.trimmed.fasta \
        ${GENBANK_ACCESSION}-mpxv-vadr-test-output

WORKDIR /test-rsv

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

WORKDIR /test-sarscov2

# download B.1.1.7 genome from Utah
# run fasta-trim-terminal-ambigs
# run v-annotate.pl
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
