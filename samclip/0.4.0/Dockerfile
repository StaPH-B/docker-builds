ARG SAMCLIP_VER="0.4.0"

FROM ubuntu:jammy as app

ARG SAMCLIP_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="samclip"
LABEL software.version="${SAMCLIP_VER}"
LABEL description="Samclip: filter SAM file for soft and hard clipped alignments"
LABEL website="https://github.com/tseemann/samclip"
LABEL license="https://github.com/tseemann/samclip/blob/master/LICENSE"
LABEL maintainer="Dhatri Badri"
LABEL maintainer.email="dhatrib@umich.edu"

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    software-properties-common \
    perl && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install samclip
RUN wget https://raw.githubusercontent.com/tseemann/samclip/master/samclip && \
    chmod +x samclip && \
    mkdir /data

ENV PATH="${PATH}:/samclip-${SAMCLIP_VER}/" \
    LC_ALL=C

CMD [ "./samclip", "--help" ]

WORKDIR /data

FROM app as test

ARG SAMCLIP_VER

# Copy the samclip executable from the app stage to the test stage
COPY --from=app /samclip /samclip

RUN /samclip --help && \
 /samclip --version

WORKDIR /test

# Run test using samclip executable
RUN wget https://raw.githubusercontent.com/tseemann/samclip/master/test.fna && \
    wget https://raw.githubusercontent.com/tseemann/samclip/master/test.sam && \
    wget https://raw.githubusercontent.com/tseemann/samclip/master/test.fna.fai && \
    /samclip --ref test.fna < test.sam > out.sam  
