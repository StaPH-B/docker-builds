# MetaPhlAn3 docker image (without database already built in image)

Main tool: [MetaPhlAn](https://github.com/biobakery/MetaPhlAn/tree/3.0)

Additional tools:
- bowtie2

Full documentation: https://github.com/biobakery/biobakery/wiki/metaphlan2

> MetaPhlAn is a computational tool for profiling the composition of microbial communities (Bacteria, Archaea and Eukaryotes) from metagenomic shotgun sequencing data (i.e. not 16S) with species-level.

This docker image contains the  metaphlan3 program and its dependencies. It does not contain the metaphlan3 database, and the user will have to download the database to their machine, index the database, and mount to the Docker or Singularity container (see below).  

# Example Usage

Downloading the database
```
# have to download database on your machine to run this image
metaphlan --install --bowtie2db <database folder>
````

If installing the database externally, mount the database to `/usr/local/lib/python3.7/dist-packages/metaphlan/metaphlan_databases/`

Running metaphlan
```
metaphlan /data/SRX2474191_1.fastq --input_type fastq -o profiled_metagenome.txt

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
