ARG PARSNP_VER="2.0.5"
ARG HARVEST_VER="1.3"

FROM ubuntu:jammy as builder

ARG PARSNP_VER
ARG HARVEST_VER

ARG RAXML_VER="8.2.12"
ARG FASTTREE_VER="2.1.11"
ARG MASH_VER="2.3"
ARG FASTANI_VER="1.34"

# Update package index, install packages (ParSNP basic dependencies and packages needed to build from source)
RUN apt-get update && apt-get install -y \
    autoconf \
    make \
    build-essential \
    capnproto \
    libcapnp-dev \
    libgsl0-dev \
    libprotobuf-dev \
    libssl-dev \
    libtool \
    protobuf-compiler \
    libsqlite3-dev \
    wget \
    zlib1g-dev \
    python3 \
    python3-pip \
    unzip

# Add /usr/lib to the library path so Mash and HarvestTools can find the capnp libraries
ENV LD_LIBRARY_PATH="/usr/lib:/usr/local/lib"

# Move some static libraries that Mash and HarvestTools demand to where they want to see them
RUN cp /usr/lib/x86_64-linux-gnu/libprotobuf.a /usr/lib/ && \
    cp /usr/lib/x86_64-linux-gnu/libcapnp.a /usr/lib/ && \
    cp /usr/lib/x86_64-linux-gnu/libkj.a /usr/lib/

RUN pip3 install numpy

# install fasttree
# ParSNP expects the FastTree executable to be called 'fasttree'
RUN wget -q http://www.microbesonline.org/fasttree/FastTree && \
    chmod +x FastTree && \
    mv FastTree /usr/local/bin/fasttree

# Install RAxML: https://cme.h-its.org/exelixis/resource/download/NewManual.pdf
RUN wget -q https://github.com/stamatak/standard-RAxML/archive/refs/tags/v$RAXML_VER.tar.gz && \
    tar -xvf v$RAXML_VER.tar.gz && \
    cd standard-RAxML-$RAXML_VER && \
    make -f Makefile.AVX.PTHREADS.gcc && \
    cp /standard-RAxML-$RAXML_VER/raxmlHPC-PTHREADS-AVX /usr/local/bin/raxmlHPC-PTHREADS

