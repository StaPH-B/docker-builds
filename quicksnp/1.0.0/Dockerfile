FROM ubuntu:focal as app

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="QuickSNP"
LABEL software.version="1.0.0"
LABEL description="This software quickly builds a Neighbor Joining tree using only a SNP distance matrix."
LABEL website="https://github.com/StaPH-B/docker-builds/QuickSNP"
LABEL license="https://github.com/StaPH-B/docker-builds/QuickSNP/LICENSE"
LABEL maintainer="CJ Jossart"
LABEL maintainer.email="christopher.jossart@slh.wisc.edu"

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  git

RUN git clone https://github.com/k-florek/QuickSNP.git && \
  cd QuickSNP && \
  pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir -r requirements.txt && \
  mkdir /data

ENV PATH="/QuickSNP:${PATH}"

WORKDIR /data

FROM app as test

COPY quicksnp_test.sh .

COPY test_data ./test_data

RUN bash quicksnp_test.sh
