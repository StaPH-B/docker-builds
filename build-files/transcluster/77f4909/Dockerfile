FROM ubuntu:jammy AS app 

ARG COMMIT="77f4909"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="transcluster R package"
LABEL software.version="${COMMIT}"
LABEL description="Infer transmission clusters from SNP and timing data"
LABEL website="https://github.com/JamesStimson/transcluster"
LABEL license="https://github.com/JamesStimson/transcluster/blob/master/DESCRIPTION"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    r-cran-devtools \
    r-cran-igraph \
    r-cran-rmarkdown \
    r-cran-rlang \
    r-cran-lifecycle \
    r-cran-glue \
    r-cran-cli \
    r-cran-vctrs \
    r-cran-stringi \
    r-cran-magrittr \
    r-cran-stringr \
    r-cran-cluster \
    r-cran-clue \
    && apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN R -e "devtools::install_github('JamesStimson/transcluster@${COMMIT}', build_vignettes = TRUE, dependencies = FALSE)"

ENV LC_ALL=C

WORKDIR /data

CMD ["R", "-e", "help(package='transcluster')"]

## TEST ##
FROM app AS test

WORKDIR /tests 

COPY test1.R test2.R /tests/

RUN mkdir test1 test2 &&\
    cd test1 &&\
    R < ../test1.R --vanilla &&\
    cd ../test2 &&\
    R < ../test2.R --vanilla