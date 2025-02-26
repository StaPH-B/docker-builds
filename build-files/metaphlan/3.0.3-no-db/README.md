# MetaPhlAn3 docker image (without database already built in image)

Main tool: [MetaPhlAn/3.0](https://github.com/biobakery/MetaPhlAn/tree/3.0)

This docker image contains the  metaphlan3 program and its dependencies. It does not contain the metaphlan3 database, and the user will have to download the database to their machine, index the database, and mount to the Docker or Singularity container (see below).  

# Example: Downloading the database
```bash
# have to download database on your machine to run this image
# need to download the following files from metaphlan's dropbox or googledrive (see https://github.com/biobakery/MetaPhlAn/wiki/MetaPhlAn-3.0#installation). recommend putting them in their own directory, i.e. named "metaphlan_database"
# note, I ran into problems when downloading db from googledrive - the md5 didn't match, which resulted in empty bowtie2 build indices. dropbox downloads worked fine.
	# file_list.txt
	# mpa_latest
	# mpa_v30_CHOCOPhlAn_201901.tar (or whichever version of database you prefer)
	# mpa_v30_CHOCOPhlAn_201901_marker_info.txt.bz2
	# mpa_v30_CHOCOPhlAn_201901.md5

 
# extract database  
$ tar -xvf mpa_v30_CHOCOPhlAn_201901.tar  
$ bunzip2 mpa_v30_CHOCOPhlAn_201901.fna.bz2   
$ ls  
file_list.txt  
mpa_latest  
mpa_v30_CHOCOPhlAn_201901.fna  
mpa_v30_CHOCOPhlAn_201901_marker_info.txt.bz2  
mpa_v30_CHOCOPhlAn_201901.md5  
mpa_v30_CHOCOPhlAn_201901.pkl  
mpa_v30_CHOCOPhlAn_201901.tar  
````
After downloading the database, need to index the files using bowtie2 in the Docker or Singularity image (see examples below). As long as you keep the indexed database stored in your local machine, the bowtie2-build step only needs to be performed once. Then, can run metaphlan in Docker or Singularity (see examples below). 

## Example Usage: Docker

### Download Docker image:  
```bash
$ docker pull staphb/metaphlan:3.0.3-no-db
```
### Indexing database & running metaphlan in Docker:
```bash
# next, use bowtie2 to build and index the database. can use the metaphlan docker for this!  
# note this will take ~15 minutes
# change directory to directory with database files
$ cd ./metaphlan_database/  
$ docker run -v $PWD:/usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/ -u $(id -u):$(id -g) \
	--rm=True \
	staphb/metaphlan:3.0.3-no-db \ 
	bowtie2-build /usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/mpa_v30_CHOCOPhlAn_201901.fna /usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/mpa_v30_CHOCOPhlAn_201901
# after bowtie2-build completes, should have indexed files in your metaphlan_databases directory  
$ ls 
file_list.txt
mpa_latest  
mpa_v30_CHOCOPhlAn_201901.1.bt2  
mpa_v30_CHOCOPhlAn_201901.2.bt2  
mpa_v30_CHOCOPhlAn_201901.3.bt2  
mpa_v30_CHOCOPhlAn_201901.4.bt2  
mpa_v30_CHOCOPhlAn_201901.fna  
mpa_v30_CHOCOPhlAn_201901_marker_info.txt.bz2  
mpa_v30_CHOCOPhlAn_201901.md5  
mpa_v30_CHOCOPhlAn_201901.pkl  
mpa_v30_CHOCOPhlAn_201901.rev.1.bt2  
mpa_v30_CHOCOPhlAn_201901.rev.2.bt2  
mpa_v30_CHOCOPhlAn_201901.tar  

# to run metaphlan  
# for this example, stool metagenomes downloaded from SRA 
# if you have SRA toolkit, can do:  
$ fastq-dump --outdir ./data --skip-technical --readids --split-files --clip SRX2474191  
$ ls  
SRX2474191_1.fastq  

# in this example, 2  directories to mount: /data contains the .fastq and /metaphlan_database contains the  indexed database  
# check to make sure these 2 directories are in current working directory
$ ls
data  metaphlan_database

# run docker:
docker run  -v $PWD/metaphlan_database:/usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/ \
	-v $PWD/data:/data \
	-u $(id -u):$(id -g) \
	 --rm=True \
	staphb/metaphlan:3.0.3-no-db metaphlan /data/SRX2474191_1.fastq --input_type fastq -o profiled_metagenome.txt


# OUTPUT:  
WARNING: The metagenome profile contains clades that represent multiple species merged into a single representant.
An additional column listing the merged species is added to the MetaPhlAn output.  
$ head data/profiled_metagenome.txt    
#mpa_v30_CHOCOPhlAn_201901  
#/usr/local/bin/metaphlan /data/SRX2474191_1.fastq --input_type fastq -o profiled_metagenome.txt  
#SampleID	Metaphlan_Analysis  
#clade_name	NCBI_tax_id	relative_abundance	additional_species  
k__Bacteria	2	100.0	
k__Bacteria|p__Bacteroidetes	2|976	52.90346	
k__Bacteria|p__Firmicutes	2|1239	45.08223	
k__Bacteria|p__Actinobacteria	2|201174	2.01431	
k__Bacteria|p__Bacteroidetes|c__Bacteroidia	2|976|200643	52.90346	
k__Bacteria|p__Firmicutes|c__Clostridia	2|1239|186801	45.08223  

```

## Example usage: Singularity

### Build Singularity image

```bash
# build singularity image
$ singularity build ~/metaphlan-no-db-3.0.3.simg docker://staphb/metaphlan:3.0.3-no-db  
# last couple lines of OUTPUT:
INFO:    Creating SIF file...
INFO:    Build complete: /home/tgallagher/metaphlan-no-db-3.0.3.simg
```

### Index database and run metaphlan in Singularity 

```bash
# next, use bowtie2 to build and index the database. can use the metaphlan singularity for this!
# note this will take ~15 minutes
# change directory to directory with database files
$ cd ./metaphlan_database/ 
$ singularity exec --no-home -B  $PWD:/usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/ \
	/home/tgallagher/metaphlan-no-db-3.0.3.simg \
	bowtie2-build /usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/mpa_v30_CHOCOPhlAn_201901.fna \
	/usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/mpa_v30_CHOCOPhlAn_201901  

$ ls -l | awk '{print $5,"\t", $9'} #look at database index files and sizes
3526 	 file_list.txt
26 	 mpa_latest
629609227 	 mpa_v30_CHOCOPhlAn_201901.1.bt2
299330364 	 mpa_v30_CHOCOPhlAn_201901.2.bt2
10314872 	 mpa_v30_CHOCOPhlAn_201901.3.bt2
299330358 	 mpa_v30_CHOCOPhlAn_201901.4.bt2
1427036330 	 mpa_v30_CHOCOPhlAn_201901.fna
16175165 	 mpa_v30_CHOCOPhlAn_201901_marker_info.txt.bz2
64 	 mpa_v30_CHOCOPhlAn_201901.md5
25998762 	 mpa_v30_CHOCOPhlAn_201901.pkl
629609227 	 mpa_v30_CHOCOPhlAn_201901.rev.1.bt2
299330364 	 mpa_v30_CHOCOPhlAn_201901.rev.2.bt2
384430080 	 mpa_v30_CHOCOPhlAn_201901.tar

# to run metaphlan  
# for this example, stool metagenomes downloaded from SRA 
# if you have SRA toolkit, can do:  
$ fastq-dump --outdir ./data --skip-technical --readids --split-files --clip SRX2474191  
$ ls  
SRX2474191_1.fastq  

# in this example, 2  directories to mount: /data contains the .fastq and /metaphlan_database contains the  indexed database  
# check to make sure these 2 directories are in current working directory
$ ls
data  metaphlan_database

# run singularity:

$ singularity exec --no-home \
	-B $PWD/metaphlan_database:/usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/ \
	-B $PWD/data:/data \
	/home/tgallagher/metaphlan-no-db-3.0.3.simg \
	metaphlan /data/SRX2474191_1.fastq \
	 --input_type fastq -o /data/profiled_metagenome.txt

# OUTPUT:
WARNING: The metagenome profile contains clades that represent multiple species merged into a single representant.
An additional column listing the merged species is added to the MetaPhlAn output.
$ head data/profiled_metagenome.txt  
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

