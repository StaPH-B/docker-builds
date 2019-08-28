#!/bin/bash
# test for samtools 1.9
set -e

docker run samtools:1.9 /bin/bash -c 'cd /samtools/samtools-1.9; make test'
