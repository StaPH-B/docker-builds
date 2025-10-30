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
resfinder_db_commit           = c0aa05c5cae9da75e4395e9fa3dd5057e3bf4a75
resfinder_db_date             = Tue, 09 Sep 2025 18:35
pointfinder_db_dir            = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/pointfinder
pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
pointfinder_db_commit         = 29d83a51cb41e429e38e46b1096608b9accb2b2a
pointfinder_db_date           = Fri, 22 Aug 2025 09:34
pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
pointfinder_organisms_valid   = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, salmonella
plasmidfinder_db_dir          = /usr/local/lib/python3.9/site-packages/staramr/databases/data/update/plasmidfinder
plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
plasmidfinder_db_commit       = 49c24c1c9401fa175fbcfdbd4b37227a160baca4
plasmidfinder_db_date         = Wed, 10 Sep 2025 18:56
mlst_version                  = 2.23.0
pointfinder_gene_drug_version = 070623
resfinder_gene_drug_version   = 072423
```

STARAMR uses several databases that it does not maintain. As such, this image is re-built twice a year for the latest of these databases {latest-version}={date of rebuilding}.


Full documentation: https://github.com/phac-nml/staramr

staramr scans bacterial genome contigs for AMR genes and plasmids

## Example Usage

```bash
# run "staramr search" on a genome assembly (broken into multiple lines for readability)
staramr search -o /data/staramrtest-Salmonella \
  --pointfinder-organism salmonella \
  --plasmidfinder-database-type enterobacteriales \
  /data/salmonella_enterica_assembly.fasta

# to get database information
staramr db info
```
