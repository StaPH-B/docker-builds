#!/bin/bash
# test for ariba container
set -e

docker run ariba:2.14.4 ariba
docker run ariba:2.14.4 ariba test test-outdir/
