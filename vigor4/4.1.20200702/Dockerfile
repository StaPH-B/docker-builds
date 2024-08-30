FROM ubuntu:jammy as app

ARG VIGOR4_VER='4.1.20200702'
ARG VIGOR4_COMMIT='23852472af871b6c05bd5abf2022d140b9cecd3b'
ARG VIGOR4_DB_COMMIT='390582955049b9ddc989510672fbde90cf3387c7'

LABEL base.image="ubuntu:jammy"
LABEL container.version="1"
LABEL software="VIGOR4"
LABEL software.version="${VIGOR4_VER}"
LABEL description="VIGOR - Viral Genome ORF Reader"
LABEL website="https://github.com/JCVenterInstitute/VIGOR4"
LABEL lisence="https://github.com/JCVenterInstitute/VIGOR4/blob/master/LICENSE.txt"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get -y upgrade && apt-get -y  --no-install-recommends install \
    exonerate \
    maven \
    openjdk-11-jre-headless \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

#get VIGOR4
RUN wget -q https://github.com/JCVenterInstitute/VIGOR4/archive/${VIGOR4_COMMIT}.zip && \
    unzip ${VIGOR4_COMMIT}.zip && \
    mv VIGOR4-${VIGOR4_COMMIT} /VIGOR4 && \
    rm ${VIGOR4_COMMIT}.zip && \
    cd /VIGOR4 && \
    mvn -DskipTests clean package && \
    ls /VIGOR4/target && \
    unzip /VIGOR4/target/vigor-${VIGOR4_VER}.zip

RUN cd VIGOR4 && \
    mkdir tmp && \
    cd tmp && \
    mkdir vigor-temp

#get databases
RUN wget https://github.com/JCVenterInstitute/VIGOR_DB/archive/${VIGOR4_DB_COMMIT}.zip && \
    unzip ${VIGOR4_DB_COMMIT}.zip && \
    rm ${VIGOR4_DB_COMMIT}.zip && \
    mv VIGOR_DB-${VIGOR4_DB_COMMIT} /VIGOR_DB

#set paths for refs, exonerate, and tmp directory in the config file
RUN cd VIGOR4/vigor-${VIGOR4_VER}/config && \
    (echo  "\nreference_database_path=/VIGOR_DB/Reference_DBs/\nexonerate_path=/usr/bin/exonerate\ntemporary_directory=/VIGOR4/tmp/vigor-temp\n" > vigor.ini)

#permissions
RUN chmod 777 -R VIGOR4

#set paths
ENV PATH="/usr/bin/exonerate:/VIGOR_DB/Reference_DBs:/VIGOR4/vigor-${VIGOR4_VER}/bin/:$PATH"\
    LC_ALL=C

CMD vigor4 -h

RUN mkdir /data
WORKDIR /data

FROM app as test

WORKDIR /test

# checking help and version
RUN vigor4 -h && vigor4 --version

# list databases
RUN ls /VIGOR_DB/Reference_DBs

# copy bash script for running
COPY test.sh .

RUN bash test.sh

# using test files
COPY test.fasta .

RUN vigor4 -i test.fasta -o test1 -d /VIGOR_DB/Reference_DBs/entovirus_txid2733257_db 
