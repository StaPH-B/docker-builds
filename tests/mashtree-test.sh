#!/bin/bash
# test for mashtree 
set -e
docker run mashtree:0.52 /bin/bash -c 'cd /mashtree-0.52 && perl Makefile.PL && make test'
