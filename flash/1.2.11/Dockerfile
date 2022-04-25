ARG FLASH_VER="1.2.11"

FROM ubuntu:focal as builder
ARG FLASH_VER

RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    zlib1g-dev

RUN wget http://ccb.jhu.edu/software/FLASH/FLASH-$FLASH_VER.tar.gz && \
 tar -xzf FLASH-$FLASH_VER.tar.gz && \
 rm FLASH-$FLASH_VER.tar.gz

WORKDIR /FLASH-$FLASH_VER
RUN make

FROM ubuntu:focal as app
ARG FLASH_VER

# Labels need to go in the production stage
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2"
LABEL software="FLASH"
LABEL software.version=$FLASH_VER
LABEL description="FLASH (Fast Length Adjustment of Short Reads): merges overlapping paired-end reads"
LABEL website="http://ccb.jhu.edu/software/FLASH"
LABEL license="https://github.com/ebiggers/flash/blob/master/COPYING"
LABEL maintainer="Sarah Nadeau"
LABEL maintainer.email="sarah.nadeau@bsse.ethz.ch"

# Copy only executable into production stage to reduce image size
COPY --from=builder FLASH-$FLASH_VER/flash /usr/local/bin/flash

WORKDIR /data

FROM app as test
ARG FLASH_VER

# Install test dependency
RUN apt-get update && apt-get install -y wget

# Run test script
COPY test_flash.sh .
RUN bash test_flash.sh $FLASH_VER
