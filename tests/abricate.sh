#!/bin/bash
# tests for abricate 1.0.0

# exit script with exit code=0 if any test fails
set -e

# this should spit out 'abricate #.#.#' and exit 0
docker run abricate:1.0.0 abricate --version

# test default db: ncbi
# expect 5 genes in results
docker run abricate:1.0.0 abricate /abricate-1.0.0/test/assembly.fa

# plasmidfinder: expect 2 genes 
docker run abricate:1.0.0 abricate --db plasmidfinder /abricate-1.0.0/test/assembly.fa

# vfdb: expect 0 genes, exit code should still be 0
docker run abricate:1.0.0 abricate --db vfdb /abricate-1.0.0/test/assembly.fa

# ecoh: expect 0 genes, exit code=0
docker run abricate:1.0.0 abricate --db ecoh /abricate-1.0.0/test/assembly.fa

# card: expect 4 genes
docker run abricate:1.0.0 abricate --db card /abricate-1.0.0/test/assembly.fa

# ecoli_vf: expect 0 genes, exit code=0
docker run abricate:1.0.0 abricate --db ecoli_vf /abricate-1.0.0/test/assembly.fa

# megares: expect 8 genes
docker run abricate:1.0.0 abricate --db megares /abricate-1.0.0/test/assembly.fa

# argannot: expect 5 genes
docker run abricate:1.0.0 abricate --db argannot /abricate-1.0.0/test/assembly.fa