# Install Mash: https://github.com/marbl/Mash/blob/master/INSTALL.txt
RUN wget -q https://github.com/marbl/Mash/releases/download/v${MASH_VER}/mash-Linux64-v${MASH_VER}.tar && \
    tar -xf mash-Linux64-v${MASH_VER}.tar --no-same-owner && \
    rm -rf mash-Linux64-v${MASH_VER}.tar && \
    chown root:root /mash-Linux64-v${MASH_VER}/*

# Install PhiPack: https://www.maths.otago.ac.nz/~dbryant/software/phimanual.pdf
RUN wget -q https://www.maths.otago.ac.nz/~dbryant/software/PhiPack.tar.gz && \
    tar -xvf PhiPack.tar.gz && \
    cd /PhiPack/src && \
    make && \
    cp /PhiPack/Phi /usr/local/bin && \
    cp /PhiPack/Profile /usr/local/bin

# Install HarvestTools
RUN wget -q https://github.com/marbl/harvest-tools/releases/download/v${HARVEST_VER}/harvesttools-Linux64-v${HARVEST_VER}.tar.gz && \
    tar -vxf harvesttools-Linux64-v${HARVEST_VER}.tar.gz && \
    cp harvesttools-Linux64-v${HARVEST_VER}/harvesttools /usr/local/bin/.

# Install ParSNP
RUN wget -q https://github.com/marbl/parsnp/archive/v$PARSNP_VER.tar.gz && \
    tar -xvf v$PARSNP_VER.tar.gz && \
    rm v$PARSNP_VER.tar.gz && \
    cd /parsnp-$PARSNP_VER/muscle && \
    ./autogen.sh && \
    ./configure CXXFLAGS='-fopenmp' && \
    make install && \
    cd /parsnp-$PARSNP_VER && \
    ./autogen.sh && \
    export ORIGIN=\$ORIGIN && \
    ./configure LDFLAGS='-Wl,-rpath,$$ORIGIN/../muscle/lib' && \
    make LDADD=-lMUSCLE-3.7 && \
    make install

# install fastani
RUN wget -q https://github.com/ParBLiSS/FastANI/releases/download/v${FASTANI_VER}/fastANI-Linux64-v${FASTANI_VER}.zip && \
    unzip fastANI-Linux64-v${FASTANI_VER}.zip -d /usr/local/bin

FROM ubuntu:jammy as app

ARG PARSNP_VER
ARG HARVEST_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="ParSNP"
LABEL software.version="${PARSNP_VER}"
LABEL description="ParSNP: Rapid core genome multi-alignment."
LABEL documentation="https://harvest.readthedocs.io/en/latest/content/parsnp.html"
LABEL website="https://github.com/marbl/parsnp"
LABEL license="https://github.com/marbl/parsnp/blob/master/LICENSE"
LABEL maintainer="Erin Young"
LABEL maintainer.email="eriny@utah.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps \
    python3 \
    python3-pip \
    python-is-python3 \
    unzip \
    libgomp1 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Copy necessary packages into the production image
COPY --from=builder /parsnp-$PARSNP_VER/ /parsnp/
COPY --from=builder /usr/local/bin/* /usr/local/bin/
COPY --from=builder /usr/local/lib/* /usr/local/lib/

RUN pip install pyspoa numpy biopython tqdm

# Put harvesttools & parsnp in PATH and set LD_LIBRARY_PATH for MUSCLE
ENV PATH="/parsnp/:$PATH" \
    LD_LIBRARY_PATH="/usr/local/lib"

CMD parsnp -h

WORKDIR /data

FROM app as test

# IS_GITHUB only applicable for tests run by GitHub action
ARG IS_GITHUB

RUN parsnp -h

# negative control
WORKDIR /test/negative

RUN mkdir input_dir && \
    mkdir reference && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/703/365/GCA_000703365.1_Ec2011C-3609/GCA_000703365.1_Ec2011C-3609_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/766/575/GCA_016766575.1_PDT000040717.5/GCA_016766575.1_PDT000040717.5_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/748/565/GCA_000748565.2_ASM74856v2/GCA_000748565.2_ASM74856v2_genomic.fna.gz && \
    gunzip *.gz && \
    mv GCA_000703365.1_Ec2011C-3609_genomic.fna reference/. && \
    mv *fna input_dir && \
    parsnp -d input_dir -o filter --use-fasttree -v -r reference/GCA_000703365.1_Ec2011C-3609_genomic.fna

# positive control
WORKDIR /test/positive

RUN mkdir input_dir && \
    mkdir reference && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/703/365/GCA_000703365.1_Ec2011C-3609/GCA_000703365.1_Ec2011C-3609_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/766/575/GCA_016766575.1_PDT000040717.5/GCA_016766575.1_PDT000040717.5_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/003/018/935/GCA_003018935.1_ASM301893v1/GCA_003018935.1_ASM301893v1_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/830/055/GCA_012830055.1_PDT000040719.3/GCA_012830055.1_PDT000040719.3_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/829/335/GCA_012829335.1_PDT000040724.3/GCA_012829335.1_PDT000040724.3_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/003/018/775/GCA_003018775.1_ASM301877v1/GCA_003018775.1_ASM301877v1_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/829/275/GCA_012829275.1_PDT000040726.3/GCA_012829275.1_PDT000040726.3_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/016/766/555/GCA_016766555.1_PDT000040728.5/GCA_016766555.1_PDT000040728.5_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/829/195/GCA_012829195.1_PDT000040729.3/GCA_012829195.1_PDT000040729.3_genomic.fna.gz && \
    wget -q https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/012/829/295/GCA_012829295.1_PDT000040727.3/GCA_012829295.1_PDT000040727.3_genomic.fna.gz && \
    gunzip *.gz && \
    mv GCA_000703365.1_Ec2011C-3609_genomic.fna reference/. && \
    mv *.fna input_dir/. && \
    parsnp -d input_dir -o outdir_parsnp_raxml -v -c -r reference/GCA_000703365.1_Ec2011C-3609_genomic.fna && \
    parsnp -d input_dir -o outdir_parsnp_fasttree --use-fasttree -v -c -r reference/GCA_000703365.1_Ec2011C-3609_genomic.fna && \
    harvesttools -i outdir_parsnp_fasttree/parsnp.ggr -S outdir_parsnp_fasttree/snp_alignment.txt && \
    harvesttools -i outdir_parsnp_raxml/parsnp.ggr -S outdir_parsnp_raxml/snp_alignment.txt
