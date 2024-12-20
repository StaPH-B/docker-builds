FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="GNU Parallel"
LABEL software.version="20200722"
LABEL description="Small basic container with parallel"
LABEL website="https://www.gnu.org/software/parallel"
LABEL license="https://gnu.org/licenses/gpl.html"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

# install dependencies
RUN apt-get update && apt-get install -y \
                     parallel \
                     make \
                     curl \
                     cpanminus \
                     libxml-parser-perl \
                     libperlio-utf8-strict-perl \
                     libmoose-perl \
                     libgraph-perl && \
                     rm -rf /var/lib/apt/lists/* && apt-get autoclean

WORKDIR /data
# set perl locale settings
ENV LC_ALL=C
