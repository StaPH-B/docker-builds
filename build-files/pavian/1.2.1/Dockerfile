FROM rocker/shiny:4.1.0 as app

ARG SOFTWARENAME_VER="1.2.1"

LABEL base.image="rocker/shiny:4.1.0"
LABEL dockerfile.version="1"
LABEL software="Pavian"
LABEL software.version="${SOFTWARENAME_VER}"
LABEL description="Interactive analysis of metagenomics data for microbiome studies and pathogen identification."
LABEL website="https://github.com/fbreitwieser/pavian"
LABEL license="https://github.com/fbreitwieser/pavian/blob/master/DESCRIPTION"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    liblzma-dev \
    libbz2-dev &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# based on https://github.com/fbreitwieser/pavian/blob/master/inst/docker/Dockerfile by Florian Breitwieser
RUN R -e "install.packages('BiocManager', version = 3.13 , clean = TRUE); BiocManager::install('Rsamtools', ask=FALSE)" &&\
    R -e "install.packages('remotes', clean = TRUE);remotes::install_github('fbreitwieser/pavian@750a18073bae3c443d8b9465d8d6e997595788be', clean = TRUE)" &&\
    rm -rf /srv/shiny-server/* &&\
    R -e "sapply(list.files(system.file('shinyapp',package='pavian'),full.names=TRUE),file.copy,to='/srv/shiny-server/',recursive=TRUE)"

EXPOSE 3838

CMD ["/usr/bin/shiny-server"]

ENV LC_ALL=C

WORKDIR /data

## Test ##
FROM app as test

CMD ["/bin/bash"]

RUN R -e "installed.packages()" > test.log &&\
    cat test.log
