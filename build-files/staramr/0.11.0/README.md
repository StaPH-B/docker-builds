# staramr container

Main tool : [staramr](https://github.com/phac-nml/staramr)

Additional tools:

- mlst 2.23.0
- ncbi-blast+ 2.12.0+
- any2fasta 0.4.2
- Databases for PlasmidFinder, PointFinder, ResFinder

Database version information:

```
##### staramr db information at time of docker image build #####
resfinder_db_dir              = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/resfinder
resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
resfinder_db_commit           = d3b2312c9db22ec33e5e93368a314dde9c17d4ab
resfinder_db_date             = Fri, 13 Dec 2024 12:00
pointfinder_db_dir            = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/pointfinder
pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
pointfinder_db_commit         = 694919f59a38980204009e7ade76bf319cb7df0b
pointfinder_db_date           = Thu, 08 Aug 2024 11:57
pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
pointfinder_organisms_valid   = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, salmonella
plasmidfinder_db_dir          = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/plasmidfinder
plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
plasmidfinder_db_commit       = 4add282963c788762cdc3c6e91eb46c3d109f19b
plasmidfinder_db_date         = Thu, 14 Nov 2024 09:59
mlst_version                  = 2.23.0
pointfinder_gene_drug_version = 070623
resfinder_gene_drug_version   = 072423
```

This image is re-built every year to the latest databases.

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
