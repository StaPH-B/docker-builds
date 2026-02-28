ARG VADR_VERSION=1.7

FROM staphb/vadr:$VADR_VERSION AS app

# for easy upgrade later. LC_ALL set for singularity compatibility
ENV VADR_VERSION=${VADR_VERSION} \
    VADR_MPXV_MODELS_VERSION="1.4.2-1"

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

# download mpxv models 
RUN wget -O vadr-models-mpxv.tar.gz https://ftp.ncbi.nlm.nih.gov/pub/nawrocki/vadr-models/mpxv/${VADR_MPXV_MODELS_VERSION}/vadr-models-mpxv-${VADR_MPXV_MODELS_VERSION}.tar.gz && \
    tar -xf vadr-models-mpxv.tar.gz && \
    cp -nv /vadr-models-mpxv-${VADR_MPXV_MODELS_VERSION}/* ${VADRMODELDIR} && \
    rm -rf /vadr-models-mpxv* 

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
