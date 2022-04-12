# MetaPhlAn3 docker image  

Main tool: [MetaPhlAn/3.0](https://github.com/biobakery/MetaPhlAn/tree/3.0)  

This docker image contains the metaphlan3 database along with the metaphlan3 program and its dependencies. Specifically, the database is a ~1.1M unique clade-specific marker genes from ~100,000 reference genomes (~99,500 bacterial and archaeal and ~500 eukaryotic). The database can be found on Metaphlan3's github (https://github.com/biobakery/MetaPhlAn/tree/3.0). To build this image, the database was downloaded on Oct 16 2020.  

Please note the size of this docker image with the metaphlan3 database is ~3.6 GB. If downloading this image fails or takes too long, consider using the docker image version without the metaphlan 3 database:  
  * docker image name and tag: `staphb/metaphlan:3.0.3-no-db` https://hub.docker.com/r/staphb/metaphlan/tags. Instructions for downloading databse are in the 3.0.3-no-db/README

## Example Usage: running metaphlan in Docker  

```bash
 
# Download docker image:  
$ docker pull staphb/metaphlan:3.0.3  

# for this example, stool metagenomes downloaded from SRA  
# if you have SRA toolkit, can do:
$ fastq-dump --outdir . --skip-technical --readids --split-files --clip SRX2474191  
$ ls  
SRX2474191_1.fastq  

# run metaphlan3 via docker, mount $PWD (make sure your current dir has data) to /data in the container  
docker run --rm -u $(id -u):$(id -g) -v $PWD:/data staphb/metaphlan:3.0.3 \   
	metaphlan SRX2474191_1.fastq --input_type fastq -o profiled_metagenome.txt  

# OUTPUT:  
WARNING: The metagenome profile contains clades that represent multiple species merged into a single representant.
An additional column listing the merged species is added to the MetaPhlAn output.  
$ head profiled_metagenome.txt  
#mpa_v30_CHOCOPhlAn_201901  
#/usr/local/bin/metaphlan SRX2474191_1.fastq --input_type fastq -o profiled_metagenome.txt  
#SampleID	Metaphlan_Analysis  
#clade_name	NCBI_tax_id	relative_abundance	additional_species  
k__Bacteria	2	100.0	
k__Bacteria|p__Bacteroidetes	2|976	52.90346	
k__Bacteria|p__Firmicutes	2|1239	45.08223	
k__Bacteria|p__Actinobacteria	2|201174	2.01431	 
k__Bacteria|p__Bacteroidetes|c__Bacteroidia	2|976|200643	52.90346  	
k__Bacteria|p__Firmicutes|c__Clostridia	2|1239|186801	45.08223  

```



## Example usage: running metaphlan in Singularity

```bash
# build singularity image
$ singularity build ~/metaphlan-3.0.3.simg docker://staphb/metaphlan:3.0.3  
# last couple lines of OUTPUT:
INFO:    Creating SIF file...
INFO:    Build complete: /home/tgallagher/metaphlan-3.0.3.simg

# to run metaphlan  
# for this example, stool metagenomes downloaded from SRA 
# if you have SRA toolkit, can do:  
$ fastq-dump --outdir ./data --skip-technical --readids --split-files --clip SRX2474191  
$ ls  
SRX2474191_1.fastq  

# run singularity, mount $PWD (make sure your current dir has data) to /data in the container
$ singularity exec --no-home \
	-B $PWD:/data \
	/home/tgallagher/metaphlan-3.0.3.simg \
	metaphlan /data/SRX2474191_1.fastq \
	 --input_type fastq -o /data/profiled_metagenome.txt

# OUTPUT:
WARNING: The metagenome profile contains clades that represent multiple species merged into a single representant.
An additional column listing the merged species is added to the MetaPhlAn output.
$ head profiled_metagenome.txt  
#mpa_v30_CHOCOPhlAn_201901
#/usr/local/bin/metaphlan /data/SRX2474191_1.fastq --input_type fastq -o /data/profiled_metagenome.txt
#SampleID	Metaphlan_Analysis
#clade_name	NCBI_tax_id	relative_abundance	additional_species
k__Bacteria	2	100.0	
k__Bacteria|p__Bacteroidetes	2|976	52.90346	
k__Bacteria|p__Firmicutes	2|1239	45.08223	
k__Bacteria|p__Actinobacteria	2|201174	2.01431	
k__Bacteria|p__Bacteroidetes|c__Bacteroidia	2|976|200643	52.90346	
k__Bacteria|p__Firmicutes|c__Clostridia	2|1239|186801	45.08223

```
