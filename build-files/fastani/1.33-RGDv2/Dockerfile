FROM ubuntu:focal as app

# for easy upgrade later. ARG variables only persist at build time
ARG FASTANI_VER="v1.33"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="FastANI"
LABEL software.version="${FASTANI_VER}"
LABEL description="Fast alignment-free computation of whole-genome Average Nucleotide Identity"
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL license="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"
LABEL maintainer1="Kelsey Florek"
LABEL maintainer1.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"

# to prevent tzdata from asking for a region during apt updates; ARG so that variable only 
# persists at buildtime
ARG DEBIAN_FRONTEND=noninteractive

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y wget \
 unzip \
 libgomp1 && \
 apt-get clean && rm -rf /var/lib/apt/lists/*

# download pre-compiled binary; unzip; put binary in /usr/bin; make /data
# apt dependencies: libgomp1 unzip wget
RUN wget https://github.com/ParBLiSS/FastANI/releases/download/${FASTANI_VER}/fastANI-Linux64-${FASTANI_VER}.zip && \
 unzip fastANI-Linux64-${FASTANI_VER}.zip -d /usr/bin && \
 rm fastANI-Linux64-${FASTANI_VER}.zip && \
 mkdir /data

# install ncbi datasets tool (pre-compiled binary); place in $PATH
RUN wget https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/LATEST/linux-amd64/datasets && \
 chmod +x datasets && \
 mv -v datasets /usr/local/bin

# copy in list of NCBI accessions and species list
COPY RGDv2-NCBI-assembly-accessions.txt /RGDv2/RGDv2-NCBI-assembly-accessions.txt
COPY RGDv2-NCBI-assembly-accessions-and-species.txt /RGDv2/RGDv2-NCBI-assembly-accessions-and-species.txt

# download RGD genomes using NCBI datasets tools; cleanup unneccessary files; 
# move and re-name assemblies to include Species in the filename
# make fasta files readable to all users; create File Of FileNames for all 43 assemblies (to be used with fastANI)
RUN for ID in $(cat /RGDv2/RGDv2-NCBI-assembly-accessions.txt); do \
 SPECIES=$(grep "${ID}" /RGDv2/RGDv2-NCBI-assembly-accessions-and-species.txt | cut -f 1) && \
 echo "downloading $ID, species "${SPECIES}", from NCBI..."; \
 datasets download genome accession --filename ${ID}.zip ${ID}; \
 unzip ${ID}.zip; \
 rm ${ID}.zip; \
 mv -v ncbi_dataset/data/${ID}/${ID}*.fna /RGDv2/${ID}.${SPECIES}.fasta; \
 rm -rfv ncbi_dataset/; \
 rm -v README.md; \
done && \
ls /RGDv2/*.fasta >/RGDv2/FOFN-RGDv2.txt && \
chmod 664 /RGDv2/*

# set working directory
WORKDIR /data

# for singularity compatibility
ENV LC_ALL=C

# test layer here
FROM app as test

# download 2 genomes from fastANI GitHub; compare the 2; cat the output file
RUN wget -P /data https://github.com/ParBLiSS/FastANI/raw/master/data/Escherichia_coli_str_K12_MG1655.fna && \
 wget -P /data https://github.com/ParBLiSS/FastANI/raw/master/data/Shigella_flexneri_2a_01.fna && \
 fastANI -q /data/Shigella_flexneri_2a_01.fna -r /data/Escherichia_coli_str_K12_MG1655.fna -o /data/fastANI-test-ShiglellaFlexneri-EcoliK12.tsv && \
 echo "output TSV from fastANI test:" && \
 cat fastANI-test-ShiglellaFlexneri-EcoliK12.tsv