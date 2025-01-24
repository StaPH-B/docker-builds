# emmtyper container

Main tool : [emmtyper](https://github.com/MDU-PHL/emmtyper)

Code repository: https://github.com/MDU-PHL/emmtyper

Basic information on how to use this tool:
- executable: emmtyper
- help: --help
- version: --version
- description: |

'emmtyper' is a command line tool for emm-typing of _Streptococcus pyogenes_ using a _de novo_ or complete assembly.

Additional information:

This image uses the most up-to-date fasta file for emm typing by downloading from https://ftp.cdc.gov/pub/infectious_diseases/biotech/tsemm/alltrimmed.tfa. The out-of-date files are removed and overwritten at the time of building and deployment.
  
Full documentation: https://github.com/MDU-PHL/emmtyper

## Example Usage

```bash
# run emmtyper in BLAST (default) mode:

emmtyper <file name(s)>.fasta -o <output_file>

# or with output written in verbose format:

emmtyper <file name(s)>.fasta -o <output_file> -f verbose

# run emmtyper in PCR mode (useful for troubleshooting, see documentation)

emmtyper -w pcr <file name(s)>.fasta -o <output_file_2> 

```