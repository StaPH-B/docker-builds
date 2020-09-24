FROM ubuntu:bionic AS builder

LABEL base.image="ubuntu:bionic"
LABEL version="1"
LABEL software="MetaPhlAn3.0"
LABEL software.version="3.0"
LABEL description="microbial composition of metagenomes"
LABEL website="http://cab.spbu.ru/files/release3.13.0/manual.html"
LABEL maintainer="Tara Gallagher"
LABEL maintainer.email="tgallagher@utah.gov"

# install python (>3.6) and other dependencies
RUN apt-get update && apt-get install -y software-properties-common && \
	add-apt-repository ppa:deadsnakes/ppa&& \
	apt-get update && apt-get install -y \
        gcc \
	wget \
	python3.7 \
	python3.7-dev \
	python3-distutils \
	python3-setuptools \
        python3-pip \
	unzip && \ 
	python3.7 -m pip install pip --force-reinstall && \
	python3.7 -m pip install numpy Cython six --force-reinstall && \
	ln -s /usr/bin/python3.7 /usr/bin/python 


# bowtie 2 dependency 
RUN mkdir /usr/bin/bowtie2 && \
	cd /usr/bin/bowtie2 && \  
	 wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.3.1/bowtie2-2.3.3.1-linux-x86_64.zip/download && \
	unzip download && \
	rm download 

ENV PATH="$PATH:/usr/bin/bowtie2/bowtie2-2.3.3.1-linux-x86_64"


# install metaphlan 3
RUN python3.7 -m pip install metaphlan==3.0.3

# download metaphlan database
RUN metaphlan --install && \ 
	mkdir /data 

# build onto first stage
FROM ubuntu:bionic

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/bin/bowtie2/ /usr/bin/bowtie2/
COPY --from=builder /usr/bin/python3.7 /usr/bin/python3.7
COPY --from=builder /usr/lib/python3.7 /usr/lib/python3.7
COPY --from=builder /usr/lib/x86_64-linux-gnu/libexpat.so /usr/lib/x86_64-linux-gnu/libexpat.so
COPY --from=builder /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
COPY --from=builder /usr/local/lib/python3.7/dist-packages/ /usr/local/lib/python3.7/dist-packages/
COPY --from=builder /usr/lib/python3/dist-packages/* /usr/lib/python3.7/dist-packages/

WORKDIR /data

ENV PATH="$PATH:/usr/bin/bowtie2/bowtie2-2.3.3.1-linux-x86_64"
