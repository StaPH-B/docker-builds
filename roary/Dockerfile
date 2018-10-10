FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="Roary"
LABEL software.version="3.6.0"
LABEL description="Rapid large-scale prokaryotic pan genome analysis"
LABEL website="https://github.com/sanger-pathogens/Roary"
LABEL license="https://github.com/sanger-pathogens/Roary/blob/master/GPL-LICENSE"

# Maintainer
MAINTAINER Curtis Kapsak <curtis.kapsak@state.co.us>

# install dependencies
RUN apt-get update && apt-get install -y roary
