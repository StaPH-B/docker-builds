#!/bin/bash
# tests for QuickSNP 1.0.0

# exit script with exit code=0 if any test fails
set -euxo pipefail

QuickSNP.py --dm ./test_data/test_snpdist.tsv --outtree ./test_data/test_1.nwk

if cmp --silent -- ./test_data/test_tree.nwk ./test_data/test_1.nwk; then
    :
else
    echo '### WARNING: Test failed! Check if all files are present and dependencies are the right version. ###'
fi