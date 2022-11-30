# pasty container

Main tool : [pasty](https://github.com/rpetit3/pasty)

Additional tools:

- ncbi-blast+ 2.13.0
- python 3.11.0
- perl 5.32.1
- entrez-direct 16.2

Full documentation: [https://github.com/rpetit3/pasty](https://github.com/rpetit3/pasty)

A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies

## Example Usage

```bash
# download test P. aeruginosa assembly from pasty repo
# visit here to see all test data: https://github.com/rpetit3/pasty/tree/main/test
$ wget -q https://github.com/rpetit3/pasty/raw/main/test/O2-GCF_000006765.fna.gz

# run pasty via docker container
$ docker run --rm -v $PWD:/data -u $(id -u):$(id -g) staphb/pasty:1.0.0 \
    pasty --assembly /data/O2-GCF_000006765.fna.gz --outdir /data
Running BLASTN...
Writing outputs...
BLASTN results written to /data/O2-GCF_000006765.fna.blastn.tsv

                     Serogroup Results                     
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample               ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O2-GCF_000006765.fna │ O1        │ 12.52    │ 2         │
│ O2-GCF_000006765.fna │ O2        │ 100.00   │ 1         │
│ O2-GCF_000006765.fna │ O3        │ 1.43     │ 1         │
│ O2-GCF_000006765.fna │ O4        │ 13.86    │ 2         │
│ O2-GCF_000006765.fna │ O5        │ 0        │ 0         │
│ O2-GCF_000006765.fna │ O6        │ 14.78    │ 2         │
│ O2-GCF_000006765.fna │ O7        │ 11.82    │ 2         │
│ O2-GCF_000006765.fna │ O9        │ 11.42    │ 1         │
│ O2-GCF_000006765.fna │ O10       │ 12.97    │ 2         │
│ O2-GCF_000006765.fna │ O11       │ 15.87    │ 2         │
│ O2-GCF_000006765.fna │ O12       │ 0.00     │ 0         │
│ O2-GCF_000006765.fna │ O13       │ 16.22    │ 2         │
│ O2-GCF_000006765.fna │ WyzB      │ 0        │ 0         │
└──────────────────────┴───────────┴──────────┴───────────┘
Serogroup Results written to /data/O2-GCF_000006765.fna.details.tsv

                    Predicted Serogroup                    
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ sample               ┃ serogroup ┃ coverage ┃ fragments ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ O2-GCF_000006765.fna │ O2        │ 100.00   │ 1         │
└──────────────────────┴───────────┴──────────┴───────────┘
Predicted serogroup result written to /data/O2-GCF_000006765.fna.tsv
```
