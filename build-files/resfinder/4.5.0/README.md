# ResFinder container

Main tool : [ResFinder](https://bitbucket.org/genomicepidemiology/resfinder/src/master/)

Additional tools:

- kma 1.4.14
- ResFinder database 2.3.1
- PointFinder database 4.1.0
- disinfinder database 2.0.1

Alternatively available as a webtool here: https://cge.cbs.dtu.dk/services/ResFinder/

Full documentation: https://bitbucket.org/genomicepidemiology/resfinder/src/master/

ResFinder identifies acquired genes and/or finds chromosomal mutations mediating antimicrobial resistance in total or partial DNA sequence of bacteria.

WARNING : The executable has changed!

## Example Usage

```bash
# run ResFinder on raw reads (FASTQs)
python3 -m resfinder -ifq /data/sample_1.fastq /data/sample_2.fastq \
    -o /data/resfinder-results-fastq-input \
    -acq -l 0.9 -t 0.9 \
    -c -s "Escherichia coli"

# run ResFinder on assembly FASTA
python3 -m resfinder -ifa /data/sample.fasta \
    -o /data/resfinder-results-fasta-input \
    -c \
    -acq -l 0.9 -t 0.9 \
    --species "Escherichia coli" \
```
