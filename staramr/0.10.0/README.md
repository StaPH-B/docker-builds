# staramr container

Main tool : [staramr](https://github.com/phac-nml/staramr)

Additional tools:

- mlst 2.23.0
- ncbi-blast+ 2.9.0
- any2fasta 0.4.2
- Databases for PlasmidFinder, PointFinder, ResFinder

Database version information:

```
##### staramr db information at time of docker image build #####
resfinder_db_dir              = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/resfinder
resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
resfinder_db_commit           = 97d1fe0cd0a119172037f6bdb29f8a1c7c6e6019
resfinder_db_date             = Sun, 28 Jan 2024 15:59
pointfinder_db_dir            = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/pointfinder
pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
pointfinder_db_commit         = ce3c9aa002e9b57bf07412ae03c8a23ff1a2f95a
pointfinder_db_date           = Mon, 15 Jan 2024 10:24
pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
pointfinder_organisms_valid   = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, salmonella
plasmidfinder_db_dir          = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/plasmidfinder
plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
plasmidfinder_db_commit       = 81c11f4f2209ff12cb74b486bad4c5ede54418ad
plasmidfinder_db_date         = Mon, 04 Dec 2023 13:21
mlst_version                  = 2.23.0
pointfinder_gene_drug_version = 072621.2
resfinder_gene_drug_version   = 072621
```

Full documentation: https://github.com/phac-nml/staramr

staramr scans bacterial genome contigs for AMR genes and plasmids

## Example Usage

```bash
# run "staramr search" on a genome assembly (broken into multiple lines for readability)
staramr search -o /data/staramrtest-Salmonella \
  --pointfinder-organism salmonella \
  --plasmidfinder-database-type enterobacteriales \
  /data/salmonella_enterica_assembly.fasta
```
