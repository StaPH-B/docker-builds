# emmtyper container

Main tool : [emmtyper](https://github.com/MDU-PHL/emmtyper)

'emmtyper' is a command line tool for emm-typing of _Streptococcus pyogenes_ using a _de novo_ or complete assembly.

## Authors

- Andre Tan
- Torsten Seemann
- Jake Lacey
- Mark Davies
- Liam Mcintyre
- Hannah Frost
- Deborah Williamson
- Anders Gon&ccedil;alves da Silva

The codebase for `emmtyper` was primarly written by Andre Tan as part of his Master's
Degree in Bioinformatics. Torsten Seemann, Deborah Williamson, and Anders Gon&ccedil;alves da Silva provided supervision and assistance.

Hannah Frost contributed with EMM clustering by suggesting we incorporate it in to the code, and providing the necessary information to do so and test it.

Jake Lacey, Liam Mcintyre, and Mark Davies provided assistance in validating `emmtyper`.

## Maintainer

The code is actively maintained by MDU Bioinformatics Team.

Contact the principal maintainer at andersgs at gmail dot com.

## Example Usage

```bash
# run emmtyper in BLAST (default) mode:

emmtyper <file name(s)>.fasta -o <output_file>

# or with output written in verbose format:

emmtyper <file name(s)>.fasta -o <output_file> -f verbose

# run emmtyper in PCR mode (useful for troubleshooting, see documentation)

emmtyper -w pcr <file name(s)>.fasta -o <output_file_2> 

```