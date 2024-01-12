FROM python:3.9.17-slim as app

# List all software versions are ARGs near the top of the dockerfile
# 'ARG' sets environment variables during the build stage
# ARG variables are ONLY available during image build, they do not persist in the final image
ARG ACI_VER="1.2.20231229"

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="ACI"
LABEL software.version="${ACI_VER}"
LABEL description="Determines amplicon coverage"
LABEL website="https://github.com/erinyoung/ACI"
LABEL license="https://github.com/erinyoung/ACI/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    ca-certificates \
    wget && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# aci was taken on pip, but not conda
RUN pip install --no-cache amplicon_coverage_inspector==${ACI_VER}

ENV PATH="$PATH" \
    LC_ALL=C

# 'CMD' instructions set a default command when the container is run. This is typically 'tool --help.'
CMD [ "aci", "--help" ]

WORKDIR /data

FROM app as test

WORKDIR /test

RUN aci --help && aci --version

RUN wget -q https://github.com/StaPH-B/docker-builds/raw/master/tests/SARS-CoV-2/SRR13957123.primertrim.sorted.bam   && \
    wget -q https://raw.githubusercontent.com/artic-network/artic-ncov2019/master/primer_schemes/nCoV-2019/V3/nCoV-2019.insert.bed && \
    aci -d nCoV-2019.insert.bed -b SRR13957123.primertrim.sorted.bam