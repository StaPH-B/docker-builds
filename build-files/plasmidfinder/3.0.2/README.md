# Plasmidfinder Container

Main tool: [Plasmidfinder](https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/)

Additional tools:
- kma : 1.6.4
- blast : 2.12.0
- plasmidfinder_db : 2.2.0

The PlasmidFinder service contains one python script plasmidfinder.py which is the script of the latest version of the PlasmidFinder service. The service identifies plasmids in total or partial sequenced isolates of bacteria.

# Example Usage
```{bash}
python -m plasmidfinder -i ERR1937840.fastq -o test
```

Better documentation can be found at [Plasmidfinder](https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/)
