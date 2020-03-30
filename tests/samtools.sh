#!/bin/bash
# test for samtools 1.10
set -e

docker run samtools:1.10 /bin/bash -c 'cd /samtools/samtools-1.10; make test'
