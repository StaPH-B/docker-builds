#!/bin/bash
# test for mashtree 
set -e
docker run mashtree:1.2.0 /bin/bash -c 'cd /mashtree-1.2.0 && perl Makefile.PL && make test'
