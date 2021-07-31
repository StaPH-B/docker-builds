#!/bin/bash
# test for spades container
set -e

docker run spades:3.14.1 spades.py
docker run spades:3.14.1 spades.py --test 
