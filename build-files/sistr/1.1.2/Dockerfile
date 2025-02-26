FROM ubuntu:focal AS app

ARG SISTR_VER="1.1.2"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SISTR"
LABEL software.version="1.1.2"
LABEL description="Salmonella In Silico Typing Resource (SISTR)"
LABEL website="https://github.com/peterk87/sistr_cmd"
LABEL license="https://github.com/peterk87/sistr_cmd/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="kapsakcj@gmail.com"
LABEL maintainer2="Kutluhan Incekara"
LABEL maintainer2.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    python3-pycurl \
    ncbi-blast+ \
    mafft \
    mash &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir sistr_cmd==${SISTR_VER}

WORKDIR /data

ENV LC_ALL=C

CMD ["sistr", "--help"]

## Test ##
FROM app AS test

RUN apt-get update && apt-get install wget

# Testing Salmonella enterica subsp. salamae serovar 58:l,z13,z28:z6 str. 00-0163 SES60163_1000002
RUN wget -q https://github.com/phac-nml/sistr_cmd/raw/master/tests/00_0163.fasta &&\
    sistr --qc -vv --alleles-output 00_0163.allele-results.json --novel-alleles 00_0163.novel-alleles.fasta --cgmlst-profiles 00_0163.cgmlst-profiles.csv -f tab -o 00_0163.sistr-output.tab 00_0163.fasta &&\
    cat 00_0163.sistr-output.tab

# Testing Salmonella enterica subsp. enterica serovar Typhimurium str. LT2 (https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000006945.2/)
RUN wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz &&\
    gunzip GCF_000006945.2_ASM694v2_genomic.fna.gz &&\
    sistr --qc -vv --alleles-output allele-results.json --novel-alleles novel-alleles.fasta --cgmlst-profiles cgmlst-profiles.csv -f tab -o sistr-output.tab GCF_000006945.2_ASM694v2_genomic.fna &&\
    cat sistr-output.tab 

