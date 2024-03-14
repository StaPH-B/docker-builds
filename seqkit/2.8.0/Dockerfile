# FROM defines the base docker image. This command has to come first in the file
# The 'as' keyword lets you name the folowing stage. We use `app` for the production image
FROM ubuntu:jammy as app

# ARG sets environment variables during the build stage
ARG SEQKIT_VER="2.8.0"

# LABEL instructions tag the image with metadata that might be important to the user
# Optional, but highly recommended
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="SeqKit"
LABEL software.version=${SEQKIT_VER}
LABEL description="SeqKit - a cross-platform and ultrafast toolkit for FASTA/Q file manipulation"
LABEL website="https://github.com/shenwei356/seqkit"
LABEL license="https://github.com/shenwei356/seqkit/blob/master/LICENSE"
LABEL maintainer="Henry Kunerth"
LABEL maintainer.email="henrykunerth@gmail.com"
LABEL maintainer2="Erin Young"
LABEL maintainer2.email="eriny@utah.gov"

# Install dependences (update as needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
	wget \
	ca-certificates \
	procps \
	unzip && \
	apt-get autoclean && rm -rf /var/lib/apt/lists/*

# download SEQKIT and organize directories
RUN wget -q https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VER}/seqkit_linux_amd64.tar.gz && \
	tar -xzf seqkit_linux_amd64.tar.gz && \
	mv seqkit /usr/local/bin/. && \
	rm seqkit_linux_amd64.tar.gz && \
	mkdir /data

# singularity compatibility
ENV LC_ALL=C

CMD seqkit --help

# WORKDIR sets working directory
WORKDIR /data

# A second FROM insruction creates a new stage
# We use `test` for the test image
FROM app as test

WORKDIR /test

RUN seqkit --help

#download test .fasta and check that SEQKIT can run to generate stats
RUN wget -q https://raw.githubusercontent.com/StaPH-B/docker-builds/master/tests/SARS-CoV-2/SRR13957123.consensus.fa && \
	seqkit stat *
