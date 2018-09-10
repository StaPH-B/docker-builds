# base ubuntu image
FROM ubuntu:xenial

# run update and install wget
RUN apt-get update && apt-get install -y wget && apt-get clean

# download sra-toolkit
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz && tar -vxzf sratoolkit.2.9.2-ubuntu64.tar.gz && rm -r sratoolkit.2.9.2-ubuntu64.tar.gz

ENV PATH="/sratoolkit.2.9.2-ubuntu64/bin:$PATH"
