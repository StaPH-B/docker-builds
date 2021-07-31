#!/bin/bash
# test for quast 5.0.2
set -e

docker run ivar:1.2.2_artic20200528 ivar version
docker run ivar:1.2.2_artic20200528 /bin/bash -c 'cd /root/ivar-1.2.2 && make check'
