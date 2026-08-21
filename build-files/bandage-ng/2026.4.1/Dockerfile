ARG BANDAGENG_VER="2026.4.1"

FROM ubuntu:noble AS app
ARG BANDAGENG_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="Bandage-NG"
LABEL software.version="${BANDAGENG_VER}"
LABEL description="A GUI program that allows users to interact with the assembly graphs made by de novo assemblers such as SPAdes, MEGAHIT and others"
LABEL website="https://github.com/asl/BandageNG"
LABEL license="https://github.com/asl/BandageNG/blob/dev/COPYING"
LABEL maintainer="Raheel Ahmed"
LABEL maintainer.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    libopengl0 \
    libgl1 \
    libegl1 \
    imagemagick && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN wget -q https://github.com/asl/BandageNG/releases/download/v${BANDAGENG_VER}/BandageNG-Linux-2aefa98.AppImage && \
    mv BandageNG-Linux-2aefa98.AppImage /opt/BandageNG.AppImage && \
    chmod +x ./BandageNG.AppImage && \
    ./BandageNG.AppImage --appimage-extract && \
    rm ./BandageNG.AppImage

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV LD_LIBRARY_PATH=/opt/squashfs-root/usr/lib:/opt/squashfs-root/usr/lib/x86_64-linux-gnu

RUN ln -s /opt/squashfs-root/AppRun /usr/local/bin/BandageNG

WORKDIR /data

CMD ["BandageNG", "--helpall"]


FROM app AS test
ARG BANDAGENG_VER

WORKDIR /test

# Version and larger help message
RUN BandageNG --version && \
    BandageNG --helpall

RUN echo "Base help message" && \
    BandageNG --help

RUN wget -q https://github.com/asl/BandageNG/archive/refs/tags/v${BANDAGENG_VER}.tar.gz && \
    tar -xzf v${BANDAGENG_VER}.tar.gz && \
    mv BandageNG-${BANDAGENG_VER}/tests /test/bandage_tests && \
    rm v${BANDAGENG_VER}.tar.gz && \
    rm -r BandageNG-${BANDAGENG_VER}

RUN cd bandage_tests && \
    ./bandage_command_line_tests.sh /usr/local/bin/BandageNG

# This should generate an output image nearly identical to bandage_tests/test.png
RUN BandageNG image bandage_tests/inputs/test.gfa output.png

# Columns are filepath, node count, edge count, smallest edge overlap, largest edge overlap, total length, total length no overlaps,
# dead ends, % dead ends, connected components, largest component, total length orphaned nodes, N50, 
# shortest node, lower quartile node, median node, upper quartile node, longest node, median depth, and estimated sequence length
RUN BandageNG info bandage_tests/inputs/test.gfa --tsv