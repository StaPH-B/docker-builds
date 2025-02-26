# ResFinder 4.1.11 container

Main tool : [ResFinder](https://bitbucket.org/genomicepidemiology/resfinder/src/master/)

Additional tools:

- kma 1.4.3
- ResFinder database
- PointFinder database

Alternatively available as a webtool here: https://cge.cbs.dtu.dk/services/ResFinder/

Full documentation: https://bitbucket.org/genomicepidemiology/resfinder/src/master/

ResFinder identifies acquired genes and/or finds chromosomal mutations mediating antimicrobial resistance in total or partial DNA sequence of bacteria.

The databases included are pinned to a specific git commit hash, since the databases are not clearly versioned.

- ResFinder database [git commit bfa1754 from 2022-04-22](https://bitbucket.org/genomicepidemiology/pointfinder_db/commits/bfa17543d776faf3962ba1e824dec5f55a66d73b)
- PointFinder database [using git commit a4cc8bc from 2022-07-19](https://bitbucket.org/genomicepidemiology/resfinder_db/commits/a4cc8bc1e969b3829ad0f0bd4a6cadf615ac9f21)

## Example Usage

```bash
# run ResFinder on raw reads (FASTQs)
run_resfinder.py -ifq /data/sample_1.fastq /data/sample_2.fastq \
    -o /data/resfinder-results-fastq-input \
    -acq -l 0.9 -t 0.9 \
    -c -s "Escherichia coli"

# run ResFinder on assembly FASTA
run_resfinder.py -ifa /data/sample.fasta \
    -o /data/resfinder-results-fasta-input \
    -c \
    -acq -l 0.9 -t 0.9 \
    --species "Escherichia coli" \
```
