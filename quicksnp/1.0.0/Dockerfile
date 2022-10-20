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
  wget && \
  pip install --no-cache-dir --upgrade pip && \
  pip install --no-cache-dir \
  pandas==1.4.3 \
  numpy==1.22.4 \
  scikit-bio==0.5.7 \
  scipy==1.8

RUN wget https://raw.githubusercontent.com/k-florek/QuickSNP/main/QuickSNP.py -O /bin/QuickSNP.py && \
  chmod +x /bin/QuickSNP.py && \
  mkdir /data && \
  mkdir /test

WORKDIR /data


FROM app as test

RUN mkdir test && \
  cd test && \
  quicksnp_test.sh
