# emmtyper container

Main tool : [emmtyper](https://github.com/MDU-PHL/emmtyper)
  
Code repository: [emmtyper](https://github.com/MDU-PHL/emmtyper)

Additional tools:
- [Daniel-VM/cdc-utilities](https://github.com/Daniel-VM/cdc-utilities): c0d1c26625cfe9ac458306089358dc26edad06f0

Basic information on how to use this tool:
- executable: emmtyper
- help: --help
- version: --version
- description: |
    'emmtyper' is a command line tool for emm-typing of _Streptococcus pyogenes_ using a _de novo_ or complete assembly.

Additional information:

This image also contains `emm_download_makedb.py` from https://github.com/Daniel-VM/cdc-utilities for downloading the most-recent fasta file for emm typing.
  
Full documentation: https://github.com/MDU-PHL/emmtyper

## Example Usage

```bash
# run emmtyper in BLAST (default) mode:
emmtyper sample.fasta -o outfile

# or with output written in verbose format:
emmtyper sample.fasta -o outfile -f verbose

# run emmtyper in PCR mode (useful for troubleshooting, see documentation)
emmtyper -w pcr sample.fasta -o outfile 

# downloading a new fasta file for the most-current emm types
emm_download_makedb.py \
    --ftp_url 'https://ftp.cdc.gov/' \
    --remote_path 'pub/infectious_diseases/biotech/tsemm/' \
    --local_path ./out_fasta 

# using the database in the image downloaded via emm_download_makedb.py
emmtyper --blast_db /cdc_emm_database/cdc_emm sample.fasta -o outfile
```
