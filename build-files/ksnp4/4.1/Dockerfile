FROM ubuntu:jammy as app

ARG KSNPVER=4.1

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="kSNP"
LABEL software.version="${KSNPVER}"
LABEL description="K-mer-based phylogenetic inference"
LABEL website="https://sourceforge.net/projects/ksnp/"
LABEL license="https://github.com/kissake/kSNP${KSNPVER}/blob/%40/THE%20BSD%20OPENSOURCE%20LICENSE.pdf"
LABEL maintainer="Jeremiah Nisbet"
LABEL maintainer.email="ksnp-dev@kissake.net"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget \
    ca-certificates \
    unzip \
    python3 \
    libgomp1 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget -O kSNP.zip https://sourceforge.net/projects/ksnp/files/kSNP${KSNPVER}%20Linux%20package.zip && \
    unzip -j kSNP.zip "kSNP${KSNPVER} Linux package/kSNP${KSNPVER}pkg/*" -d "/usr/local/bin/" &&\
    rm kSNP.zip

ENV LC_ALL=C

CMD [kSNP4]

WORKDIR /data

## Test ##
FROM app as test

COPY kSNP_test.sh RunExamples.sh ./

RUN bash ./kSNP_test.sh

