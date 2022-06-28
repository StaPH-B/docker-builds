# blast+ container

Main tools:
- [blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

This is meant to assist in local blast searches. No blast databases will be maintained in this container. Be sure to mount your relevant Volumes with `--volumes` or `-v` when using the command line.


blast+ is actually a suite of tools. blast+ v.2.13.0 includes:
```
ls /ncbi-blast-2.13.0+/bin/
blast_formatter
blastdb_aliastool  
blastn      
blastx                      
deltablast             
legacy_blast.pl  
makeprofiledb  
rpstblastn  
tblastn_vdb        
windowmasker
blast_formatter_vdb  
blastdbcheck       
blastn_vdb  
cleanup-blastdb-volumes.py  
dustmasker             
makeblastdb      
psiblast       
segmasker   
tblastx
blast_vdb_cmd        
blastdbcmd         
blastp      
convert2blastmask           
makembindex      
rpsblast       
tblastn     
```
Currently not supported, but could be:

```
get_species_taxids.sh # requires E-direct
update_blastdb.pl     # requires perl
```

# Example Usage

```
# making a blast database
makeblastdb -dbtype nucl -in fasta.fa

# query
tblastn -query query.fasta -db fasta.fa -outfmt '6' -out blast_hits.txt
```

More documentation can be found at [https://www.ncbi.nlm.nih.gov/books/NBK569856/](https://www.ncbi.nlm.nih.gov/books/NBK569856/) and [https://www.ncbi.nlm.nih.gov/books/NBK279690/](https://www.ncbi.nlm.nih.gov/books/NBK279690/)
