FROM ubuntu:14.04

MAINTAINER Dan Fornika <dfornika@gmail.com>

RUN apt-get update \
	&& apt-get install -y --no-install-recommends ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

ENV JULIA_PATH /usr/local/julia
ENV JULIA_VERSION 0.6.1

RUN mkdir $JULIA_PATH \
	&& apt-get update && apt-get install -y curl \
	&& curl -sSL "https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz" -o julia.tar.gz \
	&& curl -sSL "https://julialang-s3.julialang.org/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz.asc" -o julia.tar.gz.asc \
	&& export GNUPGHOME="$(mktemp -d)" \
# http://julialang.org/juliareleases.asc
# Julia (Binary signing key) <buildbot@julialang.org>
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 3673DF529D9049477F76B37566E3C7DC03D6E495 \
	&& gpg --batch --verify julia.tar.gz.asc julia.tar.gz \
	&& rm -r "$GNUPGHOME" julia.tar.gz.asc \
	&& tar -xzf julia.tar.gz -C $JULIA_PATH --strip-components 1 \
	&& rm -rf /var/lib/apt/lists/* julia.tar.gz*

ENV PATH $JULIA_PATH/bin:$PATH

RUN apt-get update \
        && apt-get install -y --no-install-recommends \
        build-essential \
	hdf5-tools \
	libxml2

ENV JULIA_PKGDIR $JULIA_PATH/share/julia/site

RUN mkdir /tools

ENV MENTALIST_VERSION 0.2.1

WORKDIR /tmp
RUN curl -sSL -o MentaLiST-${MENTALIST_VERSION}.tar.gz https://github.com/WGS-TB/MentaLiST/archive/v${MENTALIST_VERSION}.tar.gz
RUN tar -xvzf MentaLiST-${MENTALIST_VERSION}.tar.gz
WORKDIR /tools
RUN cp -r /tmp/MentaLiST-${MENTALIST_VERSION} mentalist

ENV HOME /tools/mentalist
RUN mkdir $HOME/.OpenGene

RUN julia -e 'Pkg.init()'
RUN julia -e 'Pkg.add("Bio")'
RUN julia -e 'Pkg.add("OpenGene")'
RUN julia -e 'Pkg.add("Logging")'
RUN julia -e 'Pkg.add("ArgParse")'
RUN julia -e 'Pkg.add("Lumberjack")'
RUN julia -e 'Pkg.add("FastaIO")'
RUN julia -e 'Pkg.add("JLD")'
RUN julia -e 'Pkg.add("DataStructures")'
