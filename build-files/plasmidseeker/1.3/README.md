# PlasmidSeeker Container  
Main tool: [PlasmidSeeker](https://github.com/bioinfo-ut/PlasmidSeeker)

A k-mer based program for the identification of known plasmids from bacterial whole genome sequencing reads

# Example Usage
```{bash}
# Identify Plasmids
plasmidseeker.pl -d db_w20 -i ERR1937840.fastq -b e_coli_sakai_ref.fna -o EC_1_results.txt

# Build custom database, with any multifatsa file of plasmids
database_builder.pl -i database.fastas
```
**WARNING!!!** You will need to make a database or download one of the databases provided on the [github page](https://github.com/bioinfo-ut/PlasmidSeeker).
You can also run this wget command: wget http://bioinfo.ut.ee/plasmidseeker/plasmidseeker_db_w20.tar.gz
Then you need to mount the container to with the directory with database. I used this docker command:
docker run -v `pwd`:`pwd` -w `pwd` -i -t plasmidseeker/john plasmidseeker.pl  -d /Users/johnarnn/Documents/plasmidseekerdb/db_w20  -i /Users/johnarnn/Documents/plasmidseeker/ERR1937840.fastq -b /Users/johnarnn/Documents/plasmidseeker/e_coli_sakai_ref.fna  -o EC_1_results.txt

Better documentation can be found at [PlasmidSeeker](https://github.com/bioinfo-ut/PlasmidSeeker)
