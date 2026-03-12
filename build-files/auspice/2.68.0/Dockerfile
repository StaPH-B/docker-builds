FROM node:20.19.0
ARG AUSPICE_VERSION=2.68.0

LABEL base.image="node:20.19.0-slim"
LABEL version="1"
LABEL software="auspice"
LABEL software.version="v2.68.0"
LABEL description="Web app for viewing genomic information."
LABEL website="https://github.com/nextstrain/auspice"
LABEL license="https://github.com/nextstrain/auspice/blob/master/LICENSE.txt"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"

#get curl so we can download auspice
RUN apt-get update && apt-get install -y curl

#set ourself as user "node" to install the global auspice package
USER node
WORKDIR /home/node/

#get auspice release
RUN curl -L https://github.com/nextstrain/auspice/archive/v${AUSPICE_VERSION}.tar.gz --output v${AUSPICE_VERSION}.tar.gz &&\
  tar -xzf v${AUSPICE_VERSION}.tar.gz &&\
  mv auspice-${AUSPICE_VERSION} /home/node/auspice

#set up global install to be available for non-root user "node"
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

RUN cd /home/node/auspice &&\
  npm install &&\
  npm install --global /home/node/auspice &&\
  auspice build

#expose the auspice port to all connections
ENV HOST=0.0.0.0
EXPOSE 4000

WORKDIR /data
