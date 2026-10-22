ARG POLYPOLISH_VER="0.7.1"
ARG BWA_VER="0.7.19"

FROM staphb/bwa:${BWA_VER} AS builder

FROM staphb/polypolish:${POLYPOLISH_VER} AS app

ARG POLYPOLISH_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="polypolish"
LABEL software.version="${POLYPOLISH_VER}"
LABEL description="Polypolish is a tool for polishing genome assemblies with short reads."
LABEL website="https://github.com/rrwick/Polypolish"
LABEL license="https://github.com/rrwick/Polypolish/blob/main/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

COPY --from=builder /usr/local/bin/bwa /usr/local/bin/

ENV LC_ALL=C

CMD ["polypolish", "--help"]

WORKDIR /data

FROM app AS test

RUN polypolish --help && polypolish --version

# using "toy" data
RUN wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/assembly.fasta && \
    wget -q https://raw.githubusercontent.com/wiki/rrwick/Polypolish/files/toy_example/alignments.sam && \
    polypolish polish assembly.fasta alignments.sam > polished.fasta

# testing bwa
RUN wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_1.fastq.gz -O r1.fq.gz && \
    wget -q ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR608/003/SRR6082043/SRR6082043_2.fastq.gz -O r2.fq.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/945/GCF_000006945.2_ASM694v2/GCF_000006945.2_ASM694v2_genomic.fna.gz && \
    gunzip -c GCF_000006945.2_ASM694v2_genomic.fna.gz > ref.fa

RUN bwa index ref.fa && \
    bwa mem ref.fa r1.fq.gz r2.fq.gz > aln.sam && \
    head aln.sam