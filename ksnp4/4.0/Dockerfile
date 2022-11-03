FROM ubuntu:jammy as app
 
# metadata
LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="kSNP4"
LABEL software.version="4.0"
LABEL description="K-mer-based phylogenetic inference"
LABEL website="https://sourceforge.net/projects/ksnp/"
LABEL license="https://github.com/kissake/kSNP4/blob/%40/THE%20BSD%20OPENSOURCE%20LICENSE.pdf"
LABEL maintainer="Jeremiah Nisbet"
LABEL maintainer.email="ksnp-dev@kissake.net"


RUN apt-get update && apt-get install -y python2 \
  wget tcsh unzip make gcc build-essential && \
  cd /opt &&\
  wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz && \
  tar xvfz v8.2.12.tar.gz && \
  cd /opt/standard-RAxML-8.2.12 && \
  make -f Makefile.SSE3.PTHREADS.gcc && \
  rm *.o && \
  ln -s $(pwd)/raxmlHPC-PTHREADS-SSE3 /usr/bin/raxml && \
  chmod a+x ./usefulScripts/*.* && \
  sed -i 's/^\$raxmlExecutable =*.*/\$raxmlExecutable = "raxml";/' ./usefulScripts/ProteinModelSelection.pl && \
  cd /opt/ && \
  wget "https://sourceforge.net/projects/ksnp/files/kSNP4 Linux package.zip" && \
  unzip "kSNP4 Linux package.zip" && \
  mv "kSNP4 Linux package/kSNP4pkg/" /usr/local/ && \
  rm -r "kSNP4 Linux package.zip" && \
  mkdir data

ENV PATH "/usr/local/kSNP4pkg:${PATH}:/standard-RAxML-8.2.12/usefulScripts/"

WORKDIR /data

FROM app as test

COPY kSNP_test.sh RunExamples.sh ./

RUN bash ./kSNP_test.sh
