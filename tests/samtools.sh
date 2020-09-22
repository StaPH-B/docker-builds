#!/bin/bash
# test for samtools

samtoolsVer=1.11

set -e

docker run -e samtoolsVer=${samtoolsVer} samtools:${samtoolsVer} /bin/bash -c 'cd /samtools-${samtoolsVer}; make test'
