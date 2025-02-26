# pasty container

Main tool : [pasty](https://github.com/rpetit3/pasty)

Additional tools:

- ncbi-blast+ 2.12.0
- python 3.10.6

Full documentation: [https://github.com/rpetit3/pasty](https://github.com/rpetit3/pasty)

A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies

## Example Usage

```bash
# test genome assemblies are included in the docker image at /pasty-1.0.2/test/
# visit here to see more information: https://github.com/rpetit3/pasty/tree/main/test

# run pasty via docker container (command broken into 2 lines for readability)
$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) staphb/pasty:1.0.2 \
    pasty --assembly /pasty-1.0.2/test/O1-GCF_000504045.fna.gz --prefix O1-GCF_000504045
Running pasty with following parameters:
    --assembly /pasty-1.0.2/test/O1-GCF_000504045.fna.gz
    --db /pasty-1.0.2/db/OSAdb.fasta
    --prefix O1-GCF_000504045
    --outdir ./
    --min_pident 95
    --min_coverage 95

Running BLASTN...
Writing outputs...
BLASTN results written to ./O1-GCF_000504045.blastn.tsv

                   Serogroup Results                   
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O1-GCF_000504045 │ O1        │ 99.97    │ 1         │
│ O1-GCF_000504045 │ O2        │ 9.83     │ 2         │
│ O1-GCF_000504045 │ O3        │ 11.18    │ 2         │
│ O1-GCF_000504045 │ O4        │ 14.36    │ 2         │
│ O1-GCF_000504045 │ O5        │ 0        │ 0         │
│ O1-GCF_000504045 │ O6        │ 14.07    │ 2         │
│ O1-GCF_000504045 │ O7        │ 11.54    │ 2         │
│ O1-GCF_000504045 │ O9        │ 36.62    │ 1         │
│ O1-GCF_000504045 │ O10       │ 12.52    │ 2         │
│ O1-GCF_000504045 │ O11       │ 15.85    │ 2         │
│ O1-GCF_000504045 │ O12       │ 1.24     │ 1         │
│ O1-GCF_000504045 │ O13       │ 15.39    │ 2         │
│ O1-GCF_000504045 │ WyzB      │ 0        │ 0         │
└──────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to ./O1-GCF_000504045.details.tsv

                       Predicted Serogroup                       
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ serogroup ┃ coverage ┃ fragments ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
│ O1-GCF_000504045 │ O1        │ 99.97    │ 1         │         │
└──────────────────┴───────────┴──────────┴───────────┴─────────┘
Predicted serogroup result written to ./O1-GCF_000504045.tsv
```
