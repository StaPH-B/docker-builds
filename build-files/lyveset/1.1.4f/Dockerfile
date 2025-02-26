FROM ubuntu:xenial as app
ARG LYVESET_VER="1.1.4f"
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="4"
LABEL software="Lyve-SET"
LABEL software.version="1.1.4f"
LABEL description="LYVE-SET, a method of using hqSNPs to create a phylogeny, especially for outbreak investigations"
LABEL website="https://github.com/lskatz/lyve-SET"
LABEL license="https://github.com/lskatz/lyve-SET/blob/master/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Erik Wolfsohn"
LABEL maintainer3.email="ewolfsohn@gmail.com"

#run apt in noninteractive mode so it can't prompt for input
ENV DEBIAN_FRONTEND noninteractive

#update apt from closest mirrors
RUN echo 'deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-security main restricted universe multiverse'  | cat - /etc/apt/sources.list > temp && mv temp /etc/apt/sources.list &&\
    echo 'deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-backports main restricted universe multiverse'  | cat - /etc/apt/sources.list > temp && mv temp /etc/apt/sources.list &&\
    echo 'deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted universe multiverse'  | cat - /etc/apt/sources.list > temp && mv temp /etc/apt/sources.list &&\
    echo 'deb mirror://mirrors.ubuntu.com/mirrors.txt xenial main restricted universe multiverse'  | cat - /etc/apt/sources.list > temp && mv temp /etc/apt/sources.list

RUN apt update && apt-get install -y \
    curl \
    perl \
    libfile-slurp-perl \
    default-jre \
    bioperl \
    wget \
    libz-dev \
    git \
    libncurses5-dev \
    libncursesw5-dev \
    build-essential \
    ncbi-blast+ \
    libsvn-perl \
    subversion \
    libsvn1 \
    automake1.11 \
    libpthread-stubs0-dev \
    cpanminus \
    mpich \
    clang \
    libssl-dev \
    libio-socket-ssl-perl \
    libxml-simple-perl \
    unzip \
    smalt \
    python3 &&\
    apt-get clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /edirect && \
    perl -MNet::FTP -e '$ftp = new Net::FTP("ftp.ncbi.nlm.nih.gov", Passive => 1);$ftp->login; $ftp->binary;$ftp->get("/entrez/entrezdirect/edirect.tar.gz");' && \
    gunzip -c edirect.tar.gz | tar xf - && \
    mv -v /edirect/* /usr/local/bin && \
    rm edirect.tar.gz

# install missing xtract executable required by efetch
RUN wget https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/xtract.Linux.gz && \
    gunzip -f xtract.Linux.gz && \
    mv -v xtract.Linux /usr/local/bin/xtract && \
    chmod +x /usr/local/bin/xtract

#get lyveset files
RUN wget https://github.com/lskatz/lyve-SET/archive/v${LYVESET_VER}.tar.gz &&\
    tar -xzvf v${LYVESET_VER}.tar.gz &&\
    rm v${LYVESET_VER}.tar.gz &&\
    mv lyve-SET-${LYVESET_VER} lyve-SET

# download perl modules, setup the lyveset filesystem
RUN cpanm Test::Most Bio::FeatureIO String::Escape File::Slurp URI::Escape Math::Round Schedule::SGE --force
RUN make -C /lyve-SET install -e PREFIX=/lyve-SET &&\
    make -C /lyve-SET env -e PREFIX=/lyve-SET

RUN make -C /lyve-SET clean-edirect

# set PATH and locale settings for singularity compatibility
ENV PATH="/lyve-SET:\
/lyve-SET/scripts:\
/edirect:\
${PATH}"\
    LC_ALL=C

WORKDIR /data

FROM app as test

RUN set_test.pl --numcpus 4 lambda lambda
