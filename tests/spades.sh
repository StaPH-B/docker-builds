#!/bin/bash
# test for spades container
set -e

docker run spades:3.15.2 spades.py
docker run spades:3.15.2 spades.py --test 
