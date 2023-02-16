FROM ubuntu:xenial as app

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="2"
LABEL software="cfsan_snp_pipeline"
LABEL software.version="2.0.2"
LABEL description="A pipeline for the production of SNP matrices from sequence data used in the phylogenetic analysis of pathogenic organisms sequenced from samples of interest to food safety."
LABEL website="https://github.com/CFSAN-Biostatistics/snp-pipeline"
LABEL license="https://github.com/CFSAN-Biostatistics/snp-pipeline/blob/master/LICENSE.txt"
LABEL original.maintainer="Justin Payne"
LABEL original.maintainer.email="justin.payne@fda.hhs.gov"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# This Dockerfile is based on a Docker file from Justin Payne which can be found here:
# https://hub.docker.com/r/crashfrog/snp-pipeline/dockerfile
# The dockerfile has been modified from it's original form by Curtis Kapsak and Sam Baird

WORKDIR /tmp/
RUN apt-get update -y \
	&& apt-get install -y --no-install-recommends \
		bowtie2 \
		openjdk-8-jre \
		g++ \
		gcc \
		gsl-bin \
		libgsl0-dev \
		make \
                perl \
                bzip2 \
		python \
		python-dev \
		wget \
                tabix \
                libncurses5-dev \
                libbz2-dev \
                liblzma-dev \
                libcurl4-gnutls-dev \
                zlib1g-dev \
                libssl-dev \
                build-essential \
                ca-certificates \
                libperl-dev \
	&& apt-get clean

ARG SNP_PIPELINE_VER
ENV SNP_PIPELINE_VER=${SNP_PIPELINE_VER:-2.0.2}

# install pip (code originally from Justin)
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py  -q \
	&& python get-pip.py

# install samtools, since the version in apt-get is too far out-of-date
RUN mkdir samtools &&\
  cd samtools &&\
  wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 &&\
  tar -xjf samtools-1.9.tar.bz2 &&\
  rm samtools-1.9.tar.bz2 &&\
  cd samtools-1.9 &&\
  ./configure &&\
  make &&\
  make install

# install bcftools
RUN mkdir bcftools &&\
    cd bcftools &&\
    wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2 &&\
    tar -xjf bcftools-1.9.tar.bz2 &&\
    rm bcftools-1.9.tar.bz2 &&\
    cd bcftools-1.9 &&\
    ./configure &&\
    make &&\
    make install

# get picard jar file
RUN mkdir /picard &&\
    cd /picard &&\
    wget https://github.com/broadinstitute/picard/releases/download/2.18.4/picard.jar

# get GATK 3.8-1-0 jar flie
RUN mkdir /gatk &&\
    cd /gatk &&\
    wget -O ./gatk.tar.bz2 'https://storage.googleapis.com/gatk-software/package-archive/gatk/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2' &&\
    tar -xjvf gatk.tar.bz2 &&\
    rm gatk.tar.bz2

# get VarScan and SRA-toolkit
RUN wget http://downloads.sourceforge.net/project/varscan/VarScan.v2.3.7.jar -q \
	&& cp VarScan.v2.3.7.jar /usr/bin/VarScan.jar \
	&& cd /tmp/ \
	&& wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.3.5-2/sratoolkit.2.3.5-2-ubuntu64.tar.gz -q \
	&& tar -zxf /tmp/sratoolkit.2.3.5-2-ubuntu64.tar.gz \
	&& cp /tmp/sratoolkit.2.3.5-2-ubuntu64/bin/fastq-dump.2.3.5.2 /usr/bin/fastq-dump \
	&& rm -r /tmp/*

#install snp-pipeline and snp-mutator
RUN pip install numpy snp-pipeline==$SNP_PIPELINE_VER biopython==1.68 snp-mutator

# set java CLASSPATH variables
ENV CLASSPATH /usr/bin/VarScan.jar:/picard/picard.jar:/gatk/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef/GenomeAnalysisTK.jar
# not sure why this is here, or what program uses NUMCORES, but I'm going to leave it for now.
ENV NUMCORES 1

# make a DIR called /data for running cfsan-snp-pipeline in
WORKDIR /data

# Test snp_pipeline (code modified from Justin). Running copy_snppipeline_data.py generates an message the the script is deprecated
# but I figured I would leave it since the below commands test that the image runs properly.
FROM app as test
WORKDIR /test/
RUN copy_snppipeline_data.py lambdaVirusInputs testLambdaVirus \
	&& cd testLambdaVirus \
	&& run_snp_pipeline.sh -s samples reference/lambda_virus.fasta \
	&& copy_snppipeline_data.py lambdaVirusExpectedResults expectedResults \
	&& diff -q snplist.txt expectedResults/snplist.txt >> diffOutput.txt \
	&& diff -q snpma.fasta expectedResults/snpma.fasta >> diffOutput.txt \
	&& diff -q referenceSNP.fasta expectedResults/referenceSNP.fasta >> diffOutput.txt \
    && if [ -s diffOutput.txt ]; then echo "testLambdaVirus failed"; else echo "testLambdaVirus passed"; fi

WORKDIR /data