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
    libglx-mesa0 \
    libgl1 \
    libopengl0 \
    libegl1 \
    libfontconfig1 \
    libfreetype6 \
    libglib2.0-0 \
    libdbus-1-3 \
    libxcb1 \
    libx11-6 \
    libxcb-cursor0 \
    imagemagick && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/bin

RUN wget -q https://github.com/asl/BandageNG/releases/download/v${BANDAGENG_VER}/BandageNG-Linux-2aefa98.AppImage && \
    mv BandageNG-Linux-2aefa98.AppImage /usr/local/bin/BandageNG.AppImage && \
    chmod +x BandageNG.AppImage && \
    ./BandageNG.AppImage --appimage-extract

ENV LD_LIBRARY_PATH=/usr/local/bin/squashfs-root/usr/lib
ENV QT_PLUGIN_PATH=/usr/local/bin/squashfs-root/usr/plugins
ENV OPENSSL_ia32cap=~0x20000000
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV QT_LOGGING_RULES="*.debug=false"

RUN ln -s /usr/local/bin/squashfs-root/usr/bin/BandageNG /usr/local/bin/BandageNG


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

