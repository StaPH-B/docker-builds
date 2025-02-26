FROM ubuntu:bionic AS builder_metaphlan

# multstage build
# labels associated with final docker image are further down
# label the intermediate image so we can delete later 
LABEL stage=builder_metaphlan

# install python (>3.6) and other dependencies
# R necessary if user wants to run unifrac function in metaphlan

RUN apt-get update && apt-get install -y software-properties-common && \
	add-apt-repository ppa:deadsnakes/ppa && \
	apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
        gcc \
	wget \
	python3.7 \
	python3.7-dev \
	python3-distutils \
	python3-setuptools \
        python3-pip \
	unzip \
	r-base=3.4.4-1ubuntu1 && \ 
	python3.7 -m pip install pip --force-reinstall && \
	python3.7 -m pip install numpy Cython six --force-reinstall && \
	ln -s /usr/bin/python3.7 /usr/bin/python 

# bowtie 2 dependency 
RUN mkdir /usr/bin/bowtie2 && \
	cd /usr/bin/bowtie2 && \  
	 wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.3.1/bowtie2-2.3.3.1-linux-x86_64.zip/download && \
	unzip download && \
	rm download 

ENV PATH="$PATH:/usr/bin/bowtie2/bowtie2-2.3.3.1-linux-x86_64" \
	LC_ALL=C

# install metaphlan 3
RUN python3.7 -m pip install metaphlan==3.0.3

# download metaphlan database
RUN metaphlan --install && \ 
	mkdir /data 

# build onto first stage
# this will make the final docker image ~0.5 GB smaller 
# after the build completes, recommend deleting the intermediate image generated from builder stage
# can do this with the flag label=stage=filter:
# docker image ls --filter "label=stage=builder_metaphlan"
# docker image prune --filter "label=stage=builder_metaphlan"

FROM ubuntu:bionic

# labels for final image
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="1"
LABEL software="MetaPhlAn3.0"
LABEL software.version="3.0.3"
LABEL description="microbial composition of metagenomes"
LABEL website="https://github.com/biobakery/MetaPhlAn/tree/3.0"
LABEL maintainer="Tara Gallagher"
LABEL maintainer.email="tgallagher@utah.gov"

# copy over necessary bin and packages 

COPY --from=builder_metaphlan /usr/local/bin /usr/local/bin
COPY --from=builder_metaphlan /usr/bin/bowtie2/ /usr/bin/bowtie2/
COPY --from=builder_metaphlan /usr/bin/python3.7 /usr/bin/python3.7
COPY --from=builder_metaphlan /usr/lib/python3.7 /usr/lib/python3.7
COPY --from=builder_metaphlan /usr/lib/x86_64-linux-gnu/libexpat.so /usr/lib/x86_64-linux-gnu/libexpat.so
COPY --from=builder_metaphlan /lib/x86_64-linux-gnu/ /lib/x86_64-linux-gnu/
COPY --from=builder_metaphlan /usr/local/lib/python3.7/dist-packages/ /usr/local/lib/python3.7/dist-packages/
COPY --from=builder_metaphlan /usr/lib/python3/dist-packages/* /usr/lib/python3.7/dist-packages/
COPY --from=builder_metaphlan /usr/bin/R /usr/bin/R
COPY --from=builder_metaphlan /usr/bin/Rscript /usr/bin/Rscript
COPY --from=builder_metaphlan /usr/lib/R /usr/lib/R
COPY --from=builder_metaphlan /usr/local/lib/R /usr/local/lib/R
COPY --from=builder_metaphlan /etc/R /etc/R
COPY --from=builder_metaphlan /usr/lib/libR.so /usr/lib/libR.so

ENV PATH="$PATH:/usr/bin/bowtie2/bowtie2-2.3.3.1-linux-x86_64" \ 
	LC_ALL=C

WORKDIR /data

# link to python, soft link doesn't get copied from intermed stage
RUN  ln -s /usr/bin/python3.7 /usr/bin/python 
