ARG MUMMER_VER="4.0.1"

FROM ubuntu:jammy AS app

# ARG sets environment variables during the build stage; they do not persist after the image is built
ARG MUMMER_VER

LABEL base.image="ubuntu:jammy"
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

# Install dependencies via apt; clean up apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
  wget \
  perl \
  sed \
  gawk \
  fig2dev\
  gnuplot \
  xfig \ 
  unzip \
  ca-certificates \
  build-essential && \
  apt-get autoclean && rm -rf /var/lib/apt/lists/*

# there is likely someone smarter than I that can move this into a build stage
RUN wget -q https://github.com/mummer4/mummer/releases/download/v${MUMMER_VER}/mummer-${MUMMER_VER}.tar.gz && \
  tar -xvf mummer-${MUMMER_VER}.tar.gz && \
  rm mummer-${MUMMER_VER}.tar.gz && \ 
  cd mummer-${MUMMER_VER} && \
  ./configure && \
  make && \
  make check && \
  make install && \
  ldconfig && \
  # for whatever reason, promer was not picking up the environmental variables, so I hardcoded them in 
  sed -i "s|my \$BIN_DIR = '@BIN_DIR';|my \$BIN_DIR = '/mummer-${MUMMER_VER}/';|" /mummer-${MUMMER_VER}/promer  && \
  sed -i "s|my \$AUX_BIN_DIR = '@LIBEXEC_DIR';|my \$AUX_BIN_DIR = '/mummer-${MUMMER_VER}/';|" /mummer-${MUMMER_VER}/promer && \
  # removing not needed directories 
  rm -rf  /mummer-${MUMMER_VER}/unittests && \
  rm -rf  /mummer-${MUMMER_VER}/tests

ENV PATH=/mummer-${MUMMER_VER}/:$PATH \
  BIN_DIR=/mummer-${MUMMER_VER} \
  LIBEXEC_DIR=/mummer-${MUMMER_VER}

# set working directory
WORKDIR /data

CMD ["nucmer", "-h"]

FROM app AS test

# test a few commands part of the mummer package
RUN nucmer -h && nucmer --version && \
  promer -h && promer --version

RUN wget -q https://mummer4.github.io/tutorial/exampleFiles/2.1/in/H_pylori26695_Eslice.fasta && \
  wget -q https://mummer4.github.io/tutorial/exampleFiles/2.1/in/H_pyloriJ99_Eslice.fasta && \
  wget -q https://mummer4.github.io/tutorial/exampleFiles/2.2/in/B_anthracis_Mslice.fasta && \
  wget -q https://mummer4.github.io/tutorial/exampleFiles/2.2/in/B_anthracis_contigs.fasta && \
  mummer -mum -b -c H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta > mummer.mums && \
  mummerplot -x "[0,275287]" -y "[0,265111]" --terminal png -postscript -p mummer mummer.mums && \
  nucmer  -c 100 -p nucmer B_anthracis_Mslice.fasta B_anthracis_contigs.fasta && \
  show-snps -C nucmer.delta > nucmer.snps && \
  promer -p promer_100 -c 100  H_pylori26695_Eslice.fasta H_pyloriJ99_Eslice.fasta && \
  mummerplot -l nucmer.delta -p test_mummer_plot --png && \
  gnuplot test_mummer_plot.gp
