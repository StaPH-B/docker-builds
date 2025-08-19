FROM mambaorg/micromamba:2.3.1-ubuntu22.04 AS app

ARG SEROBA_VERSION="2.0.5"

ARG PYSAM_VERSION="0.15.0"
ARG PYMUMMER_VERSION="0.10.3"
ARG PYYAML_VERSION="5.4.1"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.1-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="SeroBA"
LABEL software.version="${SEROBA_VERSION}"
LABEL description="k-mer based Pipeline to identify the Serotype from Illumina NGS reads"
LABEL website="https://github.com/GlobalPneumoSeq/seroba"
LABEL license="https://github.com/GlobalPneumoSeq/seroba/blob/master/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

RUN micromamba install --name base -c conda-forge -c bioconda pysam=${PYSAM_VERSION} pymummer=${PYMUMMER_VERSION} pyyaml=${PYYAML_VERSION} requests kmc ariba && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

RUN wget https://github.com/GlobalPneumoSeq/seroba/archive/refs/tags/v${SEROBA_VERSION}.tar.gz &&\
    tar -xvf v${SEROBA_VERSION}.tar.gz && rm v${SEROBA_VERSION}.tar.gz &&\
    mv seroba-${SEROBA_VERSION}/ seroba/ && cd seroba &&\
    python3 setup.py install &&\
    seroba createDBs database/ 71

CMD [ "seroba", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test 

RUN seroba version

RUN cd /seroba && python3 setup.py test

