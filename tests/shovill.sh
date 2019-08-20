#!/bin/bash
# test for Shovill 1.0.4
set -e

docker run shovill:1.0.4 /shovill/shovill-1.0.4/test/test.sh
