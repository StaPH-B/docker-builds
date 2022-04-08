#!/bin/bash

ABRICATE_VER=$1
echo $ABRICATE_VER

if [ "$(abricate --version | awk '{print $2}')" != "$ABRICATE_VER" ] ; then echo "version didn't match" ; exit 100 ; fi

# expects 5 genes
if [ "$(abricate /abricate-1.0.0/test/assembly.fa | wc -l)" != "6" ] ; then echo "genes didn't match" ; exit 200 ; fi
# expects 2 genes
if [ "$(abricate --db plasmidfinder /abricate-1.0.0/test/assembly.fa | wc -l)" != "3" ] ; then echo "genes didn't match" ; exit 300 ; fi
# expects 0 genes
if [ -z "$(abricate --db vfdb /abricate-1.0.0/test/assembly.fa | wc -l )" ] ; then echo "genes didn't match" ; exit 400 ; fi
# expects 0 genes
if [ -z "$(abricate --db ecoh /abricate-1.0.0/test/assembly.fa | wc -l )" ] ; then echo "genes didn't match" ; exit 500 ; fi
# expects 4 genes
if [ "$(abricate --db card /abricate-1.0.0/test/assembly.fa | wc -l )" != "5" ]  ; then echo "genes didn't match" ; exit 600 ; fi
# expects 0 genes
if [ -z "$(abricate --db ecoli_vf /abricate-1.0.0/test/assembly.fa | wc -l )" ]  ; then echo "genes didn't match" ; exit 700 ; fi
#expects 8 genes
if [ "$(abricate --db megares /abricate-1.0.0/test/assembly.fa | wc -l )" != "9" ]  ; then echo "genes didn't match" ; exit 800 ; fi
# expects 5 genes
if [ "$(abricate --db argannot /abricate-1.0.0/test/assembly.fa | wc -l )" != "6" ]  ; then echo "genes didn't match" ; exit 900 ; fi
