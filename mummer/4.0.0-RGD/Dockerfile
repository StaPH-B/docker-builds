FROM ubuntu:focal as app

# ARG sets environment variables during the build stage
ARG MUMMER_VER="4.0.0"

# LABEL instructions tag the image with metadata that might be important to the user
LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="mummer"
LABEL software.version=${MUMMER_VER}
LABEL description="MUMmer is a versatile alignment tool for DNA and protein sequences."
LABEL website="https://github.com/mummer4/mummer"
LABEL license="https://github.com/mummer4/mummer/blob/master/LICENSE.md"
LABEL maintainer1="John Arnn"
LABEL maintainer1.email="jarnn@utah.gov"
LABEL maintaine2r="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# to prevent tzdata from asking for a region during apt updates; ARG so that variable only 
# persists at buildtime
ARG DEBIAN_FRONTEND=noninteractive

# RUN executes code during the build
# Install dependencies via apt-get or yum if using a centos or fedora base
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 git \
 libncurses5-dev \
 libbz2-dev \
 liblzma-dev \
 libcurl4-gnutls-dev \
 zlib1g-dev \
 libssl-dev \
 gcc \
 make \
 perl \
 bzip2 \
 gnuplot \
 ca-certificates \
 gawk \
 curl \
 sed \
 build-essential \
 unzip && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/*

 # install mummer
RUN wget https://github.com/mummer4/mummer/releases/download/v${MUMMER_VER}rc1/mummer-${MUMMER_VER}rc1.tar.gz && \
  tar -xvf mummer-${MUMMER_VER}rc1.tar.gz && \
  rm mummer-${MUMMER_VER}rc1.tar.gz && \
  cd mummer-${MUMMER_VER}rc1 && \
  ./configure && \
  make && \
  make install && \
  ldconfig && \
  cd .. && \
  mkdir /data

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

# copy in list of NCBI accessions and species list
COPY RGDv2-NCBI-assembly-accessions.txt /RGDv2/RGDv2-NCBI-assembly-accessions.txt
COPY RGDv2-NCBI-assembly-accessions-and-species.txt /RGDv2/RGDv2-NCBI-assembly-accessions-and-species.txt

# download RGD genomes using NCBI datasets tools; cleanup unneccessary files; 
# move and re-name assemblies to include Species in the filename
# make fasta files readable to all users; create File Of FileNames for all 43 assemblies (to be used with fastANI)
RUN for ID in $(cat /RGDv2/RGDv2-NCBI-assembly-accessions.txt); do \
 SPECIES=$(grep "${ID}" /RGDv2/RGDv2-NCBI-assembly-accessions-and-species.txt | cut -f 1) && \
 echo "downloading $ID, species "${SPECIES}", from NCBI..."; \
 datasets download genome accession --filename ${ID}.zip ${ID}; \
 unzip ${ID}.zip; \
 rm ${ID}.zip; \
 mv -v ncbi_dataset/data/${ID}/${ID}*.fna /RGDv2/${ID}.${SPECIES}.fasta; \
 rm -rfv ncbi_dataset/; \
 rm -v README.md; \
done && \
ls /RGDv2/*.fasta >/RGDv2/FOFN-RGDv2.txt && \
chmod 664 /RGDv2/*

# for singularity compatibility
ENV LC_ALL=C

# WORKDIR sets working directory
WORKDIR /data

FROM app as test

RUN nucmer -h && \
  promer -h && \
  wget https://mummer4.github.io/tutorial/exampleFiles/2.1/in/H_pylori26695_Eslice.fasta && \
  wget https://mummer4.github.io/tutorial/exampleFiles/2.1/in/H_pyloriJ99_Eslice.fasta && \
  wget https://mummer4.github.io/tutorial/exampleFiles/2.2/in/B_anthracis_Mslice.fasta && \
  wget https://mummer4.github.io/tutorial/exampleFiles/2.2/in/B_anthracis_contigs.fasta && \
  wget http://mummer.sourceforge.net/examples/data/H_pylori26695_Eslice.fasta && \
  wget http://mummer.sourceforge.net/examples/data/H_pyloriJ99_Eslice.fasta && \
  mummer -mum -b -c H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta > mummer.mums && \
  mummerplot -x "[0,275287]" -y "[0,265111]" --terminal png -postscript -p mummer mummer.mums && \
  nucmer  -c 100 -p nucmer B_anthracis_Mslice.fasta B_anthracis_contigs.fasta && \
  show-snps -C nucmer.delta > nucmer.snps && \
  promer -p promer_100 -c 100  H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta
