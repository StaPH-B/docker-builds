ARG PANDAS_VER="2.2.3"

FROM ubuntu:jammy as app

ARG PANDAS_VER

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="pandas"
LABEL software.version="${PANDAS_VER}"
LABEL description="data analysis and manipulation tool for python"
LABEL website="https://github.com/pandas-dev/pandas"
LABEL license="https://github.com/pandas-dev/pandas?tab=BSD-3-Clause-1-ov-file#readme"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# 'RUN' executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pandas==${PANDAS_VER}

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "pip", "list" ]

# 'WORKDIR' sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
FROM app as test

# set working directory so that all test inputs & outputs are kept in /test
WORKDIR /test

RUN pip list | grep pandas

COPY test_pandas.py .