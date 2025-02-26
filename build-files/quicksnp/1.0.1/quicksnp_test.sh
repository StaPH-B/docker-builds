#!/bin/bash
# tests for QuickSNP 1.0.1

#Exit immediately if a command exits with a non-zero status
set -e

#Running QuickSNP 
QuickSNP.py --dm ./test_data/test_snpdist.tsv --outtree ./test_data/test_1.nwk

# Checking if the outputs match 
if cmp --silent -- ./test_data/test_tree.nwk ./test_data/test_1.nwk; then
    :
else
    echo '### WARNING: Test failed! Check if all files are present and dependencies are the right version. ###'
fi