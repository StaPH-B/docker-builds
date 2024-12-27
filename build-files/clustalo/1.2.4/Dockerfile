FROM ubuntu:xenial

# metadata
LABEL base.image="ubuntu:xenial"
LABEL container.version="1"
LABEL software="ClustalO"
LABEL software.version="1.2.4"
LABEL description="Multiple sequence alignment program."
LABEL website="http://www.clustal.org/omega/"
LABEL license=""
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="Kelsey.florek@slh.wisc.edu"

RUN apt-get update && apt-get install -y wget

RUN wget http://www.clustal.org/omega/clustalo-1.2.4-Ubuntu-x86_64 && mv clustalo-1.2.4-Ubuntu-x86_64 /usr/bin/clustalo && chmod +x /usr/bin/clustalo 

WORKDIR /data
