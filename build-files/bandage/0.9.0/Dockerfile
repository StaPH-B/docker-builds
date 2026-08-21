FROM ubuntu:noble AS app

ARG BANDAGE_VERSION="0.9.0"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="bandage"
LABEL software.version="${BANDAGE_VERSION}"
LABEL description="Bandage is a program for visualising de novo assembly graphs."
LABEL website="https://rrwick.github.io/Bandage/"
LABEL license="https://github.com/rrwick/Bandage/blob/main/COPYING"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    imagemagick \
    bandage=${BANDAGE_VERSION}* &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN mkdir /tmp/runtime-root &&\
    chmod 0700 /tmp/runtime-root

ENV QT_QPA_PLATFORM=offscreen \
    XDG_RUNTIME_DIR=/tmp/runtime-root \
    LC_ALL=C.UTF-8

CMD [ "Bandage", "--help" ]

WORKDIR /data

FROM app AS test

## Test ##
WORKDIR /test

RUN Bandage --help && \
    Bandage --version

RUN apt-get update && apt-get install -y git &&\
    git clone https://github.com/rrwick/Bandage.git &&\
    cd Bandage/tests &&\
    sed -i 's|bandagepath="../../build-Bandage-Desktop_Qt_5_6_0_clang_64bit-Release/Bandage.app/Contents/MacOS/Bandage"|bandagepath=/usr/bin/Bandage|' bandage_command_line_tests.sh &&\
    ./bandage_command_line_tests.sh



