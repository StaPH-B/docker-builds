FROM staphb/ispcr:33 AS ispcr

FROM python:3.13-slim AS app

ARG EMMTYPER_VER="0.2.0"

LABEL base.image="python:3.13-slim"
LABEL dockerfile.version="1"
LABEL software="emmtyper"
LABEL software.version=${EMMTYPER_VER}
LABEL description="Conda environment for emmtyper. emmtyper is a command line tool for emm-typing of Streptococcus pyogenes using a de novo or complete assembly."
LABEL website="https://github.com/MDU-PHL/emmtyper"
LABEL license="GNU General Public License v3.0"
LABEL license.url="https://github.com/MDU-PHL/emmtyper/blob/master/LICENSE"
LABEL maintainer="Henry Kunerth"
LABEL maintainer.email="henrykunerth@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    ncbi-blast+ && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# copy precompiled ispcr from staphb image    
COPY --from=ispcr /usr/local/bin/isPcr /usr/local/bin/isPcr

# using click<8.2 supresses duplicate flag in emmtyper
RUN pip install --no-cache-dir emmtyper==${EMMTYPER_VER} "click<8.2"

ENV LC_ALL=C.UTF-8

# first, check that the default db files are there. Then remove them and download new ones.
WORKDIR /usr/local/lib/python3.13/site-packages/emmtyper/db

RUN ls * && head db_metadata.json && ls emm.fna && \
    rm * && \
    wget --progress=dot:giga https://ftp.cdc.gov/pub/infectious_diseases/biotech/tsemm/alltrimmed.tfa && \
    mv alltrimmed.tfa emm.fna && \
    makeblastdb -in emm.fna -dbtype nucl -out emm.fna

CMD ["emmtyper", "--help"]

WORKDIR /data

FROM app AS test

WORKDIR /test

RUN emmtyper --help && emmtyper --version

RUN wget --progress=dot:giga ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/006/785/GCA_000006785.2_ASM678v2/GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	gunzip GCA_000006785.2_ASM678v2_genomic.fna.gz && \
	mv GCA_000006785.2_ASM678v2_genomic.fna test_data.fasta

RUN emmtyper test_data.fasta && \
    emmtyper -w pcr --primer-db /usr/local/lib/python3.13/site-packages/emmtyper/data/isPcrPrim.tsv test_data.fasta -o test_out && \
    head test_out

RUN pip list
