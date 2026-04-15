FROM ubuntu:noble AS app
ARG BANDAGENG_VER="2026.4.1"

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
    ca-certificates && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

RUN wget -q https://github.com/asl/BandageNG/releases/download/v${BANDAGENG_VER}/BandageNG-Linux-2aefa98.AppImage && \
    mv BandageNG-Linux-2aefa98.AppImage /usr/local/bin/BandageNG.AppImage && \
    chmod +x BandageNG.AppImage && \
    ./BandageNG.AppImage --appimage-extract


# RUN squashfs-root/AppRun --help



