#!/bin/bash
# test for metaphlan container
set -e

docker run metaphlan:3.0.3-no-db metaphlan --help 
