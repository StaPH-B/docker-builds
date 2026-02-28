ARG VADR_VERSION=1.7

FROM staphb/vadr:$VADR_VERSION AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION=${VADR_VERSION} \
    VADR_SARSCOV2_MODELS_VERSION="1.3-2"

LABEL base.image="staphb/vadr:${VADR_VERSION}"
LABEL dockerfile.version="1"
LABEL software="VADR"
LABEL software.version="${VADR_VERSION}"
LABEL description="Classification and annotation of viral sequences based on RefSeq annotation"
LABEL website="https://github.com/ncbi/vadr"
LABEL license="https://github.com/ncbi/vadr/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"

WORKDIR /

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
#NOTE: These tests require the flavi and calici models to be present, which are not included in this image. These tests are however run in the docker build process for the `build-files/vadr/1.6.4-2505/Dockerfile` image.
#RUN /opt/vadr/vadr/testfiles/do-install-tests-local.sh

WORKDIR /test

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
