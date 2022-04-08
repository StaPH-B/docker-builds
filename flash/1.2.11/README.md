# FLASH container

Main tool : [FLASH](http://ccb.jhu.edu/software/FLASH)

Full documentation: http://ccb.jhu.edu/software/FLASH/MANUAL

This image implements the software [FLASH](http://ccb.jhu.edu/software/FLASH) for merging overlapping paired-end reads.

## Example usage
This example useage is adapted from the built-in tests for this image. See [run_flash_pos_control.sh](tests/scripts/run_flash_pos_control.sh).

```bash
# Input data are paired-end reads
R1=/data/R1.fastq.gz
R2=/data/R2.fastq.gz

# Set up an output directory
OUTDIR=/test_result
mkdir -p $OUTDIR

# Define a sensible minimum overlap for merging based on your read lengths
OVERLAP_LEN=240
# Define read length, will use this to define the maximum overlap
READ_LEN=300

# Run FLASH to merge overlapping reads
flash \
  $R1 $R2 \
  --min-overlap=$OVERLAP_LEN \
  --max-overlap=$READ_LEN \
  --output-prefix=test \
  --output-directory=$OUTDIR
```

## Example output

The on-screen output tells you the parameters FLASH ran with and how many read pairs it combined:
```
[FLASH] Starting FLASH v1.2.11
[FLASH] Fast Length Adjustment of SHort reads
[FLASH]  
[FLASH] Input files:
[FLASH]     /data/R1.fastq.gz
[FLASH]     /data/R2.fastq.gz
[FLASH]  
[FLASH] Output files:
[FLASH]     /test_result/test.extendedFrags.fastq
[FLASH]     /test_result/test.notCombined_1.fastq
[FLASH]     /test_result/test.notCombined_2.fastq
[FLASH]     /test_result/test.hist
[FLASH]     /test_result/test.histogram
[FLASH]  
[FLASH] Parameters:
[FLASH]     Min overlap:           240
[FLASH]     Max overlap:           300
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
...
[FLASH] Processed 830228 read pairs
[FLASH]  
[FLASH] Read combination statistics:
[FLASH]     Total pairs:      830228
[FLASH]     Combined pairs:   81862
[FLASH]     Uncombined pairs: 748366
[FLASH]     Percent combined: 9.86%
[FLASH]  
[FLASH] Writing histogram files.
[FLASH]  
[FLASH] FLASH v1.2.11 complete!
[FLASH] 22.683 seconds elapsed
```

The result files from this command are:
```
test.extendedFrags.fastq
test.notCombined_1.fastq
test.notCombined_2.fastq
test.hist
test.histogram
```
