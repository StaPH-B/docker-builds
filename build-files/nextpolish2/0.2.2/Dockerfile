FROM mambaorg/micromamba:2.9.0-ubuntu22.04 AS app

ARG NEXTPOLISH2_VER="0.2.2"

USER root

WORKDIR /

LABEL base.image="mambaorg/micromamba:2.3.0-ubuntu22.04"
LABEL dockerfile.version="1"
LABEL software="SOFTWARENAME"
LABEL software.version="${NEXTPOLISH2_VER}"
LABEL description="Repeat-aware polishing tool for genomes assembled using HiFi long reads"
LABEL website="https://github.com/Nextomics/NextPolish2"
LABEL license="https://github.com/Nextomics/NextPolish2/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN micromamba install --name base -c conda-forge -c bioconda \
    nextpolish2=${NEXTPOLISH2_VER} \
    meryl \
    winnowmap \
    samtools \
    minimap2 && \
    micromamba clean -a -f -y

ENV PATH="/opt/conda/bin/:${PATH}" \
    LC_ALL=C.UTF-8

CMD [ "nextPolish2", "--help" ]

WORKDIR /data

## Test data ##
FROM staphb/sratoolkit AS data

RUN fasterq-dump SRR31499991 SRR9043691 &&\
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/046/272/015/GCF_046272015.1_ASM4627201v1/GCF_046272015.1_ASM4627201v1_genomic.fna.gz -O asm.fa.gz

## Test ##
FROM app AS test

COPY --from=data /data/* /data/

RUN meryl count k=15 output merylDB asm.fa.gz &&\
    meryl print greater-than distinct=0.9998 merylDB > repetitive_k15.txt &&\
    winnowmap -W repetitive_k15.txt -ax map-pb asm.fa.gz SRR31499991.fastq | samtools sort -o hifi.map.sort.bam - &&\
    samtools index hifi.map.sort.bam &&\
    yak count -o k21.yak -k 21 <(cat SRR9043691_1.fastq) <(cat SRR9043691_2.fastq) &&\
    yak count -o k31.yak -k 31 <(cat SRR9043691_1.fastq) <(cat SRR9043691_2.fastq) &&\
    nextPolish2 -t 4 hifi.map.sort.bam asm.fa.gz k21.yak k31.yak > asm.np2.fa



