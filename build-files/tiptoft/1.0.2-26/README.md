# tiptoft container
Main tool: [tiptoft](https://github.com/andrewjpage/tiptoft)

Code repository: https://github.com/andrewjpage/tiptoft

Additional tools as listed by pip freeze:
- biopython: 1.79
- pyfastaq: 3.17.0
- cython: 3.0.12
- numpy: 1.19.5

Basic information on how to use this tool:
- executable: `tiptoft`
- help: `--help`
- version: `--version`
- description: Predict plasmids from uncorrected long read data

Additional information:
This container includes a pre-downloaded plasmid database. Use `tiptoft_database_downloader` to download the latest PlasmidFinder database. The database downloader uses the [PlasmidFinder Bitbucket repository](https://bitbucket.org/genomicepidemiology/plasmidfinder_db). 
* AJ Page, T Seemann (2019). TipToft: detecting plasmids contained in uncorrected long read sequencing data. Journal of Open Source Software, 4(35), 1021, https://doi.org/10.21105/joss.01021
* Carattoli et al, In Silico Detection and Typing of Plasmids using PlasmidFinder and Plasmid Multilocus Sequence Typing, Antimicrob Agents Chemother. 2014;58(7):3895–3903. 
* Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL. BLAST+: architecture and applications. BMC Bioinformatics 2009; 10:421.
* Clausen PTLC, Aarestrup FM, Lund O. Rapid and precise alignment of raw reads against redundant databases with KMA. BMC Bioinformatics 2018; 19:307.

Full documentation: [https://github.com/andrewjpage/tiptoft/blob/master/docs/USER_GUIDE.md](https://github.com/andrewjpage/tiptoft/blob/master/docs/USER_GUIDE.md)

## Example Usage
### Download the plasmid database
```bash
tiptoft_database_downloader tiptoftDB_name
```

### Run tiptoft with the downloaded database
```bash
tiptoft -d tiptoftDB_name.fa ERS654932_plasmids.fastq.gz
```
### Run tiptoft with the built-in database
```bash
tiptoft ERS654932_plasmids.fastq.gz
```