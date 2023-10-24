# blast+ container

Main tools:

- [blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

This is meant to assist in local blast searches. No blast databases will be maintained in this container. Be sure to mount your relevant Volumes with `--volumes` or `-v` when using the command line.

blast+ is actually a suite of tools. blast+ v.2.14.1 includes:

```bash
$ ls /ncbi-blast-2.14.1+/bin
blast_formatter
blast_formatter_vdb
blast_vdb_cmd
blastdb_aliastool
blastdbcheck
blastdbcmd
blastn
blastn_vdb
blastp
blastx
cleanup-blastdb-volumes.py
convert2blastmask
deltablast
dustmasker
get_species_taxids.sh
legacy_blast.pl
makeblastdb
makembindex
makeprofiledb
psiblast
rpsblast
rpstblastn
segmasker
tblastn
tblastn_vdb
tblastx
update_blastdb.pl
windowmasker 
```

Currently not supported, but could be:

```bash
get_species_taxids.sh # requires E-direct
update_blastdb.pl     # requires perl
```

## Example Usage

```bash
# making a blast database
makeblastdb -dbtype nucl -in fasta.fa

# query
tblastn -query query.fasta -db fasta.fa -outfmt '6' -out blast_hits.txt
```

More documentation can be found at [https://www.ncbi.nlm.nih.gov/books/NBK569856/](https://www.ncbi.nlm.nih.gov/books/NBK569856/) and [https://www.ncbi.nlm.nih.gov/books/NBK279690/](https://www.ncbi.nlm.nih.gov/books/NBK279690/)
