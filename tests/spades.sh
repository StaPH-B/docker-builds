#!/bin/bash
# test for spades container
set -e

docker run spades:3.13.0 spades.py
docker run spades:3.13.0 spades.py --test 
