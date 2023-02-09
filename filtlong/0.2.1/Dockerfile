ARG FILTLONG_VER="0.2.1"
# setting as global variable for persistence across all build layers 

FROM ubuntu:jammy as app
USER root
#
# re-instantiating for the app build layer if using ARG as a global variable above
ARG FILTLONG_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="3"
LABEL software="Filtlong"
LABEL software.version="${FILTLONG_VER}"
LABEL description="Filters long reads by quality and length. Can use Illumina reads as reference."
LABEL website="https://github.com/rrwick/Filtlong"
LABEL license="https://github.com/rrwick/Filtlong/blob/master/LICENSE"
LABEL website="https://github.com/StaPH-B/docker-builds"
LABEL license="https://github.com/StaPH-B/docker-builds/blob/master/LICENSE"

LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Thomas A. Christensen II"
LABEL maintainer2.email="25492070+MillironX@users.noreply.github.com"
LABEL maintainer3="Stephen Beckstrom-Sternberg"
LABEL maintainer3.email="stephen.beckstrom-sternberg@azdhs.gov"

# Install dependencies and cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 g++ \
 zlib1g-dev \
 make \
 python3 \
 pigz \
 less \
 bc  \
 gzip && \
 update-alternatives --install /usr/bin/python python /usr/bin/python3 10 && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH"

# set workdir to /opt for installing Filtlong; set to /data at the end for testing
WORKDIR /opt

RUN echo "installing filtlong" && echo
RUN wget \
https://github.com/rrwick/Filtlong/archive/v${FILTLONG_VER}.tar.gz \
--no-check-certificate && \
tar -xzf v${FILTLONG_VER}.tar.gz && \
rm -rf v${FILTLONG_VER}.tar.gz
RUN echo "Change to lowercase name: " && \
 mv Filtlong-${FILTLONG_VER} filtlong-${FILTLONG_VER}

WORKDIR /opt/filtlong-${FILTLONG_VER}
RUN make
RUN chmod +x bin/filtlong 

ENV PATH="$PATH:/opt/filtlong-$FILTLONG_VER/bin:\
/opt/filtlong-$FILTLONG_VER/scripts:\
/opt/filtlong-$FILTLONG_VER/test" LC_ALL=C 

RUN echo "Symlink executable into /usr/local/bin"
RUN ln -s /opt/filtlong-$FILTLONG_VER/bin/filtlong /usr/local/bin/

# set workdir to default for building; set to /data at the end
WORKDIR /data

# new base for testing
FROM app as test
ARG FILTLONG_VER
RUN echo "Running Test layer"
ENV PATH="$PATH:/data"

RUN echo "Download a pair of long-reads sequences from European Nucleotide Archive (ENA)" && \
 echo "    SRR19008456_1.fastq and SRR19008456_2.fastq"
RUN wget --no-verbose "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/056/SRR19008456/SRR19008456_1.fastq.gz"
RUN wget --no-verbose "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR190/056/SRR19008456/SRR19008456_2.fastq.gz"

RUN echo "Running read_info_histograms.sh"
RUN sed -i 's/\$hist/\$hist --dot "*"/g' /opt/filtlong-${FILTLONG_VER}/scripts/read_info_histograms.sh
RUN /opt/filtlong-${FILTLONG_VER}/scripts/read_info_histograms.sh /data/*fastq.gz 
RUN echo "Done with histograms"

RUN echo "Show help file for installed unittest"
RUN cd /opt/filtlong-${FILTLONG_VER}
RUN python3 -m unittest -h

RUN echo "Run unittest without args" && \
 python3 -m unittest && \
 echo "Done with unittest"

RUN echo && echo "Show filtlong help file:  " && echo && \
 filtlong -h  && echo

RUN echo "Run filtlong with options on a pair of long reads in /data dir: " && \
 filtlong --min_length 250 --min_mean_q 40 SRR19008456_1.fastq.gz|gzip  > SRR19008456_1_filt.fastq.gz && \
 filtlong --min_length 250 --min_mean_q 40 SRR19008456_2.fastq.gz|gzip  > SRR19008456_2_filt.fastq.gz

RUN echo "Files successfully filtered: " && \
 ls -lh SRR19008456_1.fastq.gz && echo " ---> " && ls -lh SRR19008456_1_filt.fastq.gz && \
 ls -lh SRR19008456_2.fastq.gz && echo " ---> " && ls -lh SRR19008456_2_filt.fastq.gz
RUN echo && echo "Successful installation of filtlong-${FILTLONG_VER}"
