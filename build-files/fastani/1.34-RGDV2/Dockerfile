## build RGDv2 ##
FROM staphb/ncbi-datasets:15.11.0 as stage

# copy in list of NCBI accessions and species list
COPY RGDv2-NCBI-assembly-accessions.txt /RGDv2/RGDv2-NCBI-assembly-accessions.txt
COPY RGDv2-NCBI-assembly-accessions-and-species.txt /RGDv2/RGDv2-NCBI-assembly-accessions-and-species.txt

# download RGD genomes using NCBI datasets tools; cleanup unneccessary files; 
# move and re-name assemblies to include Species in the filename
# make fasta files readable to all users; create File Of FileNames for all 43 assemblies (to be used with fastANI)
RUN for ID in $(cat /RGDv2/RGDv2-NCBI-assembly-accessions.txt); do \
 SPECIES=$(grep "${ID}" /RGDv2/RGDv2-NCBI-assembly-accessions-and-species.txt | cut -f 1) && \
 echo "downloading $ID, species "${SPECIES}", from NCBI..."; \
 datasets download genome accession ${ID} --filename ${ID}.zip; \
 unzip ${ID}.zip; \
 rm ${ID}.zip; \
 mv -v ncbi_dataset/data/${ID}/${ID}*.fna /RGDv2/${ID}.${SPECIES}.fasta; \
 rm -rfv ncbi_dataset/; \
 rm -v README.md; \
done && \
ls /RGDv2/*.fasta >/RGDv2/FOFN-RGDv2.txt &&\
chmod 664 /RGDv2/*

## App ##
FROM ubuntu:jammy as app

# for easy upgrade later. ARG variables only persist at build time
ARG FASTANI_VER="v1.34"

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1"
LABEL software="FastANI"
LABEL software.version=${FASTANI_VER}
LABEL description="Fast alignment-free computation of whole-genome Average Nucleotide Identity"
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL license="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"
LABEL maintainer="Kelsey Florek"
LABEL maintainer.email="kelsey.florek@slh.wisc.edu"
LABEL maintainer2="Curtis Kapsak"
LABEL maintainer2.email="kapsakcj@gmail.com"
LABEL maintainer3="Kutluhan Incekara"
LABEL maintainer3.email="kutluhan.incekara@ct.gov"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install --no-install-recommends -y \
 wget \
 unzip \
 libgomp1 && \
 apt-get clean && rm -rf /var/lib/apt/lists/*

# download pre-compiled binary; unzip; put binary in /usr/local/bin
# apt dependencies: libgomp1 unzip wget
RUN wget --no-check-certificate https://github.com/ParBLiSS/FastANI/releases/download/${FASTANI_VER}/fastANI-Linux64-${FASTANI_VER}.zip && \
 unzip fastANI-Linux64-${FASTANI_VER}.zip -d /usr/local/bin && \
 rm fastANI-Linux64-${FASTANI_VER}.zip
 
# copy RGDv2 from stage
COPY --from=stage /RGDv2/ /RGDv2/

# default run command
CMD fastANI -h

# singularity compatibility
ENV LC_ALL=C

# set working directory
WORKDIR /data

## Test ##
FROM app as test

# test against RGDv2
RUN wget --no-check-certificate -P /data https://github.com/ParBLiSS/FastANI/raw/master/tests/data/Escherichia_coli_str_K12_MG1655.fna && \
 fastANI -t 8 -q /data/Escherichia_coli_str_K12_MG1655.fna --rl /RGDv2/FOFN-RGDv2.txt -o fastANI.RGDv2.out.tsv &&\
 echo "output TSV from fastANI test:" && \
 cat fastANI.RGDv2.out.tsv 

