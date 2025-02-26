FROM ubuntu:focal

LABEL base.image="focal"
LABEL container.version="1"
LABEL software="VIGOR4"
LABEL software.version="4.1.20190131"
LABEL description="VIGOR - Viral Genome ORF Reader"
LABEL website="https://github.com/JCVenterInstitute/VIGOR4"
LABEL lisence="https://github.com/JCVenterInstitute/VIGOR4/blob/master/LICENSE.txt"
LABEL maintainer="Rachael St. Jacques"
LABEL maintainer.email="rachael.stjacques@dgs.virginia.gov"

RUN apt-get update && apt-get -y upgrade && apt-get -y  --no-install-recommends install \
    exonerate \
    git \
    maven \
    openjdk-11-jre-headless \
    unzip \
    wget \
    && rm -rf /var/lib/apt/lists/*

#get VIGOR4
RUN wget https://github.com/JCVenterInstitute/VIGOR4/archive/7fa683e5694d896b2a44de09383a248817d7c46a.zip && \
    unzip 7fa683e5694d896b2a44de09383a248817d7c46a.zip && \
    mv VIGOR4-7fa683e5694d896b2a44de09383a248817d7c46a VIGOR4 && \
    rm 7fa683e5694d896b2a44de09383a248817d7c46a.zip && \
    cd VIGOR4 && \
    mvn -DskipTests clean package && \
    unzip target/vigor-4.1.20190131.zip

RUN cd VIGOR4 && \
    mkdir tmp && \
    cd tmp && \
    mkdir vigor-temp

#get databases
RUN wget https://github.com/JCVenterInstitute/VIGOR_DB/archive/eb493eb1222dc31d96ec03a8f99c1fa55fc99d3f.zip && \
    unzip eb493eb1222dc31d96ec03a8f99c1fa55fc99d3f.zip && \
    rm eb493eb1222dc31d96ec03a8f99c1fa55fc99d3f.zip && \
    mv VIGOR_DB-eb493eb1222dc31d96ec03a8f99c1fa55fc99d3f VIGOR_DB

#set paths for refs, exonerate, and tmp directory in the config file
RUN cd VIGOR4/vigor-4.1.20190131/config && \
    (echo  "\nreference_database_path=/VIGOR_DB/Reference_DBs/\nexonerate_path=/usr/bin/exonerate\ntemporary_directory=/VIGOR4/tmp/vigor-temp\n" > vigor.ini)

#permissions
RUN chmod 777 -R VIGOR4

#set paths
ENV PATH="/usr/bin/exonerate:\
/VIGOR_DB/Reference_DBs:\
/VIGOR4/vigor-4.1.20190131/bin/:\
$PATH"\
    LC_ALL=C

RUN mkdir /data
WORKDIR /data
