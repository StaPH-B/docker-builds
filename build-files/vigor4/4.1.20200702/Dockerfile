FROM ubuntu:jammy as app

ARG VIGOR4_VER='4.1.20200702'
ARG VIGOR4_COMMIT='23852472af871b6c05bd5abf2022d140b9cecd3b'
ARG VIGOR4_DB_COMMIT='390582955049b9ddc989510672fbde90cf3387c7'

LABEL base.image="ubuntu:jammy"
LABEL container.version="1"
LABEL dockerfile.version="1"
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
    wget && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

#get VIGOR4
RUN wget -q https://github.com/JCVenterInstitute/VIGOR4/archive/${VIGOR4_COMMIT}.zip && \
    unzip ${VIGOR4_COMMIT}.zip && \
    mv VIGOR4-${VIGOR4_COMMIT} /VIGOR4 && \
    rm ${VIGOR4_COMMIT}.zip && \
    cd /VIGOR4 && \
    mvn -DskipTests clean package && \
    unzip /VIGOR4/target/vigor-${VIGOR4_VER}.zip && \
    rm /VIGOR4/target/vigor-${VIGOR4_VER}.zip && \
    # create temp directory
    mkdir -p /VIGOR4/tmp/vigor-temp && \
    # make executable
    chmod 777 -R /VIGOR4/vigor-${VIGOR4_VER}/bin/vigor4 && \
    #set paths for refs, exonerate, and tmp directory in the config file
    cd /VIGOR4/vigor-${VIGOR4_VER}/config && \
    (echo  "\nreference_database_path=/VIGOR_DB/Reference_DBs/\nexonerate_path=/usr/bin/exonerate\ntemporary_directory=/VIGOR4/tmp/vigor-temp\n" > vigor.ini)

#get databases
RUN wget -q https://github.com/JCVenterInstitute/VIGOR_DB/archive/${VIGOR4_DB_COMMIT}.zip && \
    unzip ${VIGOR4_DB_COMMIT}.zip && \
    rm ${VIGOR4_DB_COMMIT}.zip && \
    mv VIGOR_DB-${VIGOR4_DB_COMMIT} /VIGOR_DB

#set paths
ENV PATH="/usr/bin/exonerate:/VIGOR_DB/Reference_DBs:/VIGOR4/vigor-${VIGOR4_VER}/bin/:$PATH"\
    LC_ALL=C

CMD vigor4 -h

RUN mkdir /data
WORKDIR /data

# testing stage
FROM app as test

WORKDIR /test

# checking help and version
RUN vigor4 -h && vigor4 --version

# list databases
RUN ls /VIGOR_DB/Reference_DBs | grep -v ini

# running on test files
RUN vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/rtva/rtva.ungapped.fasta -o test_rtva_db -d /VIGOR_DB/Reference_DBs/rtva_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/rtvb/rtvb.ungapped.fasta -o test_rtvb_db -d /VIGOR_DB/Reference_DBs/rtvb_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/rtvc/rtvc.ungapped.fasta -o test_rtvc_db -d /VIGOR_DB/Reference_DBs/rtvc_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/rtvf/rtvf.ungapped.fasta -o test_rtvf_db -d /VIGOR_DB/Reference_DBs/rtvf_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/rtvg/rtvg.ungapped.fasta -o test_rtvg_db -d /VIGOR_DB/Reference_DBs/rtvg_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/sapo/sapo.ungapped.fasta -o test_sapo_db -d /VIGOR_DB/Reference_DBs/sapo_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/wnvI/wnvI.ungapped.fasta -o test_wnvI_db -d /VIGOR_DB/Reference_DBs/wnvI_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/wnvII/wnvII.ungapped.fasta -o test_wnvII_db -d /VIGOR_DB/Reference_DBs/wnvII_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/zikv/zikv.ungapped.fasta -o test_zikv_db -d /VIGOR_DB/Reference_DBs/zikv_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/flua/flua.ungapped.fasta -o test_flua_db -d /VIGOR_DB/Reference_DBs/flua_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/flub/flub.ungapped.fasta -o test_flub_db -d /VIGOR_DB/Reference_DBs/flub_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/fluc/fluc.ungapped.fasta -o test_fluc_db -d /VIGOR_DB/Reference_DBs/fluc_db && \
    vigor4 -i /VIGOR4/src/test/resources/vigor4ReferenceOutput/veev/veev.ungapped.fasta -o test_veev_db -d /VIGOR_DB/Reference_DBs/veev_db && \
    head test*.tbl
