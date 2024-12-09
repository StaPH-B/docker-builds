# pbptyper container

Main tool : [pbptyper](https://github.com/rpetit3/pbptyper)

Additional tools:

- ncbi-blast+ 2.13.0
- python 3.10.6
- perl 5.32.1
- entrez-direct 16.2
- fastANI 1.33

Full documentation: [https://github.com/rpetit3/pbptyper](https://github.com/rpetit3/pbptyper)

In silico Penicillin Binding Protein (PBP) typer for Streptococcus pneumoniae assemblies

## Example Usage

```bash
# run pbptyper on an test S. pneumo assembly included with pbptyper 
# WARNING: test data no longer included in docker image, visit here to get test data: https://github.com/rpetit3/pbptyper/tree/main/test
$ pbptyper --assembly SRR2912551.fna.gz --prefix SRR2912551 --db /pbptyper-*/db/ --outdir /SRR2912551-pbptyper-test
Running TBLASTN for 1A...
TBLASTN results written to /SRR2912551-pbptyper-test/SRR2912551-1A.tblastn.tsv

Running TBLASTN for 2B...
TBLASTN results written to /SRR2912551-pbptyper-test/SRR2912551-2B.tblastn.tsv

Running TBLASTN for 2X...
TBLASTN results written to /SRR2912551-pbptyper-test/SRR2912551-2X.tblastn.tsv

                                          Predicted PBP Type                                          
┏━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample     ┃ pbptype ┃ 1A_coverage ┃ 1A_pident ┃ 2B_coverage ┃ 2B_pident ┃ 2X_coverage ┃ 2X_pident ┃
┡━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ SRR2912551 │ 23:0:2  │ 100         │ 100.000   │ 100         │ 100.000   │ 100         │ 100.000   │
└────────────┴─────────┴─────────────┴───────────┴─────────────┴───────────┴─────────────┴───────────┘
Predicted pbp type result written to /SRR2912551-pbptyper-test/SRR2912551.tsv
```
