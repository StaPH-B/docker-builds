FROM ubuntu:focal as app

ARG QUICKSNP_VER="1.0.1"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="QuickSNP"
LABEL software.version="${QUICKSNP_VER}"
LABEL description="This software quickly builds a Neighbor Joining tree using only a SNP distance matrix."
LABEL website="https://github.com/k-florek/QuickSNP"
LABEL license="https://github.com/k-florek/QuickSNP/blob/main/LICENSE"
LABEL maintainer="CJ Jossart"
LABEL maintainer.email="christopher.jossart@slh.wisc.edu"

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  wget

RUN wget https://github.com/k-florek/QuickSNP/archive/refs/tags/${QUICKSNP_VER}.tar.gz && \
  tar -zxvf ${QUICKSNP_VER}.tar.gz && \
  rm ${QUICKSNP_VER}.tar.gz && \
  cd QuickSNP-${QUICKSNP_VER} && \
  pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt && \
  mkdir /data

ENV PATH="/QuickSNP-${QUICKSNP_VER}:${PATH}"

WORKDIR /data

FROM app as test

COPY quicksnp_test.sh .

COPY test_data ./test_data

RUN bash quicksnp_test.sh
