#!/bin/bash
# test for quast 5.0.2

docker run quast:5.0.2 quast.py --help

# this command runs the test since 'quast.py --test' alone doesn't work
docker run quast:5.0.2 /bin/bash -c 'cd /quast-5.0.2/; /quast-5.0.2/setup.py test'
