FROM ubuntu:xenial as app

# metadata
LABEL base.image="ubuntu:xenial"
LABEL dockerfile.version="1"
LABEL software="cfsan_snp_pipeline"
LABEL software.version="2.2.1"
LABEL description="A pipeline for the production of SNP matrices from sequence data used in the phylogenetic analysis of pathogenic organisms sequenced from samples of interest to food safety."
LABEL website="https://github.com/CFSAN-Biostatistics/snp-pipeline"
LABEL license="https://github.com/CFSAN-Biostatistics/snp-pipeline/blob/master/LICENSE.txt"
LABEL original.maintainer="Justin Payne"
LABEL original.maintainer.email="justin.payne@fda.hhs.gov"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"

# This Dockerfile is based on a Docker file from Justin Payne which can be found here:
# https://github.com/CFSAN-Biostatistics/snp-pipeline/blob/master/Dockerfile
# The dockerfile has been modified from it's original form by Curtis Kapsak and Sam Baird

WORKDIR /tmp/
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		bzip2 \
		default-jre \
		g++ \
		gcc \
		git \
		gsl-bin \
		libgsl0-dev \
		libtbb-dev \
		libbz2-dev \
		liblzma-dev \
		make \
		ncurses-dev \
		python \
		python-dev \
		tabix \
		wget \
		zlib1g-dev \
        ca-certificates \
	&& apt-get clean

# Dependency version, can be updated in the build with build_args
ARG SNP_PIPELINE_VER
ENV SNP_PIPELINE_VER=${SNP_PIPELINE_VER:-2.2.1}

ARG BCFTOOLS_VER
ENV BCFTOOLS_VER=${BCFTOOLS_VER:-1.8}
ARG BOWTIE2_VER
ENV BOWTIE2_VER=${BOWTIE2_VER:-2.3.4.1}
ARG HTSLIB_VER
ENV HTSLIB_VER=${HTSLIB_VER:-1.3.2}
ARG GATK_VER
ENV GATK_VER=${GATK_VER:-3.4-46-gbc02625}
ARG PICARD_VER
ENV PICARD_VER=${PICARD_VER:-2.18.4}
ARG SAMTOOLS_VER
ENV SAMTOOLS_VER=${SAMTOOLS_VER:-1.8}
ARG SRATOOLKIT_VER
ENV SRATOOLKIT_VER=${SRATOOLKIT_VER:-2.8.1}
ARG VARSCAN_VER
ENV VARSCAN_VER=${VARSCAN_VER:-2.3.9}
ARG NUMPY_VER
ENV NUMPY_VER=${NUMPY_VER:-1.16.6}
ARG BIOPYTHON_VER
ENV BIOPYTHON_VER=${BIOPYTHON_VER:-1.68}


# install pip (code originally from Justin)
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py  -q \
	&& python get-pip.py

#install bowtie2
#add -std:c++11 to make for compiler support
RUN wget https://github.com/BenLangmead/bowtie2/archive/v$BOWTIE2_VER.tar.gz -qO						 			- | tar xz && cd bowtie2-$BOWTIE2_VER  && make && make install && cd /tmp

#install samtools
RUN	wget https://github.com/samtools/htslib/releases/download/$HTSLIB_VER/htslib-$HTSLIB_VER.tar.bz2 -qO       		- | tar xj && (cd htslib-$HTSLIB_VER  	 && make && make install && cd /tmp)
RUN wget https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VER/samtools-$SAMTOOLS_VER.tar.bz2 -qO  	- | tar xj && (cd samtools-$SAMTOOLS_VER && make && make install && cd /tmp)
RUN wget https://github.com/samtools/bcftools/releases/download/$BCFTOOLS_VER/bcftools-$BCFTOOLS_VER.tar.bz2 -qO 	- | tar xj && (cd bcftools-$BCFTOOLS_VER && make && make install && cd /tmp)

#install VARSCAN, ART, SRA Toolkit, GATK, Picard
RUN wget http://downloads.sourceforge.net/project/varscan/VarScan.v$VARSCAN_VER.jar -q \
	&& cp VarScan.v$VARSCAN_VER.jar /usr/bin/VarScan.jar 
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/$SRATOOLKIT_VER/sratoolkit.$SRATOOLKIT_VER-ubuntu64.tar.gz -q \
	&& tar -zxf /tmp/sratoolkit.$SRATOOLKIT_VER-ubuntu64.tar.gz \
	&& cp /tmp/sratoolkit.$SRATOOLKIT_VER-ubuntu64/bin/fastq-dump.$SRATOOLKIT_VER /usr/bin/fastq-dump 
RUN wget https://storage.googleapis.com/gatk-software/package-archive/gatk/GenomeAnalysisTK-$GATK_VER.tar.bz2 \
	&& tar -jxf /tmp/GenomeAnalysisTK-$GATK_VER.tar.bz2 \
	&& cp /tmp/GenomeAnalysisTK.jar /usr/bin/GenomeAnalysisTK.jar 
RUN wget https://github.com/broadinstitute/picard/releases/download/$PICARD_VER/picard.jar -q \
	&& cp picard.jar /usr/bin/picard.jar

#install snp-pipeline and snp-mutator
RUN pip install numpy==$NUMPY_VER \
	snp-pipeline==$SNP_PIPELINE_VER \
	biopython==$BIOPYTHON_VER


ENV PATH "$PATH:/tmp/samtools-$SAMTOOLS_VER/bin:/tmp/bcftools-$BCFTOOLS_VER/bin:/tmp/bowtie2-$BOWTIE2_VER/bin"
ENV CLASSPATH "/usr/bin/VarScan.jar:/usr/bin/picard.jar:/usr/bin/GenomeAnalysisTK.jar"
ENV NUMCORES 1

# make a DIR called /data for running cfsan-snp-pipeline in
WORKDIR /data

# Test snp_pipeline (code modified from Justin). Running copy_snppipeline_data.py generates an message the the script is deprecated
# but I figured I would leave it since the below commands test that the image runs properly.
FROM app as test
WORKDIR /test/
RUN cfsan_snp_pipeline data lambdaVirusInputs testLambdaVirus \
	&& cd testLambdaVirus \
	&& cfsan_snp_pipeline run -s samples reference/lambda_virus.fasta \
	&& copy_snppipeline_data.py lambdaVirusExpectedResults expectedResults \
	&& diff -q snplist.txt expectedResults/snplist.txt >> diffOutput.txt \
	&& diff -q snpma.fasta expectedResults/snpma.fasta >> diffOutput.txt \
	&& diff -q referenceSNP.fasta expectedResults/referenceSNP.fasta >> diffOutput.txt \
    && if [ -s diffOutput.txt ]; then echo "testLambdaVirus failed"; else echo "testLambdaVirus passed"; fi

WORKDIR /data