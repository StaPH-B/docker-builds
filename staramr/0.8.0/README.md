# staramr container

Main tool : [staramr](https://github.com/phac-nml/staramr)

Additional tools:

- mlst 2.22.1
- ncbi-blast+ 2.9.0
- any2fasta
- Databases for PlasmidFinder, PointFinder, ResFinder

Database version information:

```
##### staramr db information at time of docker image build #####
resfinder_db_dir              = /usr/local/lib/python3.8/dist-packages/staramr/databases/data/update/resfinder
resfinder_db_url              = https://bitbucket.org/genomicepidemiology/resfinder_db.git
resfinder_db_commit           = a4cc8bc1e969b3829ad0f0bd4a6cadf615ac9f21
resfinder_db_date             = Tue, 19 Jul 2022 07:16
pointfinder_db_dir            = /usr/local/lib/python3.8/dist-packages/staramr/databases/data/update/pointfinder
pointfinder_db_url            = https://bitbucket.org/genomicepidemiology/pointfinder_db.git
pointfinder_db_commit         = bfa17543d776faf3962ba1e824dec5f55a66d73b
pointfinder_db_date           = Fri, 22 Apr 2022 08:27
pointfinder_organisms_all     = campylobacter, enterococcus_faecalis, enterococcus_faecium, escherichia_coli, helicobacter_pylori, klebsiella, mycobacterium_tuberculosis, neisseria_gonorrhoeae, plasmodium_falciparum, salmonella, staphylococcus_aureus
pointfinder_organisms_valid   = campylobacter, salmonella
plasmidfinder_db_dir          = /usr/local/lib/python3.8/dist-packages/staramr/databases/data/update/plasmidfinder
plasmidfinder_db_url          = https://bitbucket.org/genomicepidemiology/plasmidfinder_db.git
plasmidfinder_db_commit       = 9002e7282dd0599b9247f4f700368b8fa64fbaa8
plasmidfinder_db_date         = Wed, 30 Mar 2022 09:20
mlst_version                  = 2.22.1
pointfinder_gene_drug_version = 072621
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
