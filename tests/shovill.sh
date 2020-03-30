#!/bin/bash
# test for Shovill 1.1.0
set -e

docker run shovill:1.1.0 /shovill/shovill-1.1.0/test/test.sh
