##### Building stage #####

# Stage 1: Build Python environment with required packages
FROM python:3.8-slim AS app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Add metadata
LABEL authors="CDC PolkaPox Team"
LABEL description="Container used in the PolkaPox pipeline by graph_reconstruct.nf module"
LABEL base.image="python:3.8-slim"
LABEL dockerfile.version="1.0"
LABEL website="https://github.com/CDCgov/polkapox"
LABEL license="https://github.com/CDCgov/polkapox/blob/master/LICENSE"

# Install required system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libopenblas-dev \
    wget \
    procps

# Install Python packages
RUN pip install --no-cache-dir \
    biopython==1.83 \
    numpy==1.24.4 \
    mkl==2024.0.0 \
    networkx==3.1 \
    gfapy==1.2.3

# Stage 2: Build the final (lightweight) image 
FROM python:3.8-slim

# Copy only the necessary files from the builder stage
COPY --from=app /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=app /usr/local/bin /usr/local/bin
COPY --from=app /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu
COPY --from=app /usr/bin/wget /usr/bin/wget

RUN echo "Original path: ${PATH}"

# Set environment variables
ENV PATH="/usr/local/bin:${PATH}"

# Set a work dir for the Blast+ install
WORKDIR /src

# Install NCBI BLAST+
ARG BLAST_VER=2.15.0

RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLAST_VER}/ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 tar -xzf ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 rm ncbi-blast-${BLAST_VER}+-x64-linux.tar.gz && \
 mkdir /data

# Add blast executable to path
ENV PATH="/src/ncbi-blast-${BLAST_VER}+/bin:${PATH}" \
    LC_ALL=C

# Set the working directory
WORKDIR /data

# Set the default command
CMD ["bash"]

###### Testing Stage ######
RUN blastn -version
