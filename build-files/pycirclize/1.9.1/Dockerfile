FROM python:3.9.17-slim AS app

ARG PYCIRCLIZE_VER="1.9.1"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="pyCirclize"
LABEL software.version="${PYCIRCLIZE_VER}"
LABEL description="Circular visualization in Python"
LABEL website="https://github.com/moshi4/pyCirclize"
LABEL license="https://github.com/moshi4/pyCirclize/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache pycirclize==${PYCIRCLIZE_VER}

ENV PATH=$PATH \
    LC_ALL=C

CMD ["pip", "show", "pycirclize"]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN pip show pycirclize

RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/pycirclize/1.5.0/tests/example1.py && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/pycirclize/1.5.0/tests/example2.py && \
    wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/build-files/pycirclize/1.5.0/tests/example3.py

RUN python example1.py && ls example01.png && \
    python example2.py && ls example02.png && \
    python example3.py && ls example03.png
