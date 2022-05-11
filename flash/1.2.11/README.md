# FLASH

This image implements the software [FLASH](http://ccb.jhu.edu/software/FLASH) for merging overlapping paired-end reads.
Documentation is available at http://ccb.jhu.edu/software/FLASH/MANUAL.

## Example usage
This example useage is adapted from the built-in tests for this image. See [test_flash.sh](test_flash.sh).

```bash
# Get input data (paired-end reads)
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz -O R2.fastq.gz

# Define a sensible minimum overlap for merging based on your read lengths
OVERLAP_LEN=100
# Define read length, will use this to define the maximum overlap
READ_LEN=126

# Run FLASH to merge overlapping reads
flash \
  R1.fastq.gz R2.fastq.gz \
  --min-overlap=$OVERLAP_LEN \
  --max-overlap=$READ_LEN \
  --output-prefix=test \
  --output-directory=results
```

## Example output

The on-screen output tells you the parameters FLASH ran with and how many read pairs it combined:
```
[FLASH] Starting FLASH v1.2.11
[FLASH] Fast Length Adjustment of SHort reads
[FLASH]  
[FLASH] Input files:
[FLASH]     R1.fastq.gz
[FLASH]     R2.fastq.gz
[FLASH]  
[FLASH] Output files:
[FLASH]     results/test.extendedFrags.fastq
[FLASH]     results/test.notCombined_1.fastq
[FLASH]     results/test.notCombined_2.fastq
[FLASH]     results/test.hist
[FLASH]     results/test.histogram
[FLASH]  
[FLASH] Parameters:
[FLASH]     Min overlap:           100
[FLASH]     Max overlap:           126
[FLASH]     Max mismatch density:  0.250000
[FLASH]     Allow "outie" pairs:   false
[FLASH]     Cap mismatch quals:    false
[FLASH]     Combiner threads:      2
[FLASH]     Input format:          FASTQ, phred_offset=33
[FLASH]     Output format:         FASTQ, phred_offset=33
[FLASH]  
[FLASH] Starting reader and writer threads
[FLASH] Starting 2 combiner threads
[FLASH] Processed 25000 read pairs
[FLASH] Processed 50000 read pairs
[FLASH]  
[FLASH] Read combination statistics:
[FLASH]     Total pairs:      50000
[FLASH]     Combined pairs:   5
[FLASH]     Uncombined pairs: 49995
[FLASH]     Percent combined: 0.01%
[FLASH]  
[FLASH] Writing histogram files.
[FLASH]  
[FLASH] FLASH v1.2.11 complete!
[FLASH] 0.213 seconds elapsed
```

The result files from this command are:
```
test.extendedFrags.fastq
test.notCombined_1.fastq
test.notCombined_2.fastq
test.hist
test.histogram
```
