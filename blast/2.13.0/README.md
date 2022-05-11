# blast+ container

Main tools:
- [blast+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

This is meant to assist in local blast searches. No blast databases will be maintained in this container. Be sure to mount your relevant Volumes with `--volumes` or `-v` when using the command line.

# Example Usage

```
# making a blast database
makeblastdb makeblastdb -dbtype nucl -in fasta.fa

# query
tblastn -query query.fasta -db fasta.fa -outfmt '6' -out blast_hits.txt
```

More documentation can be found at [https://www.ncbi.nlm.nih.gov/books/NBK569856/](https://www.ncbi.nlm.nih.gov/books/NBK569856/) and [https://www.ncbi.nlm.nih.gov/books/NBK279690/](https://www.ncbi.nlm.nih.gov/books/NBK279690/)
