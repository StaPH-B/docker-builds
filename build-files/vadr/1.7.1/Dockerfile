FROM ubuntu:noble AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION="1.7.1" \
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
VADRMINIMAP2DIR=$VADRINSTALLDIR/minimap2 \
R2DT_DIR=$VADRINSTALLDIR/R2DT

ENV PERL5LIB=$VADRSCRIPTSDIR:$VADRSEQUIPDIR:$VADRBIOEASELDIR/blib/lib:$VADRBIOEASELDIR/blib/arch:$PERL5LIB \
PATH=$VADRSCRIPTSDIR:$VADRMINISCRIPTSDIR:$VADRINFERNALDIR:$VADRBIOEASELDIR:$VADRSEQUIPDIR:$VADRBLASTDIR:$VADRFASTADIR:$VADRMINIMAP2DIR:$PATH

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/NLM-DIR/vadr"
LABEL license="https://github.com/NLM-DIR/vadr/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

# install dependencies via apt-get. Clean up apt garbage 
# git, python3, and python3-venv required for R2DT to install & function properly
# R2DT was added in v1.7.1 of VADR for drawing secondary structure diagrams of classified sequences https://github.com/NLM-DIR/vadr/blob/master/RELEASE-NOTES.md#vadr-171-release-september-2026
RUN apt-get update && apt-get install -y --no-install-recommends \
wget \
ca-certificates \
perl \
python3 \
python3-venv \
git \
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
# sed to edit vadr-install.sh to pin up-to-date model versions (as of September 2026). Basically replicate changes made in VADR v1.7.2: https://github.com/NLM-DIR/vadr/pull/100/changes
# use vadr-install.sh script to install VADR into $VADRINSTALLDIR (set to /opt/vadr)
# remove directory that's no longer needed
# install perl module Mozilla::CA required in VADR v1.6.4
RUN mkdir -p ${VADRINSTALLDIR}/vadr-${VADR_VERSION} /data ${VADRMODELDIR} && \
cd ${VADRINSTALLDIR} && \ 
wget -q https://github.com/NLM-DIR/vadr/archive/refs/tags/vadr-${VADR_VERSION}.tar.gz && \
tar -xzf vadr-${VADR_VERSION}.tar.gz -C vadr-${VADR_VERSION} --strip-components 1 && \
rm vadr-${VADR_VERSION}.tar.gz && \
sed -i 's|CALICIVERSION="1.2-1"|CALICIVERSION="1.7-2"|' vadr-${VADR_VERSION}/vadr-install.sh && \
sed -i 's|SARSCOV2VERSION="1.3-2"|SARSCOV2VERSION="1.6.3-1"|' vadr-${VADR_VERSION}/vadr-install.sh && \
sed -i 's|FLUVERSION="1.6.3"|FLUVERSION="1.7-2"|' vadr-${VADR_VERSION}/vadr-install.sh && \
sed -i 's|RSVVERSION="1.5-2"|RSVVERSION="1.7-1"|' vadr-${VADR_VERSION}/vadr-install.sh && \
bash vadr-${VADR_VERSION}/vadr-install.sh linux && \
rm -rf vadr-${VADR_VERSION}/ && \
yes | cpan install Mozilla::CA

# set working directory
WORKDIR /data

# set default command
CMD ["v-annotate.pl", "-h"]

FROM app AS test

# testing that executable is in PATH
# v-build.pl -h to ensure required perl modules are available (See issue #1393)
RUN v-annotate.pl -h &&  \
  v-build.pl -h && \
  fasta-trim-terminal-ambigs.pl -h || echo "prints to stderr for some reason"

# copy calici model files into VADRMODELDIR to allow VADR tests to pass completely
# run vadr tests
RUN cp -nv ${VADRINSTALLDIR}/vadr-models-calici/* ${VADRMODELDIR} && \
rm -rf ${VADRINSTALLDIR}/vadr-models-calici/ && \
/opt/vadr/vadr/testfiles/do-install-tests-local.sh

WORKDIR /test

# download sars-cov-2 (B.1.1.7 pango lineage) genome from Utah
# run test script included w/ VADR
# test terminal N trimming script
# run v-annotate.pl on trimmed B.1.1.7 genome
RUN wget https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \ 
fasta-trim-terminal-ambigs.pl \
  SRR13957123.consensus.fa \
  --minlen 50 \
  --maxlen 30000 \
  > SRR13957123.consensus.trimmed.fasta && \
v-annotate.pl --noseqnamemax --glsearch -s -r --nomisc --mkey sarscov2 \
  --mdir /opt/vadr/vadr-models-sarscov2 --lowsim5seq 6 --lowsim3seq 6 --alt_fail lowscore,insertnn,deletinn \
  "SRR13957123.consensus.trimmed.fasta" \
  "SRR13957123-vadr-outdir" && \
ls SRR13957123-vadr-outdir
