# Plasmidfinder Container

Main tool: [Plasmidfinder](https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/)

Additional tools:
- kma : 1.3.28
- blast : 2.12.0
- plasmidfinder_db : commit hash 4add282963c788762cdc3c6e91eb46c3d109f19b

The PlasmidFinder service contains one python script plasmidfinder.py which is the script of the latest version of the PlasmidFinder service. The service identifies plasmids in total or partial sequenced isolates of bacteria.

# Example Usage
```{bash}
plasmidfinder.py -i ERR1937840.fastq -o test
```

Better documentation can be found at [Plasmidfinder](https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/)
