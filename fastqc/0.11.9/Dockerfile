ARG FASTQC_VER="0.11.9"

# FROM defines the base docker image. 
# The 'as' keyword lets you name the following stage. We use `app` for the production image

FROM ubuntu:bionic as app

#re-instantiate these variables
ARG FASTQC_VER

# metadata
LABEL base.image="ubuntu:bionic"
LABEL dockerfile.version="2"
LABEL software="FASTQC"
LABEL software.version="0.11.9"
LABEL description="A quality control analysis tool for high throughput sequencing data"
LABEL website="https://www.bioinformatics.babraham.ac.uk/projects/fastqc/"
LABEL license="https://github.com/s-andrews/FastQC/blob/master/LICENSE.txt"
LABEL maintainer1="Abigail Shockey"
LABEL maintainer1.email="abigail.shockey@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="pjx8@cdc.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip \
    wget \
    perl \
    default-jre && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install fastqc. Make /data for use as a working dir
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQC_VER}.zip && \
    unzip fastqc_v${FASTQC_VER}.zip && \
    rm fastqc_v${FASTQC_VER}.zip && \
    chmod +x FastQC/fastqc && \
    mkdir /data

# set PATH and working directory
ENV PATH="${PATH}:/FastQC/"
WORKDIR /data

#######TESTING - Getting Test Data################
# getting fastq files with SRA tools - input data
FROM ncbi/sra-tools:3.0.1 as fastq

WORKDIR /fastq_test

RUN fasterq-dump --threads 4 -A SRR6082043 && \
    gzip *.fastq && \
    mv SRR6082043_1.fastq.gz test_1.fastq.gz && mv SRR6082043_2.fastq.gz test_2.fastq.gz

# running a 'test' in the 'test' stage
FROM app as test

#re-instantiate these variables
ARG FASTQC_VER

# Getting test output data. Just a note, it is not possible to compare the HTML files directly as the report includes a date of run.
# Files are available if someone wants to verify the outputs externally or write another test.
RUN wget -P /test/data https://raw.githubusercontent.com/poojasgupta/docker-builds/master/fastqc/0.11.9/tests/test_1_fastqc.html && \
 wget -P /test/data https://raw.githubusercontent.com/poojasgupta/docker-builds/master/fastqc/0.11.9/tests/test_1_fastqc.zip && \
 wget -P /test/data https://raw.githubusercontent.com/poojasgupta/docker-builds/master/fastqc/0.11.9/tests/test_2_fastqc.html && \
 wget -P /test/data https://raw.githubusercontent.com/poojasgupta/docker-builds/master/fastqc/0.11.9/tests/test_2_fastqc.zip

# set working directory
WORKDIR /test

COPY --from=fastq /fastq_test/test*fastq.gz /test/

#Test layer
#test reads as input
RUN echo "Running FastQC with the test fastq files"
RUN fastqc test_1.fastq.gz test_2.fastq.gz -o .

# Check validity of outputs. The expected number of sequences should be '669558' in both the fastq files.
# If the test output is different, something went wrong.
RUN  grep -q "Total Sequences</td><td>669558" /test/test_1_fastqc.html && \
grep -q "Total Sequences</td><td>669558" /test/test_2_fastqc.html && \
echo "Your test worked successfully!"

# print version and help options
RUN fastqc --version && \
    fastqc --help