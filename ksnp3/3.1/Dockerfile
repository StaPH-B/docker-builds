FROM ubuntu:xenial
 
# metadata
LABEL base.image="ubuntu:xenial"
LABEL version="1"
LABEL software="kSNP3"
LABEL software.version="3.1"
LABEL description="K-mer-based phylgenetic inference"
LABEL website="https://github.com/cdeanj/kSNP3/blob/master/kSNP3"
LABEL maintainer="Kevin Libuit"
LABEL maintainer.email="kevin.libuit@dgs.virginia.gov"

RUN apt-get update && apt-get install -y python \
  wget tcsh unzip make gcc build-essential

# install RaxML
RUN cd / &&\
  wget https://github.com/stamatak/standard-RAxML/archive/v8.2.12.tar.gz && \
  tar xvfz v8.2.12.tar.gz && \
  cd /standard-RAxML-8.2.12 && \
  make -f Makefile.SSE3.PTHREADS.gcc && \
  rm *.o && \
  ln -s $(pwd)/raxmlHPC-PTHREADS-SSE3 /usr/bin/raxml && \
  chmod a+x ./usefulScripts/*.* && \
  sed -i 's/^\$raxmlExecutable =*.*/\$raxmlExecutable = "raxml";/' ./usefulScripts/ProteinModelSelection.pl 
	
ENV PATH="${PATH}:/standard-RAxML-8.2.12/usefulScripts/"

RUN wget https://sourceforge.net/projects/ksnp/files/kSNP3.1_Linux_package.zip && \
  unzip kSNP3.1_Linux_package.zip && \
  mv /kSNP3.1_Linux_package/kSNP3/ /usr/local && \
  rm -r kSNP3.1_Linux_package.zip && \
  mkdir data

ENV PATH ="${PATH}:/usr/local/kSNP3/"

WORKDIR /data
