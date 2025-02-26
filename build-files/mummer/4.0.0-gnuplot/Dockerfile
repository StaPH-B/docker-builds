FROM ubuntu:focal as app

# ARG sets environment variables during the build stage; they do not persist after the image is built
ARG MUMMER_VER="4.0.0"
ARG MASH_VER="2.3"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="mummer"
LABEL software.version=${MUMMER_VER}
LABEL description="MUMmer is a versatile alignment tool for DNA and protein sequences."
LABEL website="https://github.com/mummer4/mummer"
LABEL license="https://github.com/mummer4/mummer/blob/master/LICENSE.md"
LABEL maintainer="John Arnn"
LABEL maintainer.email="jarnn@utah.gov"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erin Young"
LABEL maintainer3.email="eriny@utah.gov"

# to prevent tzdata from asking for a region during apt updates
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies via apt; clean up apt garbage
# gnuplot version 5.2 patchlevel 8
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
  gnuplot \
  build-essential \
  unzip && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install mummer; make /data for use as working directory
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

# install ncbi datasets tool (pre-compiled binary) version 14.17.0; place in $PATH
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
    unzip -q ${ID}.zip; \
    rm ${ID}.zip; \
    mv -v ncbi_dataset/data/${ID}/${ID}*.fna /RGDv2/${ID}.${SPECIES}.fasta; \
    rm -rf ncbi_dataset/; \
    rm README.md; \
  done && \
  ls /RGDv2/*.fasta >/RGDv2/FOFN-RGDv2.txt && \
  chmod 664 /RGDv2/*

# downloading mash binary
RUN wget https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
  tar -xvf mash-Linux64-v${MASH_VER}.tar && \
  rm -rf mash-Linux64-v${MASH_VER}.tar

# download Lee's ani-m script
RUN wget https://github.com/lskatz/ani-m/archive/refs/tags/v0.1.tar.gz && \
  tar xzf v0.1.tar.gz && \
  rm -v v0.1.tar.gz

# LC_ALL for singularity compatibility; set PATH
ENV LC_ALL=C \
  PATH="${PATH}:/ani-m-0.1:/mash-Linux64-v${MASH_VER}"

# set working directory
WORKDIR /data

FROM app as test

# test that mash is in the PATH
RUN mash --help && mash --version

# test a few commands part of the mummer package
RUN nucmer -h && nucmer --version && \
  promer -h && promer --version && \
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
  promer -p promer_100 -c 100  H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta && \
  mummerplot -l nucmer.delta -p test_mummer_plot --png && \
  gnuplot test_mummer_plot.gp

# testing ani-m.pl (which runs 'dnadiff' and 'mash' under the hood)
# comparing one of the reference genomes to another
RUN ani-m.pl --symmetric --mash-filter 0.9 \
  /RGDv2/GCA_014526935.1.Listeria_monocytogenes.fasta \
  /RGDv2/GCA_001466295.1.Listeria_monocytogenes.fasta \
  | tee test-output-ani-m.tsv
