#/bin/bash

for file in */data/*/*.fna
do
    genus=$(head -n 1 $file   | sed 's/,//g' | sed 's/://g' | sed 's/\[//g' | sed 's/\]//g' | sed 's/\.//g' | sed 's/UNVERIFIED_ORG//g' | awk '{print $2}' )
    species=$(head -n 1 $file | sed 's/,//g' | sed 's/://g' | sed 's/\[//g' | sed 's/\]//g' | sed 's/\.//g' | sed 's/UNVERIFIED_ORG//g' | awk '{print $3}' )
    echo "The organism is $genus $species"
    accession=$(echo $file | cut -f 3 -d "/" )
    echo "The accession is $accession"
    gzip -c $file > prep/${genus}_${species}_${accession}.fna.gz
done
