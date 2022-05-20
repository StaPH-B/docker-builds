#!/bin/bash

for i in NZ_AP018457.1 NZ_LC520274.1 NZ_CP051612.1
do
ID=`curl -X 'POST' \
  'https://ccb-microbe.cs.uni-saarland.de/plsdb/plasmids/api/fasta' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F "fastas=$i" | jq -r '.job_id'`

curl --output $i.gz  -X 'GET' \
  "https://ccb-microbe.cs.uni-saarland.de/plsdb/plasmids/api/fasta?job_id=$ID" \
  -H 'accept: text/html'

gzip -d $i.gz
done

cat NZ_AP018457.1 NZ_LC520274.1 NZ_CP051612.1 > database.fastas

database_builder.pl -i database.fastas

wget http://bioinfo.ut.ee/plasmidseeker/e_coli_sakai_ref.fna
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR193/000/ERR1937840/ERR1937840.fastq.gz

gzip -d ERR1937840.fastq.gz



plasmidseeker.pl -d plasmid_db -i ERR1937840.fastq -b e_coli_sakai_ref.fna -o EC_1_results.txt
