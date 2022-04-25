# bedtools

This image implements the powerful toolset for genome arithmetic [bedtools](https://github.com/arq5x/bedtools2).
Documentation is available at https://bedtools.readthedocs.io/en/latest/. 

## Example usage
This example useage is adapted from the built-in tests for this image.

```bash
# Get data
wget -nv https://github.com/nf-core/test-datasets/raw/modules/data/genomics/sarscov2/illumina/bam/test.paired_end.sorted.bam

# Run program to calculate assembly coverage with 1-based coordinates
bedtools genomecov \
    -d \
    -ibam test.paired_end.sorted.bam > coverage.txt
```

## Example output

The results file from this command is:
```
coverage.txt  # a table of read coverage per genome position
```
