ARG CLUSTALO_VER="1.2.4"

FROM ubuntu:xenial AS app

ARG CLUSTALO_VER

WORKDIR /

# 'LABEL' instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="ClustalO"
LABEL software.version="${CLUSTALO_VER}"
LABEL description="Multiple sequence alignment program."
LABEL website="http://www.clustal.org/omega/"
LABEL license="https://www.ebi.ac.uk/licencing/"
LABEL documentation="http://www.clustal.org/omega/"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="Kelsey.florek@slh.wisc.edu"

# Execute the build
RUN apt-get update && apt-get install -y wget

RUN wget http://www.clustal.org/omega/clustalo-${CLUSTALO_VER}-Ubuntu-x86_64 && mv clustalo-${CLUSTALO_VER}-Ubuntu-x86_64 /usr/bin/clustalo && chmod +x /usr/bin/clustalo 

CMD [ "clustalo", "--help" ]

WORKDIR /data

FROM app AS test

RUN clustalo --help \
    clustalo --version

WORKDIR /test

RUN wget -q http://www.clustal.org/omega/homfam-20110613-25.tar.gz && tar -xvf homfam-20110613-25.tar.gz \
    && mkdir test_outs \
    && clustalo --in cytb_test-only.vie -o test_outs/out-a \
    && clustalo --in cytb_test-only.vie --profile1 cytb_ref.vie -o test_outs/out-b
