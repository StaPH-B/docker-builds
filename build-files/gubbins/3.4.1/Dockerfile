FROM mambaorg/micromamba:2.3.1-ubuntu22.04 AS app

ARG GUBBINS_VER="3.4.1"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.1-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="Gubbins"
LABEL software.version="${GUBBINS_VER}"
LABEL description="Genealogies Unbiased By recomBinations In Nucleotide Sequences"
LABEL website="https://github.com/nickjcroucher/gubbins"
LABEL license="https://github.com/nickjcroucher/gubbins/blob/master/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN micromamba install --name base -c conda-forge -c bioconda gubbins=${GUBBINS_VER} && \
    micromamba clean -afy

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD ["run_gubbins.py", "-h"]

WORKDIR /data

FROM app AS test

RUN run_gubbins.py -h

WORKDIR /test

RUN curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36" \
    -e "https://figshare.com/articles/dataset/PMEN1_aln_gz/18685694?file=33468725" \
    -o "PMEN1.aln.gz" \
    "https://figshare.com/ndownloader/files/33468725" 
    
RUN gunzip PMEN1.aln.gz &&\
    run_gubbins.py PMEN1.aln

