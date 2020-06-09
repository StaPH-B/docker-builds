#!/bin/bash
# test for mashtree 
set -e
docker run mashtree:1.0.4 /bin/bash -c 'cd /mashtree-1.0.4 && perl Makefile.PL && make test'
