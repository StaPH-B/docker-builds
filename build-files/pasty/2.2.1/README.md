# pasty container

Main tool : [pasty](https://github.com/rpetit3/pasty)

Additional tools:

- camlhmp 1.0.0
- blast 2.16.0+

Full documentation: [https://github.com/rpetit3/pasty](https://github.com/rpetit3/pasty)

A tool easily taken advantage of for in silico serogrouping of Pseudomonas aeruginosa isolates from genome assemblies

## Example Usage

```bash
pasty --input ./data/O1-GCF_001420225.fna.gz --prefix O1-GCF_001420225 --outdir results/

Running camlhmp with following parameters:
    --input ./data/O1-GCF_001420225.fna.gz
    --yaml /opt/conda/bin/../share/pasty/pa-osa.yaml
    --targets /opt/conda/bin/../share/pasty/pa-osa.fasta
    --outdir results/
    --prefix O1-GCF_001420225
    --min-pident 95
    --min-coverage 95

Starting camlhmp for P. aeruginosa serogrouping...
Running blastn...
Processing hits...
Final Results...
                                                          P. aeruginosa serogrouping                                                          
┏━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ sample           ┃ type ┃ targets ┃ coverages ┃ hits ┃ schema ┃ schema_version ┃ camlhmp_version ┃ params                        ┃ comment ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ O1-GCF_001420225 │ O1   │ O1      │ 100.00    │ 1    │ pasty  │ 2.1.0          │ 1.0.0           │ min-coverage=95;min-pident=95 │         │
└──────────────────┴──────┴─────────┴───────────┴──────┴────────┴────────────────┴─────────────────┴───────────────────────────────┴─────────┘
Writing outputs...
Final predicted type written to results/O1-GCF_001420225.tsv
Results against each type written to results/O1-GCF_001420225.details.tsv
blastn results written to results/O1-GCF_001420225.blastn.tsv
```
